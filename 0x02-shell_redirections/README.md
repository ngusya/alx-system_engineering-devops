Shell Redirections Scripts
==========================

 * printf "%s\n" "hello world"   >>     Prints "Hello, World" followed by a new line to the standard output.

 * echo "\"(Ôo)'"                >>     Displays a confused smiley ["(Ôo)']

 * cat /etc/passwd               >>     Displays the content of the /etc/passwd file.

 * cat /etc/passwd /etc/hosts    >>     Displays the content of /etc/passwd and /etc/hosts.

 * tail -n 10 /etc/passwd        >>     Displays the last 10 lines of the /etc/passwd file.

 * head -n 10 /etc/passwd        >>     Displays the first 10 lines of the /etc/passwd file.

 * awk "NR==3" iacta             >>     Displays the third line of the file iacta.

 * touch \*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:) echo "Holberton School\n"    >>     Creates a file named \*\\'"Holberton School"\'\\$\?\*\*\*\*\*:)

 *ls -al > ls_cwd_content        >>    Writes into the file ls_cwd_content the result of the command ls -al.