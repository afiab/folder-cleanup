import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
import os
from functions import sortAllExtensions, sortByKeyword, sortOneExtension

def sort_files():
    folderpath = entry_path.get()  # get folder path from entry widget
    # folder path exists
    if not os.path.exists(folderpath): # folderpath does not exist
        messagebox.showerror("Error", "Folder path does not exist.")
        return
    choice = var.get() # choose how to sort
    if choice == 1:  # by extension
        sort_window = tk.Toplevel(root)
        sort_window.title("Sort by Extension")
        label = tk.Label(sort_window, text="Do you want to sort all files or one extension?")
        label.pack()
        # sort all the files button
        all_files_button = tk.Button(sort_window, text="All Files", command=lambda: sortAllExtensions(folderpath))
        all_files_button.pack(side=BOTTOM,anchor=CENTER)
        # sort only one file button
        one_extension_button = tk.Button(sort_window, text="One Extension", command=lambda: sort_one_extension(folderpath))
        one_extension_button.pack(side=BOTTOM,anchor=CENTER)
    elif choice == 2:  # by keyword
        keyword = simpledialog.askstring("Keyword", "Enter the keyword to filter filenames by:")
        if keyword:
            new_subfolder_name = simpledialog.askstring("New Subfolder Name", "Enter the name for the new subfolder:")
            sortByKeyword(folderpath, keyword, new_subfolder_name)

# function to get parameters for one extension sort
def sort_one_extension(folderpath):
    extension = simpledialog.askstring("File Extension", "Enter the file extension to sort:")
    if extension:
        new_folder_name = simpledialog.askstring("New Folder Name", "Enter the name for the new folder:")
        if new_folder_name:
            sortOneExtension(folderpath, extension, new_folder_name)

# make window
root = tk.Tk()
root.title("File Sorter")

# label + entry for file path
label_path = tk.Label(root, text="Enter folder path:")
label_path.pack()
entry_path = tk.Entry(root)
entry_path.pack()

# radio buttons for sorting choice
var = tk.IntVar()
var.set(1)  # Default choice is to sort by extension
radio_extension = tk.Radiobutton(root, text="Sort by extension", variable=var, value=1)
radio_extension.pack()
radio_keyword = tk.Radiobutton(root, text="Sort by keyword", variable=var, value=2)
radio_keyword.pack()

# button to start sorting
button_sort = tk.Button(root, text="Sort Files", command=sort_files)
button_sort.pack()

root.mainloop()


