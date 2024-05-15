#imports for file manipulation
import os
import shutil

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
def sortOneExtension(folderpath, extension, name=''):
    '''
    Move all files of a certain extension into a new subfolder
    If no files are moved, and the subfolder did not previously exist, the subfolder is deleted

    Parameters:
        folderpath (str): Path of the folder to search through
        extension (str): The extension to filter out, examples: txt, pdf, py
        name (str): The name of the new subfolder, defaults to the extension being filtered
    
    Return:
        None
    '''
    # making the subfolder
    if name=='': # if name is empty
        name = extension # extension is used as default name
    newLocation = os.path.join(folderpath,name) # location of new folder
    exists = os.path.exists(newLocation) # directory was present before
    if exists: # if the folder exists alr
        print(f"{name} exists at {newLocation}")
    else: # if the folder doesnt exist alr
        os.makedirs(newLocation) # make the folder
        print(f"{name} has been created at {newLocation}")
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
                print(f"    {item} -> {name}") # print statmenent to update changes
    # check that stuff has been moved
    if not moved and not exists:
        os.rmdir(newLocation) # remove empty directory
        print(f"{name} has been removed at {newLocation} because no files were moved")

# function: put files into one folder based on certain keyword in name
def sortByKeyword(folderpath, keyword, newName=''):
    '''
    create a new folder called newName
        if newName is empty, the folder should be called keyword
    loop through the contents of folderpath
        
    '''
    pass

def main():
    folderpath = input("Enter the path of the folder you want to clean: ")
    '''test one extension'''
    # sortOneExtension(folderpath, "txt","textfiles")
    # sortOneExtension(folderpath, "txt")
    # sortAllExtensions(folderpath)

if __name__=="__main__":
    main()