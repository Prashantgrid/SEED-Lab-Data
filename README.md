# SEED Lab Data

Electrical measurements from ten IAMMETER CSV exports supplied on 13 October 2026. The collection contains **9 distinct exported series and 18,167 rows**, with reported dates spanning 2026-05-13 to 2026-10-13. Lab, meter and phase identities require confirmation.

[Coverage summary](EXPORT_SUMMARY.md) · [Original exports](raw/) · [Standardized datasets](data/) · [Data dictionary](metadata/data_dictionary.csv)

## Files

- **raw/**: all ten original CSV files, preserved byte for byte.
- **data/export_00.csv to data/export_09.csv**: one standardized file for each supplied export. export_00 corresponds to export.csv; the remaining numbers correspond to the parenthesized source numbers.
- **data/all_distinct_exports.csv**: the nine distinct exports concatenated, with dataset and source identifiers. The exact duplicate export_07 is excluded.
- **metadata/coverage.csv** and **EXPORT_SUMMARY.md**: observed date ranges, record counts, unrepresented hourly slots, and duplicate information.
- **metadata/data_gaps.csv**: each gap between observed timestamps in the nine distinct exports.
- **metadata/quality_flags.csv**: zero-voltage readings and PF values outside 0 to 1, retained without modification.
- **metadata/data_dictionary.csv**: definitions, units and provenance of each standardized data column.
- **metadata/lab_mapping.csv**: fields for confirming lab name, meter serial, phase and time zone. These fields are initially blank.
- **metadata/manifest.json**: coverage, numeric ranges, processing choices and original-file SHA-256 hashes.
- **metadata/validation.json**: independent checks of numerical preservation, row counts, duplicate handling and the original files.
- **SHA256SUMS.txt**: integrity hashes for the files in this snapshot.

## Measurements and time

Each data row contains a reported timestamp, voltage, current, active power, apparent power and power factor. The timestamps fall on an hourly grid. The CSVs do not state whether a row is an instantaneous reading, an hourly mean, or another aggregation. Minute-level measurements and energy-meter readings are not present in these files.

The interpreted units are V, A, W, VA and dimensionless PF. The source CSV headers do not explicitly specify units. These interpretations follow IAMMETER measurement conventions and the numerical relationship between voltage, current and apparent power. Apparent power and PF remain as exported.

Timestamps use **YYYY-MM-DDTHH:MM:SS**, with no timezone suffix. All original clock fields are preserved. Different countries and place settings may use different time zones. Confirm the source time zone for each series before conversion to UTC, cross-lab alignment or elapsed-duration analysis.

## Preparation

The standardized files remove numeric thousands separators, normalize the written timestamp format and add source provenance. Every supplied reading is retained, including negative active power, zero values and PF values above 1. No values are interpolated, corrected or removed.

The ten raw files contain 19,539 rows. **export (6).csv and export (7).csv are byte-identical**. Both original files and their individual standardized versions are retained; the merged file includes that series once as export_06, leaving 18,167 rows. This is file-level duplicate removal, not deduplication across different measured series.

**export (9).csv has zero current, active power, apparent power and PF throughout its 1,295 records.** Its voltage readings are retained. The export alone does not establish whether the channel was unloaded, unconnected or affected by a measurement problem.

Gaps describe unrepresented civil-time slots within each export's observed horizon. They do not demonstrate a grid outage, unmet demand or meter downtime. The exports alone also do not establish that all historical data from all living labs, meters and phases were supplied.

## Lab identification

Complete the blank lab_name, meter_sn, phase and time_zone fields in metadata/lab_mapping.csv using the export's actual IAMMETER place and channel. File sequence and first observation dates are insufficient to establish those identities. Preserve dataset_id as the stable key when applying labels.

## Source documentation

- [IAMMETER WEM3080T datasheet](https://www.iammeter.com/docs/wem3080t-datasheet)
- [IAMMETER Cloud API documentation](https://www.iammeter.com/docs/system-api)

The measurements in this repository come from the supplied CSV files. The vendor documentation provides measurement context; it does not establish the identity or completeness of these particular exports.
