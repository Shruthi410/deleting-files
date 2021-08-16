# deleting-files

## Files handling

### Comments to add in the files that need to be changed:

1. “Delete_this_file”- To delete the entire file
2. “Delete_this_line”- To delete the particular line
3. “Delete_from” and “delete_to”- To delete the block of code that has been written in between “delete_from” and “delete_to”.

### Delete a File

The python code checks if the comment exists in the directory tree. If yes, then deletes the file from the project. 

You need to write the “delete_this_file” comment in the file that needs to be deleted. 

Example:
// delete_this_file


### Delete a line or multiple lines

The python code checks if the comment exists in the directory tree. If yes, then deletes the line from the file and writes the line number of the code that got deleted in a separate file called “changes.txt.”

You need to write the “delete_this_line” comment in the file that needs to be deleted. 

Example:
// delete_this_line

 
### Delete a block of code:

The python code checks if the comment “delete_from” and “delete_to” exists in the directory tree. If yes, then deletes the block of code from the file and writes the line numbers of the code that got deleted in a separate file called “changes.txt.”

You need to write the “delete_from” comment at the beginning of the block of code and the “delete_to” comment at the end of the block of code that needs to be deleted in the file. 

#### Example:

// delete_from
sfeg
ewgg
wgwg
gg
rrgeh
// delete_to
