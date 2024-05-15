#imports for file manipulation
import os
import shutil

# function: put all files into folders by file extension
def sortAllExtensions(folderpath):
    '''
    put all the folder's extensions into a set
    loop through the set of extensions
        sortOneExtension(folderpath, extension)
        print a message saying when smth gets moved
    '''
    pass

# function: put specific files into folders by specific file extension
def sortOneExtension(folderpath, extension, name=''):
    '''
    Move all files of a certain extension into a new subfolder

    Parameters:
        folderpath (str): Path of the folder to search through
        extension (str): The extension to filter out, examples: txt, pdf, py
        name (str): The name of the new subfolder, defaults to the extension being filtered
    
    Return:
        None
    '''
    if name=='': # if name is empty
        name = extension # extension is used as default name
    newLocation = os.path.join(folderpath,name) # location of new folder
    if not os.path.exists(newLocation): # if the folder doesnt exist alr
        os.makedirs(newLocation) # make the folder
    contents = os.listdir(folderpath) # list of folder contents
    for item in contents: # loop through all the contents of the folder
        itemPath = os.path.join(folderpath,item) # current path of the item
        if os.path.isfile(itemPath): # if this is a file
            fileExt = item.split('.')[-1] # get the extension
            if fileExt == extension: # if this is a file we want to filter
                shutil.move(itemPath, os.path.join(newLocation, item)) # move the file 
                print(f"{item} has been moved to {newLocation}") # print statmenent to update changes

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

if __name__=="__main__":
    main()