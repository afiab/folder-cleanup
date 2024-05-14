#imports for file manipulation
import os
import shutil

# function: put all files into folders by file extension
def sortAllExtensions(folderpath):
    '''
    put all the folder's extensions into a set
    loop through the set of extensions
        sortOneExtension(folderpath, extension)
    '''
    pass

# function: put specific files into folders by specific file extension
def sortOneExtension(folderpath, extension, name=''):
    '''
    create a folder for this extension called name
        if name is empty, use extension as the name
    loop through the folderpath's contents
        move all the files for that extension into the folder
    '''
    pass

# function: put files into one folder based on certain keyword in name
def sortByKeyword(folderpath, keyword, newName=''):
    '''
    create a new folder called newName
        if newName is empty, the folder should be called keyword
    loop through the contents of folderpath
        
    '''
    pass