import os
import shutil

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

file_to_remove = os.path.join(os.getcwd(), 'molecule', 'cookiecutter.json')
# print(file_to_remove)

# Remove the cookiecutter.json file of the cookiecutter template to create additional scenario's
remove(file_to_remove)
print("\n\nPlease be careful. Azure resource group {{cookiecutter.azure_resource_group}} will be deleted when Molecule is done.")
