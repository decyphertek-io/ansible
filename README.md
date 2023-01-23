Install Ansible/Basic Setup
==========================

Ubuntu Install
---------------

    $ sudo apt update
    $ sudo apt install software-properties-common
    $ sudo add-apt-repository --yes --update ppa:ansible/ansible
    $ sudo apt update
    $ sudo apt install ansible
    * <<<OR>>>
    * Fedora Install
    $ sudo dnf update
    $ sudo dnf install ansible
    * Then download bitbucket to /etc/ansible/ - Your link may differ than mine
    $ sudo git clone https://your-repo.git
    * remove the hosts and roles , since they are in the ansible folder
    $ sudo rm -rf hosts
    $ sudo rm -rf roles
    * copy the ansible.cfg from ansible to /etc/ansible
    $ cd ansible/config
    $ sudo cp ansible.cfg /etc/ansible/
    * Add SSH Key
    $ sudo vim ~/.ssh/void.pem
    * Download your collections - https://galaxy.ansible.com/ 
    $ sudo ansible-galaxy collection install paloaltonetworks.panos
    * Need to sudo su
    $ cd /root/.ansible/colections/ansible_collections/palo-alto
    * you may need to install the requirements.txt for some collections or move roles directory to /ansible/roles
    $ sudo -H pip3 install -r requirements.txt

Access the server
-----------------

    $ ssh -i "void.pem" void@0.0.0.0
    * Access 
    $ cd ansible
    * Get Started. README.md in most directories to help
    $ cat README.md
    * To run a playbook you need to be in the right directory
    $ cd ~/ansible/playbook/
    $ ls
    * example
    $ cd aws

Install Ansible on Mac
----------------------

    $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    $ export PATH=$HOME/bin:~/Library/Python/3.8/bin:$PATH
    $ python3 get-pip.py --user
    $ python3 -m pip install --upgrade pip
    $ python3 -m pip install --user ansible
    $ python3 -m pip install --user paramiko
 
Ansible Config/Setup
--------------------

    $ cd ~/ansibe/config/
    $ cp ansible.cfg ~/.ansible.cfg
    $ vim ~/.ansible.cfg
    * change to right paths & directories
    * Make sure to reference the location of the ansible private key
 
AWS Cli Install/Setup
---------------------

     # Linux
     $ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
     $ unzip awscliv2.zip
     # This saves aws creds under root user.
     # Beneficial if you have ansible installed via Linux at /etc/ansible/ 
     $ sudo ./aws/install
     $ sudo aws configure
     # Mac
     $ python3 -m pip install --user awscli
     # Install Ansible AWS Module
     $ sudo ansible-galaxy collection install amazon.aws

     * Example of AWS Config > ~/.aws/config or /root/.aws/config
    [default]
    output = yaml
    region = us-east-1

    [profile account-us-east-1]
    output = yaml
    region = us-east-1

    * Example of AWS Credentials > ~/.aws/credentials or /root/.aws/credentials
    [default]
    aws_access_key_id = add_your_key_here or run aws configure
    aws_secret_access_key = add_your_key_here or run aws configure

    [account-us-east-1]
    role_arn = arn:aws:iam::0000000000000:role/admin
    role_session_name = assumeroleaccountname-us-east-1
    source_profile = default

Collections Examples
----------------------------------------

    * Example1 - Palo Alto
    * Find out where your ansible collections is. 
    $ sudo ansible --version
    $ sudo ansible-galaxy collection install paloaltonetworks.panos
    * Make sure to reference the right collections location
    $ cd /root/.ansible/collections/ansible_collections/paloaltonetworks/panos
    * Install Python requirements
    $ python3 -m pip install -r requirements.txt
    * API Command – Palo Alto >>> Add to vars , only API needed and IP of firewall. ( Minus carrot symbols )
    $ curl -k -X GET 'https://<firewall>/api/?type=keygen&user=<username>&password=<password>'
    * Save the API key, since this will be referenced in ansible-vault.
    
    * Example2 - Zabbix
    $ sudo ansible-galaxy collection install community.zabbix
    $ sudo python3 -m pip install -r /root/.ansible/collections/ansible_collections/community.zabbix/requirements.txt
    
 
Ansible Vault
-------------

    * Easy way , just encrypt the vars file
    $ ansible-vault encrypt variables.vault
    * Choose a password. 
    * Example of a variable.vault
    ip_address: 'iphere'
    api_key: 'apikeyhere'
    * Make sure Playbook references vars
    * Can reference in ansible.cfg if using just one vault.
    vars_files:
    - ~/ansible/vault/variables.vault
    * vars being referenced stored in ansible vault, example
    vars:
    - ip_address: '{{ ip_address }}'
    - api_key: '{{ api_key | default(omit) }}'
    * Need to edit the vault, no probs
    $ ansible-vault edit variables.vault
    * How to decrypt vault and use with a playbook.
    $ ansible-playbook -l windows choco-update.yml --ask-vault-pass

Git Repo
----------

    * Clone your branch of ansible
    * https://your-git
    * Ex: Your branch name will differ
    $ git clone https://your.git
    $ cd ansible
    * EX: Checkout you branch - Yours will be different
    $ git checkout ansible
    $ git status
    $ git add .
    $ git commit -m "Add a comment"
    $ git push
    * The git push command will create a pull request link, visit the link and create the pull request to be approved and merged.
    * Can also setup ssh git instead of using a password , see reference doc below.
    * Can also visualize git changes in desktop gui, if interested.
    $ brew install --cask gitahead

Crontab Automation Examples
----------------------------

    $ sudo apt install install cron
    $ sudo systemctl enable cron
    $ sudo systemctl start cron
    $ sudo systemctl status cron 
    $ crontab -e   
    * Make sure to reference host in playbook
    * Email Server Report
    0 16 * * * /usr/bin/ansible-playbook /etc/ansible/playbooks/health/server-logs.yml | grep -E '=>|failed' > /etc/ansible/reports/server.txt
    30 16 * * * /usr/bin/ansible-playbook /etc/ansible/playbooks/email/server-email.yml

    * Email - Auditd Report
    0 17 * * 5 /usr/bin/ansible-playbook /etc/ansible/playbooks/auditd/aureport.yml | grep -E '=>|Summary Report|======================|Range|Selected|Number' > /etc/ansible/reports/aureport.txt 
    30 17 * * 5 /usr/bin/ansible-playbook /etc/ansible/playbooks/email/aureport-email.yml 

    * Email - Services Report
    0 20 * * 5 /usr/bin/ansible-playbook /etc/ansible/playbooks/services/essential-services.yml | grep -E '=>|falcon:|zabbix:|auditd:|enabled:' > /etc/ansible/reports/services.txt
    30 20 * * 5 /usr/bin/ansible-playbook /etc/ansible/playbooks/email/services-email.yml

    * Email - CVE Scan Report 
    0 18 * * 5 /usr/bin/ansible-playbook /etc/ansible/playbooks/patching/cve-scan.yml | grep -E '=>|CVE*' > /etc/ansible/reports/cvescan.txt
    30 18 * * 5 /usr/bin/ansible-playbook /etc/ansible/playbooks/email/cvescan-email.yml

    * Email Unattended-Upgrades Report
    0 19 * * * /usr/bin/ansible-playbook /etc/ansible/playbooks/patching/apt-log.yml | grep -E '=>|tail|lsb_release|timedatectl|-' > /etc/ansible/reports/unattended-upgrades.yml
    30 19 * * * /usr/bin/ansible-playbook /etc/ansible/playbooks/email/upgrades-email.yml
 
General guidance
----------------

    * AWS Cli Command via playbook
    $ AWS_PROFILE=prod-us-east-1 ansible-playbook -l local aws-gather-info.yaml
    * Run a basic playbook command
    $ ansible-playbook -l test_server playbook.yaml
    * How to use Vault:( See Vault instructions fro more details, will add later. )
    $ ansible-playbook -l test_server playbook.yml --ask-vault-pass 
    * How to use Palo Alto Playbooks
    $ ansible-playbook -l firewall panos_facts.yml --ask-vault-pass
    * How to run Windows Playbooks
    $ ansible-playbook -l win template.yml --ask-vault-pass
    * Modify the ansible.cfg to point to your right directories
    $ vim ~/.ansible.cfg
    * Modify the hosts
    $ vim ~/ansible/inventory/hosts
    * have to setup ~.aws/config & ~.aws/credentials ,Found in creds pass.
    $ aws configure
    * Send email via mailgun
    $ sudo ansible-playbook -l localhost email.yml --ask-vault-pass
 
Ansible Docs
------------

    $ ansible-doc --version
    $ ansible-doc -h
    * Module info:
    $ ansible-doc <module name> >>> Example
    $ ansible-doc copy
    * Plugin info:
    $ ansible-doc –type <plugin type>  >>> Example
    $ ansible-doc -t connection -s ssh
 
References
----------

    https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
    https://docs.ansible.com/ansible/latest/cli/ansible-doc.html
    https://docs.ansible.com/ansible/latest/cli/ansible-vault.html
    https://support.atlassian.com/bitbucket-cloud/docs/set-up-an-ssh-key/
    https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-panorama-api/get-started-with-the-pan-os-xml-api/get-your-api-key.html

