# SEED Lab Data

Electrical measurements from ten IAMMETER CSV exports supplied on 13 October 2026, labelled using the user's numbered place list. The collection contains **ten lab labels, 19,539 rows and nine distinct raw file contents**. Reported dates span 13 May to 13 October 2026.

[Coverage summary](EXPORT_SUMMARY.md) · [Original exports](raw/) · [Named datasets](data/) · [Data dictionary](metadata/data_dictionary.csv)

## Lab datasets

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

## Data and documentation

- **raw/** contains the ten original CSV exports, preserved byte for byte.
- **data/** contains one named dataset for each user-labelled living lab. Each row carries lab_name, a stable dataset_id, source filename and source record index.
- **[data/all_living_labs.csv](data/all_living_labs.csv)** contains all ten labelled exports and all 19,539 rows, including the duplicated contents under two supplied lab labels.
- **[data/all_distinct_exports.csv](data/all_distinct_exports.csv)** is an optional distinct-content view with 18,167 rows. It excludes the byte-identical HUYRO SM-MT copy.
- **metadata/coverage.csv** contains date ranges, record counts, hourly-grid coverage and duplicate notes.
- **metadata/data_gaps.csv** lists gaps for the nine distinct raw contents. HUYRO SM-MT has the same gaps as its identical NUST copy.
- **metadata/quality_flags.csv** lists zero-voltage readings and PF values outside 0 to 1 in the nine distinct raw contents. Values remain unmodified.
- **metadata/data_dictionary.csv** defines columns, units and provenance.
- **metadata/lab_mapping.csv** contains the supplied lab labels. Meter serial, phase and time-zone fields remain blank.
- **metadata/manifest.json** records source-file hashes, coverage, numeric ranges and preparation choices.
- **metadata/validation.json** reports independent numerical, timestamp, label and archive checks.
- **SHA256SUMS.txt** records hashes for this data snapshot.

## Duplicate requiring verification

**HUYRO SM-MT-2026-01, export (7).csv, is byte-identical to NUST SEED Living Lab, export (6).csv.** The files have 1,372 identical readings from 11 July to 13 October 2026. The user supplied different lab labels, so both named files and both copies in the main merged dataset are preserved. Verify the source export before using them as independent measurements. The distinct-content view includes this content once under the NUST label.

**HUYRO SM-LM-2026-01, export (9).csv, has zero current, active power, apparent power and PF in all 1,295 records.** Voltage readings are retained. The file alone does not establish whether this channel was unloaded, unconnected or affected by a measurement problem.

## Measurements and timestamps

Each row contains voltage, current, active power, apparent power and power factor at a reported hourly timestamp. The CSVs do not state whether a row is an instantaneous reading, an hourly mean or another aggregation. Minute-level measurements and energy-meter readings are not included.

The interpreted units are V, A, W, VA and dimensionless PF. Source headers omit explicit units. These interpretations follow IAMMETER measurement conventions and the numerical relationship between voltage, current and apparent power. Apparent power and PF remain as exported.

Timestamps use **YYYY-MM-DDTHH:MM:SS** without a timezone suffix. All original clock fields are preserved. Confirm each source time zone before conversion to UTC or cross-lab time alignment.

## Preparation

The standardized data remove numeric thousands separators, normalize written timestamps and add provenance and user-supplied lab labels. Every supplied value is retained, including negative power, zero values and PF above 1. No readings are interpolated, corrected or removed.

Gaps describe unrepresented one-hour civil-time slots inside each export's observed horizon. They do not establish grid outages, unmet demand or meter downtime. The supplied files also do not establish completeness across all historical records, meters and phases at every living lab.

## Source documentation

- [IAMMETER WEM3080T datasheet](https://www.iammeter.com/docs/wem3080t-datasheet)
- [IAMMETER Cloud API documentation](https://www.iammeter.com/docs/system-api)

Measurements come from the supplied CSVs. Lab labels come from the user's numbered place list. The vendor documentation supplies measurement context; it does not identify or verify these exports.
