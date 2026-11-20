# Research questions

1. **Native VISA open.** On an isolated or authorized test setup, does a Keysight 82357B and explicit native Keysight VISA bare session produce an implicit device clear or interface clear during provider initialization, open or close? Which stack, exact versions and trace support the result?
2. **Default substitution.** Which TDS700D board and firmware combinations can return firmware defaults during logical calibration extraction? What evidence identifies the table, selection logic and byte mapping?
3. **Independent EEPROM evidence.** What verified acquisition methods establish the contents and order of both acquisition EEPROM devices? How was independence from a cached or fallback view demonstrated?
4. **HDD framing.** On V6.6e, what bytes and native END/status appear for a known file? Include independently known size, hash, chunk boundary and framing summary. Keep real file contents private.
5. **Dallas memory.** Which address ranges and device variants can be independently preserved without changing calibration or configuration? Identify RTC bytes, mirror behavior, unreadable regions and observed runtime effects.
