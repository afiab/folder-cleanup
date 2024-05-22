# Folder Cleanup
Quickly organize your folders

### What does it do?
This is an application that facilitates folder organization. It allows you to choose a folder, and then organize its contents into subfolderrs by file extensions or by a keyword in the title.

Please note: I tested this on a Windows device, so I have no idea if it'll work for other Operating Systems. 

### Why did I make this?
My downloads folder was looking really bad, but I did not want to manually go through each file. I made this application to sort the files for me and make it easier for me to manage my files. I did not just want to write the scripts though, and so I decided to make a GUI for them so that it's easier to understand.

### How it works
As long as functions.py and gui.py are in the same location, you can just run gui.py with python to get started.

In my case, I have the files on my desktop, and I right-click on _gui.py_ and choose _Open with Python 3.xx_

Once you run it, paste the Address of the folder you want to organize, and choose the options that apply. You can sort the folder's files by their extension, or by a certain keyword in their title. All the files that apply will then go into a new subfolder that you choose the name of, unless you are organizing the entire entire folder by file extension and in that case there will be one new subfolder for each extension in the folder.

### Usage Examples
If you want to organize an entire folder by all extensions, it'll look like this:
![image](https://github.com/afiab/folder-cleanup/assets/90729548/0fb5fb5b-928b-4ec7-88e9-656a320f4bb7)
You would first choose to _Sort by extension_, then click on _All Files_.

If you want to only sort one extension, for example only move the text files in a folder, it'll look like this:
![image](https://github.com/afiab/folder-cleanup/assets/90729548/58b60dd5-a9cd-40cc-84a5-1cdd8522421b)
Here you would choose to _Sort by extension_, then _One Extension_, then specify the extension and the name of the new folder

If you want to organize all the files with a certain keyword in their title, here's how that will look:
![image](https://github.com/afiab/folder-cleanup/assets/90729548/0b4f2560-ef15-48d6-b620-c0f95a2019b7)
You choose to _Sort by keyword_, then type the keyword, then the new subfolder name.

### Some more features
- If a folder is created, but no files are moved into the folder, then the folder is automatically removed. However, if the folder existed prior to the folder search, and no files are moved, the folder will not be deleted.
- If no name is provided for the new subfolder when organizing one extension or keyword, the subfolder's name defaults to the extension or keyword being separated.
- The additional pop-up windows automatically close when the operation is complete.
