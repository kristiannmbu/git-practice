import json
import yaml
import pandas as pd


# Load configuration from YAML file
with open('config.yml', 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)

# Extract configuration parameters
max_days = config['max_days_since_calibration']
output_file = config['output_file']

# Read sensor data and calibration data
sensors = pd.read_excel('sensors.xlsx')
calibrations = pd.read_csv('calibrations.csv')

# Merge the two DataFrames on 'sensor_id'
merged_df = pd.merge(sensors, calibrations, on='sensor_id', how='left')

# Keep sensors overdue for calibration
filtered_df = merged_df[merged_df['days_since_calibration'] > max_days]

# Write the filtered DataFrame to a JSON file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(filtered_df.to_dict(orient='records'), f, ensure_ascii=False, indent=2)
