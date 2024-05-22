#imports for file manipulation
import os
import shutil

tab = "    "

# function: put all files into folders by file extension
def sortAllExtensions(folderpath):
    '''
    Sort all files in the folder into subfolders based on their file extensions

    Parameters:
        folderpath (str): Path of the folder to search through

    Return:
        None
    '''
    extensions = {item.split('.')[-1] for item in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath,item))} # set of extensions in the folder
    for extension in extensions: #loop through all the extensions
        sortOneExtension(folderpath, extension) # sort extensions into subfolders

# function: put specific files into folders by specific file extension
def sortOneExtension(folderpath, extension, subfolder=''):
    '''
    Move all files of a certain extension into a new subfolder
    If no files are moved, and the subfolder did not previously exist, the subfolder is deleted

    Parameters:
        folderpath (str): Path of the folder to search through
        extension (str): The extension to filter out, examples: txt, pdf, py
        subfolder (str): The name of the new subfolder, defaults to the extension being filtered
    
    Return:
        None
    '''
    # making the subfolder
    if subfolder=='': # if name is empty
        subfolder = extension # extension is used as default name
    newLocation = os.path.join(folderpath,subfolder) # location of new folder
    exists = os.path.exists(newLocation) # directory was present before
    if exists: # if the folder exists alr
        print(f"{subfolder} exists at {newLocation}")
    else: # if the folder doesnt exist alr
        os.makedirs(newLocation) # make the folder
        print(f"{subfolder} has been created at {newLocation}")
    # go through current folder contents and move them
    moved = False
    contents = os.listdir(folderpath) # list of folder contents
    for item in contents: # loop through all the contents of the folder
        itemPath = os.path.join(folderpath,item) # current path of the item
        if os.path.isfile(itemPath): # if this is a file
            fileExt = item.split('.')[-1] # get the extension
            if fileExt == extension: # if this is a file we want to filter
                shutil.move(itemPath, os.path.join(newLocation, item)) # move the file 
                moved = True # a file has been moved into the subfolder
                print(f"{tab}{item} -> {subfolder}") # print statmenent to update changes
    if not moved and not exists: # check that stuff has been moved
        os.rmdir(newLocation) # remove empty directory
        print(f"{subfolder} has been removed at {newLocation} because no files were moved")

# function: put files into one folder based on certain keyword in name
def sortByKeyword(folderpath, keyword, subfolder=''):
    '''
    Move all files with a certain keyword in the title into a new subfolder
    If no files are moved, and the subfolder did not previously exist, the subfolder is deleted

    Parameters:
        folderpath (str): Path of the folder to search through
        keyword (str): The keyword to filter filenames by
        subfolder (str): The name of the new subfolder, defaults to the keyword being filtered
    
    Return:
        None
    '''
    # making the subfolder
    if subfolder=='': # if name is empty
        subfolder = keyword # keyword is used as default name
    newLocation = os.path.join(folderpath,subfolder) # location of new folder
    exists = os.path.exists(newLocation) # directory was present before
    if exists: # if the folder exists alr
        print(f"{subfolder} exists at {newLocation}")
    else: # if the folder doesnt exist alr
        os.makedirs(newLocation) # make the folder
        print(f"{subfolder} has been created at {newLocation}")
    # go through current folder contents and move them
    moved = False
    contents = os.listdir(folderpath) # list of folder contents
    for item in contents: # loop through all the contents of the folder
        itemPath = os.path.join(folderpath,item) # current path of the item
        if os.path.isfile(itemPath): # if this is a file
            fileName = item[:-len(item.split('.')[-1])-1] # get the filename
            if keyword in fileName: # if this is a file we want to filter
                shutil.move(itemPath, os.path.join(newLocation, item)) # move the file 
                moved = True # a file has been moved into the subfolder
                print(f"{tab}{item} -> {subfolder}") # print statmenent to update changes
    if not moved and not exists: # check that stuff has been moved
        os.rmdir(newLocation) # remove empty directory
        print(f"{subfolder} has been removed at {newLocation} because no files were moved")