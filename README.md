# molecule_template
Cookiecutter templates for molecule

## Description

Molecule used to have it's own template system but that was pre version 3. Starting with version 3 external template systems can be used if the scaffolding created by ```molecule init``` is not enough. This repo contains templates to create specialized Molecule scenario's. The [Cookiecutter](https://cookiecutter.readthedocs.io) tool is used to converts the templates in scaffolding ready to be be used for your project.

## Usage
* Create a new Ansible role with the for example the instructions on: https://molecule.readthedocs.io/en/latest/getting-started.html#creating-a-new-role
* Go to the molecule directory and create a new scenario with:

    cookiecutter ~/git/molecule_template/azure/windows

Where '~/git/molecule_template' is the directory where you cloned this repo and azure/windows is the subdirectory with the templates to create Windows VM's in Azure.

Example:

    ansible-galaxy role init solve_every_problem
      - Role solve_every_problem was created successfully
    cd solve_every_problem/
    mkdir molecule; cd molecule
    cookiecutter ~/git/molecule_template/azure/windows
        role_name [test]: solve_every_problem
        molecule_scenario_name [default]: 
        azure_location [Westeurope]: 
        azure_resource_group [molecule_solve_every_problem_default]: 
    cd ..
    molecule test

## Molecule links
* [Use cookiecutter to create scenario's](https://github.com/rocknsm/molecule-cookiecutter-vsphere)
* [Use cookiecutter to create an Ansible role and configure molecule](https://github.com/retr0h/cookiecutter-molecule)

## Cookiecutter links
* [Commandline options](https://cookiecutter.readthedocs.io/en/1.7.2/usage.html)
* [Choice variables](https://cookiecutter.readthedocs.io/en/latest/advanced/choice_variables.html)
* [Organizing cookiecutters in directories](https://cookiecutter.readthedocs.io/en/1.7.2/advanced/directories.html#organizing-cookiecutters-in-directories-1-7)

## ToDo:
Use https://github.com/cookiecutter/cookiecutter/issues/723#issuecomment-350561930 and maybe /home/michielv/git/molecule_test/azure to be able to create a cookiecutter template that creates a role, the molecule directory and one scenario. Both windows and linux directories are copied and a choice variable determines witch directory is not removed in a posthook. The other is renamed to the molecule_scenario_name. The posthook should als delete the cookiecutter.json file in the molecule directory that allows the creation of a new molecule scenario.

Alternative: A posthook script that cd's to the newly created role/molecule directory and starts a new unattended cookiecutter process to create a Molecule scenario .