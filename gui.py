import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from functions import sortAllExtensions, sortOneExtension, sortByKeyword
import sys

class RedirectText(object):
    '''
    Helps console print statements appear at bottom of GUI
    '''
    def __init__(self, text_widget, container):
        self.output = text_widget
        self.container = container
        self.is_visible = False

    def write(self, string):
        if not self.is_visible:
            self.container.pack(fill=tk.BOTH, expand=True)
            self.is_visible = True
        self.output.config(state=tk.NORMAL)  # Enable the text widget to insert text
        self.output.insert(tk.END, string)
        self.output.config(state=tk.DISABLED)  # Disable the text widget to make it read-only
        self.output.see(tk.END)  # Scroll to the end

    def flush(self):
        pass  # This is needed for Python's `sys.stdout`

def sort_files():
    '''
    Choose a folder to sort files in, then
    Determine how the user wants to sort files so that 
    the corresponding function can be called
    Option 1: sort by extension, then determines one specific extension or all
    Option 2: sort by keyword

    Parameters:
        None

    Return:
        None
    '''
    folderpath = entry_path.get()
    if not folderpath:
        messagebox.showerror("Error", "No folder selected!")
        return
    choice = var.get()
    if choice == 1:  # by extension
        show_sort_extension_options()
    elif choice == 2:  # by keyword
        show_sort_keyword_options()

def show_sort_extension_options():
    '''
    Displays extension sorting options onto GUI if user chose to sort by extension

    Parameters:
        None

    Return:
        None
    '''
    clear_frame(options_frame)
    all_files_button = tk.Button(options_frame, text="Sort All Extensions", command=lambda: sortAllExtensions(entry_path.get()))
    all_files_button.pack(side=tk.TOP, anchor=tk.CENTER)
    one_extension_button = tk.Button(options_frame, text="Sort One Extension", command=lambda: sort_one_extension(entry_path.get()))
    one_extension_button.pack(side=tk.TOP, anchor=tk.CENTER)

def show_sort_keyword_options():
    '''
    Displays keyword sorting fields onto GUI if user chose to sort by keyword

    Parameters:
        None

    Return:
        None
    '''
    clear_frame(options_frame)
    keyword_label = tk.Label(options_frame, text="Enter Keyword:")
    keyword_label.pack(side=tk.TOP, anchor=tk.CENTER)
    keyword_entry = tk.Entry(options_frame)
    keyword_entry.pack(side=tk.TOP, anchor=tk.CENTER)
    subfolder_label = tk.Label(options_frame, text="New Subfolder Name:")
    subfolder_label.pack(side=tk.TOP, anchor=tk.CENTER)
    subfolder_entry = tk.Entry(options_frame)
    subfolder_entry.pack(side=tk.TOP, anchor=tk.CENTER)
    sort_button = tk.Button(options_frame, text="Sort", command=lambda: sortByKeyword(entry_path.get(), keyword_entry.get(), subfolder_entry.get()))
    sort_button.pack(side=tk.TOP, anchor=tk.CENTER)

def sort_one_extension(folderpath):
    '''
    Function for the scenario where a user wants to sort by one extension
    Main purpose is to gather the necessary parameters to call the sortOneExtension function
    
    Parameters:
        folderpath (str): Path of the folder to search through
    
    Return:
        None
    '''
    extension = simpledialog.askstring("File Extension", "Enter the file extension to sort:")
    if extension:
        new_folder_name = simpledialog.askstring("New Folder Name", "Enter the name for the new folder:")
        sortOneExtension(folderpath, extension, new_folder_name)

def select_folder():
    '''
    Allows user to select a folder from their file explorer

    Parameters:
        None

    Return:
        None
    '''
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, folder_selected)

def clear_frame(frame):
    '''
    Clears the frame of options from a previous sorting choice

    Parameters:
        frame (tkinter frame widget): the frame to be cleared
        
    Return:
        None
    '''
    for widget in frame.winfo_children():
        widget.destroy()

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
button_sort = tk.Button(root, text="Next", command=sort_files)
button_sort.pack()

# frame for additional options
options_frame = tk.Frame(root)
options_frame.pack(fill=tk.BOTH, expand=True)

# frame for log output
log_frame = tk.Frame(root)

# label logging area
log_label = tk.Label(log_frame, text="Change Log:")
log_label.pack()

# text widget for log output
scrollbar = tk.Scrollbar(log_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
log_text = tk.Text(log_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, height=10, width=40, state=tk.DISABLED)  # Adjust height and width
log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=log_text.yview)

# redirect stdout
sys.stdout = RedirectText(log_text, log_frame)

root.mainloop()
