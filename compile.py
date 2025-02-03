import glob
import json
import os
import pathlib
from dbgpu import GPUDatabase
import yaml
from rich import print
from rich.pretty import pprint

# Define file paths
PROJECT_ROOT = pathlib.Path(__file__).parent.resolve()
DB_ROOT = os.path.join(PROJECT_ROOT, "db")

# Define output properties
OUTPUT_ROOT = os.path.join(PROJECT_ROOT, "frontend")
OUTPUT_JSON_FILE_PATH = os.path.join(OUTPUT_ROOT, "db.json")

# Use TechPowerUp data to augment frontend output
tpu_db = GPUDatabase.default()

output = []

# Load all yaml files from db folder
for yaml_file_path in glob.glob(os.path.join(DB_ROOT, '**/*.yaml'), recursive=True):
    print(f'Loading [yellow]{yaml_file_path}[/yellow]')

    # https://stackoverflow.com/a/1774043/5337349
    with open(os.path.join(PROJECT_ROOT, yaml_file_path)) as stream:
        try:
            file_contents = yaml.safe_load(stream)
            tpu_specs = tpu_db[file_contents['gpu']]
            file_contents['tpu_url'] = tpu_specs.tpu_url
            file_contents['manufacturer'] = tpu_specs.manufacturer
            file_contents['release_year'] = tpu_specs.release_date.year
            output.append(file_contents)
            pprint(file_contents)
        except yaml.YAMLError as exc:
            print(exc)


# Dump output in JSON format for use by frontend
with open(OUTPUT_JSON_FILE_PATH, "w", encoding='utf-8') as json_output_file:
    json.dump(output, json_output_file, indent=2)
