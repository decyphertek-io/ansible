#Save variables in namehere.vault , then encrypt.
$ sudo ansible-vault encrypt variables.vault
#Make a secure password, reference it in the playbook.
#How to edit the vault
$ sudo ansible-vault edit variables.vault
