# molecule_template
[Cookiecutter](https://cookiecutter.readthedocs.io) templates for [Ansible](https://docs.ansible.com/) roles that use [Molecule](https://molecule.readthedocs.io/) 

Version: 0.1.2

# Description

Molecule used to have it's own template system but that was pre version 3. Starting with version 3 external template systems can be used if the scaffolding created by ```molecule init``` is not enough. This repo contains templates to create specialized Molecule scenario's. The [Cookiecutter](https://cookiecutter.readthedocs.io) tool is used to convert the templates in scaffolding ready to be used for your Ansible project.

# Azure

The [molecule_azure](https://github.com/ansible-community/molecule-azure) driver can be used if you need Azure VM's to develop or test your Ansible Role. The cookiecutter template in the Azure directory will generate the scaffolding for an Ansible role where Molecule creates a Windows 2012R VM, a Windows 2016 VM and a Windows 2019 VM and/or where Molecule creates 3 CentOS VM's (Version 6, 7 and 8). Modify the molecule.yml file in the scenario directories to let Molecule create a different set of VM's.

## DANGER ZONE

The cookiecutter template in the Azure directory will create an Ansible role that contains a Molecule directory for developing and testing the role. Running Molecule will create a resource group in Azure and will also remove that resource group, AND EVERYTHING IN IT, when done. MAKE ABSOLUTELY SURE YOU KNOW WHAT YOU ARE DOING AND DO NOT ACCIDENTALLY DESTROY A RESOURCE GROUP THAT IS USED OUTSIDE MOLECULE.

To prevent mistakes you could create a dedicated Azure subscription for Molecule (and other tools for automated testing)

Also make sure, for financial and security reasons, that all resource groups created by Molecule are destroyed when you are done. 

## Prepare your developer machine

* Create Azure credentials. A credentials file like the one below should be enough to run the example below. See: https://docs.ansible.com/ansible/latest/scenario_guides/guide_azure.html#authenticating-with-azure. 
```
cat ~/.azure/credentials 
    [default]
    subscription_id=
    client_id=
    secret=
    tenant=
```

* Install molecule_azure. See the usage section below or: https://github.com/ansible-community/molecule-azure.
* Install the Azure collection. See the usage section below or: https://github.com/ansible-collections/azure#installation
* Install cookiecutter. See the usage section below or: https://cookiecutter.readthedocs.io/en/latest/installation.html

## Usage

Follow the instructions below to create the scaffolding for a new Ansible role which uses Molecule to develop and test the role.


Example usage:

In the examples below '~/git/molecule_template' is the directory where you cloned this repo and azure is the subdirectory with the templates to create Linux and/or Windows VM's in Azure.


* cd to the directory where you want to create your role
* Create a Python virtual env with Ansible, Azure roles, molecule and molecule_azure. Select either Ansible 2.9 or Ansible 2.11:

### Ansible 2.9 
```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip wheel==0.30.0
pip install -r ~/git/molecule_template/azure/requirements_ansible_2.9.13.txt
ansible-galaxy collection install azure.azcollection
```

requirements_ansible_2.9.13.txt was created with:
```
pip install --upgrade ansible[azure]==2.9.13 molecule[lint] molecule-azure cookiecutter
pip freeze > requirements_ansible_2.9.13.txt
```  

### Ansible 2.11 

```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip wheel
pip install -r ~/git/molecule_template/azure/requirements_ansible_2.11.6.txt
ansible-galaxy collection install azure.azcollection
```
requirements_ansible_2.11.6.txt was created with:

```
wget https://github.com/ansible-collections/azure/raw/dev/requirements-azure.txt
pip install -r requirements-azure.txt
pip install --upgrade ansible molecule[lint] molecule-azure cookiecutter
pip freeze > requirements_ansible_2.11.6.txt
```
### Create the scaffolding for the new role

```
cookiecutter ~/git/molecule_template/azure
    role_name [solve_everything]: 
    molecule_scenario_name [default]: 
    Select molecule_scenario_os_type:
    1 - linux
    2 - windows
    Choose from 1, 2 [1]: 
    azure_location [Westeurope]: 
    azure_resource_group [molecule_solve_everything_default]: 
```
At this stage you can ```cd``` into the newly created project directory and run:

    molecule create   

To create a new development and test environment in Azure.  To run your new role you do:

    molecule converge

To destroy the VM's create by Molecule you do:

    molecule destroy

If you want to create an additional Molecule scenario:
```
    cd solve_everything/molecule
    cookiecutter ~/git/molecule_template/azure/\{\{cookiecutter.role_name\}\}/molecule/
        role_name [solve_everything]:
        molecule_scenario_name [default]: win
        Select molecule_scenario_os_type:
        1 - linux
        2 - windows
        Choose from 1, 2 [1]: 2
        azure_location [Westeurope]: 
        azure_resource_group [molecule_solve_everything_win]: 
    cd ..
    molecule create --scenario-name win
```

# Molecule links
* [Use cookiecutter to create scenario's](https://github.com/rocknsm/molecule-cookiecutter-vsphere)
* [Use cookiecutter to create an Ansible role and configure molecule](https://github.com/retr0h/cookiecutter-molecule)

# Cookiecutter links
* [Commandline options](https://cookiecutter.readthedocs.io/en/1.7.2/usage.html)
* [Choice variables](https://cookiecutter.readthedocs.io/en/latest/advanced/choice_variables.html)
* [Organizing cookiecutters in directories](https://cookiecutter.readthedocs.io/en/1.7.2/advanced/directories.html#organizing-cookiecutters-in-directories-1-7)
* https://github.com/cookiecutter/cookiecutter/issues/723#issuecomment-350561930

