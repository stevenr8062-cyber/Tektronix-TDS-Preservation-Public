# Tektronix TDS Preservation Research

An independent research project on preserving Tektronix TDS500, TDS600 and TDS700 instruments. The reference case is a TDS784D running V6.6e. Unit identifiers and private bench records are kept in the engineering archive. The investigation concerns Windows 11, a Keysight 82357B USB–GPIB adapter, and the native Keysight VISA provider.

Factory calibration is a preservation priority. A logical calibration read can return a coherent block while its origin remains unknown. Matching repeats and checksums establish consistency under the tested rules. Authentication requires independent evidence that covers both acquisition-board EEPROM devices and accounts for any cached or substitute values. GPIB file extraction addresses named files. A sector image has a different scope and includes filesystem structures and other addressable sectors.

| Evidence type | What it supports |
|---|---|
| Community reports | Owners report useful results on several TDS models with different firmware, host stacks and adapters. The firmware-default substitution report remains a hypothesis for the reference instrument. |
| Source inspection | High-level and provider-specific session initialization must be distinguished. Some reviewed utilities explicitly clear devices or change settings. |
| Host-only tests | This repository demonstrates strict parsing of indexed synthetic words and shows why checksum consistency cannot authenticate a block. |
| Physical behavior | The reference instrument has historical basic identification evidence. The bypass path, calibration provenance, native open/close behavior and exact file framing remain open. |

## Reproduce the synthetic tests

From the repository root on Python 3.12 or 3.13:

```sh
python -B -m unittest discover -s tests -v
```

The demonstration uses the Python standard library, synthetic fixtures and no VISA or hardware interface. Its CALWORD grammar is invented for the tests. See [experimental scope](docs/EXPERIMENTAL.md), [research questions](docs/RESEARCH_QUESTIONS.md) and [source provenance](docs/SOURCES.md).

## Maintainer and license

Steven R Veneskey maintains this project and holds copyright in the project-authored release. Copyright (c) 2026 Steven R Veneskey. The [MIT License](LICENSE) covers the project-authored material in this repository. Referenced third-party resources remain subject to their respective terms.
