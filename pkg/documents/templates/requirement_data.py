import yaml
import os


def get_requirements_data(chart_yaml_folder, chart_data):
    """
    Reads and combines the requirements data from the 'requirements.yaml' file and the chart data.

    Args:
        chart_yaml_folder (str): Path to the folder containing the chart's YAML files.
        chart_data (dict): Data containing information about the chart.

    Returns:
        dict: Combined requirements data from 'requirements.yaml' and chart data.
    """
    requirements_path = os.path.join(chart_yaml_folder, 'requirements.yaml')  # Construct the path to requirements.yaml

    if not os.path.exists(requirements_path):
        print(f"Warning: '{requirements_path}' does not exist.")
        return {}  # Return an empty dictionary if the file doesn't exist

    with open(requirements_path, 'r') as chart_file:
        requirements_data = yaml.safe_load(chart_file) or {}  # Load requirements data or initialize as empty dictionary

    chart_dependencies = chart_data.get('dependencies', [])  # Extract chart dependencies from chart_data
    requirements_data['dependencies'] += chart_dependencies  # Add chart dependencies to requirements data

    return requirements_data
