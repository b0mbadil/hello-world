This tool is for brute forcing files and directories in Anonymous FTP servers. 

If an Anonymous FTP server is hosting content, but only allows a user to pull a known file, this tool can help. Anonymous FTP servers respond with certain success/error messages when the user attempts to change directories, which allows directory enumeration.

Frequently Anononymous FTP does not allow a user to list contents while connected, but it will allow a user to check the size of a known file. This "size" command is what FTPBuster utilizes to enumerate file names.

To use this tool you must have your own word list for the file names (and extensions), as well a directory list.
