# Export coverage

Snapshot: 13 October 2026. The ten user-labelled lab files contain **19,539 records**. There are nine distinct raw file contents and **18,167 records** in the optional distinct-content view.

| Lab | Records | First reported time | Last reported time | Unrepresented hour slots | Coverage |
| --- | ---: | --- | --- | ---: | ---: |
| BIT STUDENTS DORMS | 3,485 | 2026-05-13 12:00:00 | 2026-10-13 12:00:00 | 188 | 94.9% |
| IITB-Pabal | 1,608 | 2026-06-12 17:00:00 | 2026-09-22 16:00:00 | 840 | 65.7% |
| ITB Living Lab Garut | 2,337 | 2026-06-10 13:00:00 | 2026-10-13 20:00:00 | 671 | 77.7% |
| BDU TUM SEED Living Lab1 | 1,788 | 2026-06-29 18:00:00 | 2026-10-13 16:00:00 | 755 | 70.3% |
| MAK TUMSEED | 2,392 | 2026-07-04 15:00:00 | 2026-10-13 16:00:00 | 34 | 98.6% |
| JKUAT Living Lab | 2,286 | 2026-07-08 12:00:00 | 2026-10-13 16:00:00 | 47 | 98.0% |
| NUST SEED Living Lab | 1,372 | 2026-07-11 11:00:00 | 2026-10-13 14:00:00 | 888 | 60.7% |
| HUYRO SM-MT-2026-01 | 1,372 | 2026-07-11 11:00:00 | 2026-10-13 14:00:00 | 888 | 60.7% |
| KNUST_Yeboakrom | 1,604 | 2026-08-06 16:00:00 | 2026-10-13 08:00:00 | 21 | 98.7% |
| HUYRO SM-LM-2026-01 | 1,295 | 2026-05-27 05:00:00 | 2026-10-13 13:00:00 | 2,050 | 38.7% |

## File labels

| User order | Lab | Original CSV | Named dataset |
| ---: | --- | --- | --- |
| 1 | BIT STUDENTS DORMS | export.csv | [BIT_STUDENTS_DORMS.csv](data/BIT_STUDENTS_DORMS.csv) |
| 2 | IITB-Pabal | export (1).csv | [IITB_Pabal.csv](data/IITB_Pabal.csv) |
| 3 | ITB Living Lab Garut | export (2).csv | [ITB_Living_Lab_Garut.csv](data/ITB_Living_Lab_Garut.csv) |
| 4 | BDU TUM SEED Living Lab1 | export (3).csv | [BDU_TUM_SEED_Living_Lab1.csv](data/BDU_TUM_SEED_Living_Lab1.csv) |
| 5 | MAK TUMSEED | export (4).csv | [MAK_TUMSEED.csv](data/MAK_TUMSEED.csv) |
| 6 | JKUAT Living Lab | export (5).csv | [JKUAT_Living_Lab.csv](data/JKUAT_Living_Lab.csv) |
| 7 | NUST SEED Living Lab | export (6).csv | [NUST_SEED_Living_Lab.csv](data/NUST_SEED_Living_Lab.csv) |
| 8 | HUYRO SM-MT-2026-01 | export (7).csv | [HUYRO_SM_MT_2026_01.csv](data/HUYRO_SM_MT_2026_01.csv) |
| 9 | KNUST_Yeboakrom | export (8).csv | [KNUST_Yeboakrom.csv](data/KNUST_Yeboakrom.csv) |
| 10 | HUYRO SM-LM-2026-01 | export (9).csv | [HUYRO_SM_LM_2026_01.csv](data/HUYRO_SM_LM_2026_01.csv) |

## Duplicate across two lab labels

The original HUYRO SM-MT-2026-01 export, export (7).csv, is byte-identical to the NUST SEED Living Lab export, export (6).csv. Their first reported reading is 2026-07-11 11:00:00. Both named datasets are retained under the user-supplied labels, and the main all_living_labs.csv file retains both. Verify the HUYRO SM-MT export before treating the two files as independent lab measurements. The distinct-content view excludes the HUYRO SM-MT copy.

## Other observations

- HUYRO SM-LM-2026-01 has zero current and power in all 1,295 provided records. Its voltage readings are retained.
- 90 PF readings fall outside 0 to 1. They are retained and listed in metadata/quality_flags.csv.
- Every file has gaps in its hourly timestamp grid. No gaps are filled.

Coverage is observed unique timestamps divided by the inclusive one-hour civil-time grid between the first and last timestamp of that export. It does not represent electricity supply availability or prove that all stored cloud records were exported. Meter serials, phases and time zones remain unspecified by the files.
