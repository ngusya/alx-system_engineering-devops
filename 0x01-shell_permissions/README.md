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

  * chmod ugo+x hello Adds execution permission to the owner, the group owner and other users to the file hello\
  
  * chmod 007 hello   Sets the permission to the file hello as follows (Owner: no permission at all , Group owner: no perm                        ission at all, Other users:all permissions)\
  
  * chmod 753 hello   Sets the mode of the hello file to (-rwxr-x-wx)

  * chmod --reference = olleh hello   Sets the mode of the file hello the same as olleh mode\
  
  * find ./ -type d -exec chmod ugo+x {}+      Adds executive permission to all subdirectories\ of the current directory for                                               the owner, the group owner and all other users.\