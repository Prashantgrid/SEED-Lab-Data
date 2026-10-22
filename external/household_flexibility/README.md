# External datasets for Household Flexibility Classes

This is a **separate external-data collection** for the household-flexibility
classification research. It is not part of the ten SEED living-lab meter exports
in this repository. Original SEED files remain unchanged.

## Reproducible first import

Run from the repository root:

```bash
python external/household_flexibility/fetch_datasets.py
```

The script downloads source data into `external/household_flexibility/data/`
and records checksums and outcomes in `download_manifest.json`. It downloads
only the manageable source files described below, not all nine catalogued
archives. It does not invent household profiles or simulate measured responses.

| Collection | Source / version | Files selected | Evidence and cautions |
|---|---|---|---|
| Norway residential EV | Sørensen et al., Zenodo v2, DOI [10.5281/zenodo.13896176](https://doi.org/10.5281/zenodo.13896176) | Dataset1 charging reports; Dataset2 user predictions; Dataset3 session predictions | **Dataset1 records plug-in, plug-out and charging energy**. The user- and session-level charger power, battery capacity and SoC fields are **model-derived predictions**, not direct measurements. The dataset has ~35,377 sessions, 267 IDs and 12 locations. |
| OPSD / CoSSMic household | [OPSD Household Data v2020-04-15](https://data.open-power-system-data.org/household_data/2020-04-15/) | `household_data_60min_singleindex.csv` | Meter-based household and device-channel energy for 11 Southern German households, with explicit notes on interpolation and missingness. Hourly data are inappropriate for sub-five-minute response testing. |

**Attribution:** Sørensen, Å. L., Sartori, I., Lindberg, K. B., and
Andresen, I. (2024), *Electric vehicle charging dataset with 35,000
charging sessions from 12 residential locations in Norway*,
Data in Brief 57, 110883, https://doi.org/10.1016/j.dib.2024.110883.
Original data at https://doi.org/10.5281/zenodo.13896176.
OPSD (2020), *Data Package Household Data*, version 2020-04-15,
https://data.open-power-system-data.org/household_data/2020-04-15/.
These third-party data retain their original CC BY attribution terms.
Keep these notices with any redistribution.

## Other useful datasets — **not imported by this script**

- **WPuQ (Germany):** 38 individual households with separate heat-pump
  measurements; project https://isfh.de/en/projects/wind-solar-heat-pumps-neighborhood ;
  paper https://doi.org/10.1038/s41597-022-01156-1 . Original HDF5 is too large
  for a routine Git commit. Obtain the 15- or 60-minute version separately.
- **Dingle Peninsula, Ireland:** four homes with PV, BESS, heat pumps and
  EV journey logs, https://doi.org/10.1038/s41597-026-07186-3 .
- **HEAPO, Switzerland:** measured smart-meter heat-pump homes and field
  protocols, https://github.com/tbrumue/heapo .
- **UK DfT domestic charging 2017:** published historical chargepoint usage,
  https://www.data.gov.uk/dataset/5438d88d-695b-4381-a5f2-6ea03bf3dcf0/electric-chargepoint-analysis-2017-domestics .
- **MaStR, Germany:** public registry of equipment ratings; not operational
  availability observations, https://www.marktstammdatenregister.de/ .
- **Pecan Street Dataport:** access/licensing required; not mirrored here.
- **Electric Nation / Low Carbon London:** trial datasets may require
  application or licensing; not mirrored here.

## Interpretation for the paper

Measured charging sessions are evidence of *observed past plug-in/charge
behavior*, not measured willingness to respond to a DSO signal. None of
these files proves 95% flexible-service delivery on its own. In particular,
EV charger-power estimates are not equipment nameplate measurements,
OPSD hourly data do not resolve 1-5 minute control, and joining records
from different countries **does not create a measured multi-device household**.

See `fetch_datasets.py` for exact source URLs, checksum verification,
and the reproducible import procedure.
