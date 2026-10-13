# Export coverage

Snapshot: 13 October 2026. 10 uploaded files contain 19,539 data rows. 9 distinct files contain 18,167 rows after excluding the byte-identical second copy.

| Export | Original file | Records | First reported time | Last reported time | Unrepresented hour slots | Coverage | Duplicate of |
| --- | --- | ---: | --- | --- | ---: | ---: | --- |
| export_00 | export.csv | 3,485 | 2026-05-13 12:00:00 | 2026-10-13 12:00:00 | 188 | 94.9% | — |
| export_01 | export (1).csv | 1,608 | 2026-06-12 17:00:00 | 2026-09-22 16:00:00 | 840 | 65.7% | — |
| export_02 | export (2).csv | 2,337 | 2026-06-10 13:00:00 | 2026-10-13 20:00:00 | 671 | 77.7% | — |
| export_03 | export (3).csv | 1,788 | 2026-06-29 18:00:00 | 2026-10-13 16:00:00 | 755 | 70.3% | — |
| export_04 | export (4).csv | 2,392 | 2026-07-04 15:00:00 | 2026-10-13 16:00:00 | 34 | 98.6% | — |
| export_05 | export (5).csv | 2,286 | 2026-07-08 12:00:00 | 2026-10-13 16:00:00 | 47 | 98.0% | — |
| export_06 | export (6).csv | 1,372 | 2026-07-11 11:00:00 | 2026-10-13 14:00:00 | 888 | 60.7% | — |
| export_07 | export (7).csv | 1,372 | 2026-07-11 11:00:00 | 2026-10-13 14:00:00 | 888 | 60.7% | export_06 |
| export_08 | export (8).csv | 1,604 | 2026-08-06 16:00:00 | 2026-10-13 08:00:00 | 21 | 98.7% | — |
| export_09 | export (9).csv | 1,295 | 2026-05-27 05:00:00 | 2026-10-13 13:00:00 | 2,050 | 38.7% | — |

## Observations

- **export_01:** 7 PF values outside 0 to 1; retained.
- **export_04:** 15 PF values outside 0 to 1; retained.
- **export_05:** 68 PF values outside 0 to 1; retained.
- **export_09:** Current and active power are zero in every provided record.

Every file has gaps in its hourly timestamp grid. Coverage is observed unique timestamps divided by the inclusive one-hour civil-time grid from that file's first to last timestamp. It does not measure availability of the power supply or the fraction of all stored IAMMETER data exported. No missing intervals are filled.

## Identification

The source files have no lab, meter, phase or time-zone identifiers. Numbered identities are retained until these are confirmed. Complete metadata/lab_mapping.csv before interpreting these exports as individual living labs or assigning UTC timestamps.
