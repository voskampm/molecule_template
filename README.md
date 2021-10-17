# molecule_template
Cookiecutter templates for molecule

## Description

Molecule used to have it's own template system but that was pre version 3. Starting with version 3 external template systems can be used if the scaffolding created by ```molecule init``` is not enough. This repo contains templates to create specialized Molecule scenario's. The [Cookiecutter](https://cookiecutter.readthedocs.io) tool is used to converts the templates in scaffolding ready to be be used for your project.

## DANGER ZONE

This cookiecutter template will create a resource group in Azure and will also remove that resource group, AND EVERYTHING IN IT, when done. MAKE ABSOLUTELY SURE YOU KNOW WHAT YOU ARE DOING AND DO NOT ACCIDENTALLY DESTROY A RESOURCE GROUP THAT IS USED OUTSIDE MOLECULE.

To prevent mistakes you could create a dedicated subscription for Molecule (and other tools for automated testing)

Also make sure, for financial reasons, that all resource groups created by Molecule are destroyed when you are done. 

## Prepare your developer machine

* Create Azure credentails. See: https://docs.ansible.com/ansible/latest/scenario_guides/guide_azure.html#authenticating-with-azure
* Install molecule_azure
* Install cookiecutter

## Usage

* Create a new Ansible role with the for example the instructions on: https://molecule.readthedocs.io/en/latest/getting-started.html#creating-a-new-role
* Go to the molecule directory and create a new scenario with:

    cookiecutter ~/git/molecule_template/azure/windows

Where '~/git/molecule_template' is the directory where you cloned this repo and azure/windows is the subdirectory with the templates to create Windows VM's in Azure.

Example:

    cookiecutter ~/git/molecule_template/azure
        role_name [test]: solve_everything 
        molecule_scenario_name [default]: 
        Select molecule_scenario_os_type:
        1 - linux
        2 - windows
        Choose from 1, 2 [1]: 
        azure_location [Westeurope]: 
        azure_resource_group [molecule_solve_everything_default]: 
    cd solve_every_problem/molecule

    cookiecutter ~/git/molecule_template/azure/\{\{cookiecutter.role_name\}\}/molecule/
        role_name [test]: solve_every_problem
        molecule_scenario_name [default]: win
        azure_location [Westeurope]: 
        azure_resource_group [molecule_solve_every_problem_win]: 
    cd ..
    molecule test

## Molecule links
* [Use cookiecutter to create scenario's](https://github.com/rocknsm/molecule-cookiecutter-vsphere)
* [Use cookiecutter to create an Ansible role and configure molecule](https://github.com/retr0h/cookiecutter-molecule)

## Cookiecutter links
* [Commandline options](https://cookiecutter.readthedocs.io/en/1.7.2/usage.html)
* [Choice variables](https://cookiecutter.readthedocs.io/en/latest/advanced/choice_variables.html)
* [Organizing cookiecutters in directories](https://cookiecutter.readthedocs.io/en/1.7.2/advanced/directories.html#organizing-cookiecutters-in-directories-1-7)
* https://github.com/cookiecutter/cookiecutter/issues/723#issuecomment-350561930

