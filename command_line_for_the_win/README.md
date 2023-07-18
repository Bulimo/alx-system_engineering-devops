# Command line for the win

## Requirements

	. A README.md file, at the root of the folder of the project
	. Complete the CMD CHALLENGE game
	. Create a screenshot, showing that you completed the required levels
	. Push this screenshot with the right name to GitHub, in either the PNG or JPEG format
	. demonstrate the use of the SFTP (Secure File Transfer Protocol) command-line tool

## Files in the folder

	. 0-first_9_tasks.png - the 1st 9 tasks complete
	. 1-next_9_tasks.png - the next 9 tasks complete, total 18
	. 2-next_9_tasks.png - the next 9 tasks complete, total 27

## Uploading files using SFTP

	. Navigate to the folder where the files to be uploaded are located
	. connect to the sandbox using the command: `sftp remote_username@hostname`
	. Remember to use the provided username and hostname
	. Enter the password when prompted
	. Navigate to the remote directory `/root/alx-system_engineering-devops/`
	. Create the directory command_line_for_the_win using the command `mkdir`
	. upload the files using the command `put filename`
