###Install Ansible/Basic Setup###
# Ubuntu Install
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo add-apt-repository --yes --update ppa:ansible/ansible
$ sudo apt update
$ sudo apt install ansible
# <<<OR>>>
# Fedora Install
$ sudo dnf update
$ sudo dnf install ansible
# Then download bitbucket to /etc/ansible/ - Your link may differ than mine
$ sudo git clone https://your-repo.git
# remove the hosts and roles , since they are in the ansible folder
$ sudo rm -rf hosts
$ sudo rm -rf roles
# copy the ansible.cfg from ansible to /etc/ansible
$ cd ansible/config
$ sudo cp ansible.cfg /etc/ansible/
# Add SSH Key
$ sudo vim ~/.ssh/void.pem
# Download your collections - https://galaxy.ansible.com/ 
$ sudo ansible-galaxy collection install paloaltonetworks.panos
# Need to sudo su
$ cd /root/.ansible/colections/ansible_collections/palo-alto
# you may need to install the requirements.txt for some collections or move roles directory to /ansible/roles
$ sudo -H pip3 install -r requirements.txt

###Access the server###
$ ssh -i "void.pem" void@0.0.0.0
# Access 
$ cd ansible
# Get Started. README.md in most directories to help
$ cat README.md
# To run a playbook you need to be in the right directory
$ cd ~/ansible/playbook/
$ ls
# example
$ cd aws


###Install Ansible on Mac###
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ export PATH=$HOME/bin:~/Library/Python/3.8/bin:$PATH
$ python3 get-pip.py --user
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --user ansible
$ python3 -m pip install --user paramiko
 
###Ansible Config/Setup###
$ cd ~/ansibe/config/
$ cp ansible.cfg ~/.ansible.cfg
$ vim ~/.ansible.cfg
# change to right paths & directories
# Make sure to reference the location of the ansible private key
 
###AWS Cli Install/Setup###
$ pip3 install awscli --upgrade --user
$ aws configure
# add ansible keys, found in Las Pass
# Stored here: ~/.aws
# update config and credentials from ansible
 
###Collections Setup Palo Alto Example###
$ ansible-galaxy collection install paloaltonetworks.panos
$ cd ~/.ansible/collections/ansible_collections/paloaltonetworks/panos
# Install Python requirements
$ python3 -m pip install -r requirements.txt
# API Command – Palo Alto >>> Add to vars , only API needed and IP of firewall. ( Minus carrot symbols )
$ curl -k -X GET 'https://<firewall>/api/?type=keygen&user=<username>&password=<password>'
# Save the API key, since this will be referenced in ansible-vault.
 
###Ansible Vault###
# Easy way , just encrypt the vars file
$ ansible-vault encrypt variables.vault
# Choose a password. 
# Example of a variable.vault
ip_address: 'iphere'
api_key: 'apikeyhere'
# Make sure Playbook references vars
# Can reference in ansible.cfg if using just one vault.
vars_files:
  - ~/ansible/vault/variables.vault
# vars being referenced stored in ansible vault, example
vars:
  - ip_address: '{{ ip_address }}'
  - api_key: '{{ api_key | default(omit) }}'
# Need to edit the vault, no probs
$ ansible-vault edit variables.vault
# How to decrypt vault and use with a playbook.
$ ansible-playbook -l firewall panos_facts.yml --ask-vault-pass
  
###Bitbucket###
# Clone your branch of ansible
# https://your-git
# Ex: Your branch name will differ
$ git clone https://your.git
$ cd ansible
# EX: Checkout you branch - Yours will be different
$ git checkout ansible
$ git status
$ git add .
$ git commit -m "Add a comment"
$ git push
# The git push command will create a pull request link, visit the link and create the pull request to be approved and merged.
# Can also setup ssh git instead of using a password , see reference doc below.
# Can also visualize git changes in desktop gui, if interested.
$ brew install --cask gitahead
 
###General guidance###
# AWS Cli Command via playbook
$ AWS_PROFILE=prod-us-east-1 ansible-playbook -l local aws-gather-info.yaml
# Run a basic playbook command
$ ansible-playbook -l test_server playbook.yaml
# How to use Vault:( See Vault instructions fro more details, will add later. )
$ ansible-playbook -l test_server playbook.yml --ask-vault-pass 
# How to use Palo Alto Playbooks
$ ansible-playbook -l firewall panos_facts.yml --ask-vault-pass
# How to run Windows Playbooks
$ ansible-playbook -l win template.yml --ask-vault-pass
# Modify the ansible.cfg to point to your right directories
$ vim ~/.ansible.cfg
# Modify the hosts
$ vim ~/ansible/inventory/hosts
# have to setup ~.aws/config & ~.aws/credentials ,Found in creds pass.
$ aws configure
 
###Ansible Docs###
$ ansible-doc --version
$ ansible-doc -h
# Module info:
$ ansible-doc <module name> >>> Example
$ ansible-doc copy
# Plugin info:
$ ansible-doc –type <plugin type>  >>> Example
$ ansible-doc -t connection -s ssh
 
###References###
https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
https://docs.ansible.com/ansible/latest/cli/ansible-doc.html
https://docs.ansible.com/ansible/latest/cli/ansible-vault.html
https://support.atlassian.com/bitbucket-cloud/docs/set-up-an-ssh-key/
https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-panorama-api/get-started-with-the-pan-os-xml-api/get-your-api-key.html
