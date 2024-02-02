import os
import subprocess

def install_requirements(parent_directory):
    # Loop through all items in the parent directory
    for item in os.listdir(parent_directory):
        # Construct the full path
        item_path = os.path.join(parent_directory, item)
        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Construct the path to the requirements.txt file
            requirements_path = os.path.join(item_path, 'requirements.txt')
            # Check if the requirements.txt file exists
            if os.path.isfile(requirements_path):
                # Run pip install
                subprocess.check_call(['pip', 'install', '-r', requirements_path])

# Call the function with the path to the parent directory
install_requirements('./')