import tkinter as tk
import customtkinter
from tkinter import filedialog
from tkinter import ttk


root = customtkinter.CTk()

root.geometry("800x600")
root.title("Doc writer")

## Test5
def highlight_syntax(event=None):
    '''Highlight lines starting with #.'''
    text.tag_remove('highlight', '1.0', tk.END)  # Remove existing tags
    lines = text.get('1.0', 'end-1c').split('\n')
    for i, line in enumerate(lines, 1):
        if line.startswith('#'):
            index = f"{i}.0"
            text.tag_add('highlight', index, f"{index} lineend")

def save_text():
    """Save the content of the text widget to a file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", tk.END))

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

main_frame = customtkinter.CTkFrame(master=root)
main_frame.pack(pady=10, padx=10, fill="both", expand=True)

frame_1 = customtkinter.CTkFrame(master=main_frame, width=150)
frame_1.pack(side="left", fill="x", expand=False)
frame_1.pack_propagate(False)
#label = customtkinter.CTkLabel(master=frame_1,text="Treeview")
#label.grid(pady=10)

###Treeview Customisation (theme colors are selected)
bg_color = root._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
text_color = root._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkLabel"]["text_color"])
selected_color = root._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["fg_color"])

#root.grid_columnconfigure(0, weight=1)
#root.grid_rowconfigure(0, weight=1)

treestyle = ttk.Style()
treestyle.theme_use('default')
treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)
treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
root.bind("<<TreeviewSelect>>", lambda event: root.focus_set())

##Treeview widget data
treeview = ttk.Treeview(frame_1, height=16, show="tree")
treeview.grid(padx=0)
treeview.insert('', '0', 'i1', text ='Python')
treeview.insert('', '1', 'i2', text ='Customtkinter')
treeview.insert('', '2', 'i3', text ='Tkinter')
treeview.insert('i2', 'end', 'Frame', text ='Frame')
treeview.insert('i2', 'end', 'Label', text ='Label')
treeview.insert('i3', 'end', 'Treeview', text ='Treeview')
treeview.insert('i3', 'end', 'Treeview2', text ='Treeview2')
treeview.move('i2', 'i1', 'end')
treeview.move('i3', 'i1', 'end')
treeview.pack(padx=10, pady=10, fill="y", side='left', anchor='nw', expand=False)
# Add a scrollbar
#scrollbar = ttk.Scrollbar(frame_1, orient='vertical', command=tree.yview)
#tree.configure(yscroll=scrollbar.set)
#scrollbar.pack(side='right', fill='y')

# Configure the grid
#root.grid_columnconfigure(0, weight=1)
#root.grid_rowconfigure(0, weight=1)

text_frame = customtkinter.CTkFrame(master=main_frame)
#text_frame.pack(side="left", fill="both", expand=True)

#text_frame = ttk.Frame(root)
text = tk.Text(main_frame, bg='#1E1E1E', fg='white', padx=10, pady=10, insertbackground='white')
text.pack(side=tk.LEFT, expand=True, fill='both')
#text.grid(sticky='nsew', padx=20, pady=20)

# Define the tag for highlighting
text.tag_configure('highlight', foreground='green')

# Bind the Text widget to the key-release event
text.bind('<KeyRelease>', highlight_syntax)

#save_button = tk.Button(root, text="Save", command=save_text)
#save_button.pack()
#save_button.place(relx = 0.5, rely = 0.5)



root.mainloop()
