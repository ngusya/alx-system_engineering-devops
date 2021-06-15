Shell Redirections Scripts
==========================

 * printf "%s\n" "hello world"   >>     Prints "Hello, World" followed by a new line to the standard output.

 * echo "\"(Ôo)'"                >>     Displays a confused smiley ["(Ôo)']

 * cat /etc/passwd               >>     Displays the content of the /etc/passwd file.

 * cat /etc/passwd /etc/hosts    >>     Displays the content of /etc/passwd and /etc/hosts.

 * tail -n 10 /etc/passwd        >>     Displays the last 10 lines of the /etc/passwd file.

 * head -n 10 /etc/passwd        >>     Displays the first 10 lines of the /etc/passwd file.

 * cat iacta | head -3 | tail -1            >>     Displays the third line of the file iacta.

 * touch \*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:) echo "Holberton School\n"    >>     Creates a file named \*\\'"Holberton School"\'\\$\?\*\*\*\*\*:)

 * ls -la > ls_cwd_content        >>    Writes into the file ls_cwd_content the result of the command ls -al.

 * find . -name "*.js" type f -delete >>  Deletes all the regular files with a .js extension that are present in the current directory and all its subfolders.

 * find . -mindepth 1 -type d | wc -l >>  Counts the number of directories and subdirectories in the current directory.

 * find . -type f -printf '%f\n' | ls -t | head -n 10    >>  Displays the 10 newest files in the current directory.

 * sort | unique -u    >>    Takes a list of words as input and prints only words that appear exactly once.

 * cat /etc/passwd | grep -i "root"    >>    Displays lines containing the pattern "root" from the file /etc/passwd.

 * cat /etc/passwd | grep -i "bin" | wc -l    >>    Displays the number that contains the pattern "bin" in the file /etc/passwd

 * cat /etc/passwd | grep -i "root" -A 3    >>    Displays lines containing the pattern "root" and 3 lines after them in the file /etc/passwd

 * cat /etc/passwd |grep -v "bin"    >>    Displays all the lines in the file /etc/passw that do not contain the pattern "bin"

 * cat etc/ssh/sshd_config | grep -i '^[[:alpha:]]'    >>    Displays all lines of the file /etc/ssh/ssh_config starting with a letter. (Including capital letters as well)

 * tr AZ |tr c e    >>    Replaces all characters A and c from input to Z and e respectively

 * tr -d 'cC'    >>    Removes all lettes c and C from input

 * rev    >>    Reverses its input

 * cut -d : -f 1,6 /etc/passwd | sort -k1    >>    Displays all users and their home directories, sorted by users based on the /etc/passwd file