**0x01. Shell, Permissions**
============================

_Shell Permission Scripts_

  * su betty          Switches the current user to the user betty\

  * id -un, --name    Prints the effective username of the current user\
  * id -gn            Prints all the groups the current user is part of\
  
  * sudo chown betty hello  Changes the owner of the file hello to the user betty\
  
  * touch hello       Creates an empty file called hello\
  * chmod 744 hello   Adds executive permission to the owner of the file hello\
  * chmod 754 hello   Adds executive permission to the owner and the group owner\ and read permission to other users to the file hello\