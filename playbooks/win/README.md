#How to run a playbook with Ansible-Vault
$ sudo ansible-playbook -l win test.yml --ask-vault-pass
#This is where it get complicated you will have to use your own ansible-vault vars and reference it in the playbook.
