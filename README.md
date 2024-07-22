# Folder Cleanup
Quickly organize your folders

### What does it do?
This is an application that facilitates folder organization. It allows you to choose a folder, and then organize its contents into subfolderrs by file extensions or by a keyword in the title.

Please note: This was tested on Windows 

### Why did I make this?
My downloads folder was looking really bad, but I did not want to manually go through each file. I made this application to sort the files for me and make it easier for me to manage my files. I did not just want to write the scripts though, and so I decided to make a GUI for them so that it's easier to understand.

### How to use it
As long as functions.py and gui.py are in the same location, you can just run gui.py with python to get started.

In my case, I have the files on my desktop, and I right-click on _gui.py_ and choose _Open with Python 3.xx_

When you first run it, it'll look like this:
![image](https://github.com/user-attachments/assets/50d5c58b-65c1-417c-bf84-b0512cff6b30)

You will then choose the folder you want to organize by typing the path in the text input field or clicking **Browse** to open your file explorer and choose from there.
Then choose whether you want the folder's contents sorted by their extension or filter a certain keyword. All the files that apply will then go into a new subfolder that you choose the name of, unless you are organizing the entire entire folder by file extension and in that case there will be one new subfolder for each extension in the folder.

### Usage Examples
If you want to organize an entire folder by all extensions, it'll look like this:
![image](https://github.com/user-attachments/assets/8e4074c7-3ab5-406b-a53b-08b4446fd0c1)
You would first choose to _Sort by extension_, then click on _All Files_. 

If you instead want to only sort one extension, for example only move the text files in a folder, it'll look like this:
![image](https://github.com/user-attachments/assets/ec381df2-db36-4701-a1e2-d1ad82fe1d18)
Here you would choose to _Sort by extension_, then _One Extension_, then specify the extension and the name of the new folder. 

If you want to organize all the files with a certain keyword in their title, here's how that will look:
![image](https://github.com/user-attachments/assets/502286ff-dcd1-44a2-8826-97dabc5dd025)
You choose to _Sort by keyword_, then type the keyword, then the new subfolder name.

For all of these options, The changed files and folders are logged in the _Change Log_ at the bottom of the window. You can also scroll and resize the Change Log to view previous changes.

### Some more features
- If a folder is created, but no files are moved into the folder, then the folder is automatically removed. However, if the folder existed prior to the folder search, and no files are moved, the folder will not be deleted.
- If no name is provided for the new subfolder when organizing one extension or keyword, the subfolder's name defaults to the extension or keyword being separated.

### How did I make this?
I used the os and shutil libraries for the file management, and tkinter for the GUI. All of these are python libraries
