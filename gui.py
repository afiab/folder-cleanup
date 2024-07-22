import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from functions import sortAllExtensions, sortOneExtension, sortByKeyword

def sort_files():
    folderpath = entry_path.get()
    if not folderpath:
        messagebox.showerror("Error", "No folder selected!")
        return
    choice = var.get()
    if choice == 1:  # by extension
        sort_window = tk.Toplevel(root)
        sort_window.title("Sort by Extension")
        # sort all files button
        all_files_button = tk.Button(sort_window, text="All Files", command=lambda: sortAllExtensions(folderpath))
        all_files_button.pack(side=tk.BOTTOM, anchor=tk.CENTER)
        # sort only one file button
        one_extension_button = tk.Button(sort_window, text="One Extension", command=lambda: sort_one_extension(folderpath))
        one_extension_button.pack(side=tk.BOTTOM, anchor=tk.CENTER)
    elif choice == 2:  # by keyword
        keyword = simpledialog.askstring("Keyword", "Enter the keyword to filter filenames by:")
        if keyword:
            new_subfolder_name = simpledialog.askstring("New Subfolder Name", "Enter the name for the new subfolder:")
            sortByKeyword(folderpath, keyword, new_subfolder_name)

def sort_one_extension(folderpath):
    extension = simpledialog.askstring("File Extension", "Enter the file extension to sort:")
    if extension:
        new_folder_name = simpledialog.askstring("New Folder Name", "Enter the name for the new folder:")
        sortOneExtension(folderpath, extension, new_folder_name)

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, folder_selected)

# make window
root = tk.Tk()
root.title("File Sorter")

# label + entry for file path
label_path = tk.Label(root, text="Select folder path:")
label_path.pack()
entry_path = tk.Entry(root, width=50)
entry_path.pack()
button_browse = tk.Button(root, text="Browse", command=select_folder)
button_browse.pack()

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
