"""Synthetic-only indexed logical calibration validation. No instrument I/O."""
import hashlib
import re
import struct

# Deliberately synthetic grammar. It is not a claim about TDS784D firmware.
REPLY = re.compile(rb"CALWORD ([0-9]{1,4}),(-?[0-9]{1,5})\n")


def validate_region(responses, word_count=252):
    """Return raw hex and decisions for a complete ordered synthetic region."""
    if not 1 <= word_count <= 252:
        raise ValueError("synthetic region must contain 1–252 words")
    records = []
    words = []
    seen = set()
    for ordinal, raw in enumerate(responses):
        record = {"ordinal": ordinal, "raw_hex": raw.hex()}
        records.append(record)
        match = REPLY.fullmatch(raw)
        if match is None:
            record["decision"] = "invalid grammar or termination"
            continue
        index, value = map(int, match.groups())
        if index in seen:
            record["decision"] = "duplicate index"
        elif index != ordinal or index >= word_count:
            record["decision"] = "unexpected index"
        elif not -32768 <= value <= 65535:
            record["decision"] = "value outside synthetic 16-bit range"
        else:
            record["decision"] = "accepted word"
            words.append(value & 65535)
        seen.add(index)
    complete = len(records) == len(words) == word_count
    result = {"records": records, "expected_words": word_count,
              "complete": complete, "factory_authenticity": "not established"}
    if complete:
        payload = struct.pack(f">{word_count}H", *words)
        result.update(bytes=len(payload), sha256=hashlib.sha256(payload).hexdigest(),
                      checksum="match" if words[0] == sum(words[1:]) & 65535 else "mismatch")
    return result


def compare_regions(first, second):
    """Compare complete data representations, without attributing origin."""
    if not first["complete"] or not second["complete"]:
        return "incomplete"
    if first["checksum"] != "match" or second["checksum"] != "match":
        return "checksum_mismatch"
    return "consistent" if first["sha256"] == second["sha256"] else "different"
