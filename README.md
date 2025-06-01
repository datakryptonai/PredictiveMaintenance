# Tableau Dashboard Setup

This folder contains instructions to connect Tableau Desktop to the processed data files.

## Connecting to Data

- Open Tableau Desktop.
- Connect to the Parquet file located at `../data/processed/features.parquet`.
- Build visualizations:
  - Line charts for sensor trends (temperature, vibration).
  - Color-coded risk score tables.
  - Bar charts for predicted failure counts.
- Add filters for `machine_id` and `timestamp` ranges.

## Recommended Dashboard Layout

- Top section: Equipment status summary with risk scores.
- Middle: Time series line charts for sensor metrics.
- Bottom: Predicted failure alerts and maintenance scheduling.
