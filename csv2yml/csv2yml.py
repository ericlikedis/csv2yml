import csv
import yaml

# Defining variables for csv file path and the yml output file.
csv_file_path = 'sample_data.csv'
yaml_file_path = 'output.yml'

def csv_to_yaml(csv_file_path, yaml_file_path):
    # Open CSV file
    with open(csv_file_path, 'r') as csv_file:
        # Read CSV data
        csv_reader = csv.DictReader(csv_file)
        
        with open(yaml_file_path, 'w') as yaml_file:

        
            # Prepare data for YAML
            yaml_data = []
            for row in csv_reader:
                yaml_row = {
                    'field': row.get('field', ),
                    'name': row.get('name', ),
                    'type': row.get('type', ),
                    'description': row.get('description'),
                    'example': row.get('example', )
                }
                yaml_data.append(yaml_row)
        
        # Write YAML data to file
        
                yaml.dump([yaml_row], yaml_file, default_flow_style=False, sort_keys=False) 
                yaml_file.write('\n ')
# Example usage

csv_to_yaml(csv_file_path, yaml_file_path)