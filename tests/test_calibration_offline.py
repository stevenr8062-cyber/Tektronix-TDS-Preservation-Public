"""Exercise the project-authored synthetic parser with standard-library unittest."""
import unittest

from calibration_offline import compare_regions, validate_region


class CalibrationResearch(unittest.TestCase):
    fixture = [b"CALWORD 0,3\n", b"CALWORD 1,1\n", b"CALWORD 2,2\n"]

    def test_repeatable_valid_bytes_leave_origin_open(self):
        first = validate_region(self.fixture, 3)
        repeat = validate_region(self.fixture, 3)
        self.assertEqual(first["bytes"], 6)
        self.assertEqual(compare_regions(first, repeat), "consistent")
        self.assertEqual(first["factory_authenticity"], "not established")

    def test_bad_replies_retain_original_bytes(self):
        for reply in (b"", b"CALWORD 1,\n", b"CALWORD 1,1", b"CALWORD 1,1\r\n",
                      b"CALWORD 1,65536\n", b"CALWORD 0,1\n", b"CALWORD 2,1\n"):
            with self.subTest(reply=reply):
                decision = validate_region([self.fixture[0], reply, self.fixture[2]], 3)
                self.assertFalse(decision["complete"])
                self.assertEqual(decision["records"][1]["raw_hex"], reply.hex())

    def test_short_region_is_incomplete(self):
        first = validate_region(self.fixture, 3)
        short = validate_region(self.fixture[:-1], 3)
        self.assertEqual(compare_regions(first, short), "incomplete")

    def test_checksum_mismatch_is_reported(self):
        first = validate_region(self.fixture, 3)
        different = validate_region([self.fixture[0], b"CALWORD 1,9\n", self.fixture[2]], 3)
        self.assertEqual(compare_regions(first, different), "checksum_mismatch")


if __name__ == "__main__":
    unittest.main()
