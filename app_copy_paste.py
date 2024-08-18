
#test for git
import customtkinter as ctk
import tkinter as tk
import shutil
import os


class FileCopier:


    def __init__(self,source,destination):
        self.source = source
        self.destination = destination

    
    def copy_file(self):

        if os.path.isfile(self.source):
            try:
                shutil.copy(self.source,self.destination)
                return True, "File Copied Successfully"
            except Exception as e:
                return False, f"Error: {e}"
        
        else:
            return False,"Source File Does not Exist"
        


class FileCopierApp:
    def __init__(self,root):
        self.root = root
        self.root.title("File Copier")
        self.root.geometry('600x500')


        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")


        self.source_label = ctk.CTkLabel(root, text= "Copy file from")
        self.source_label.pack(pady=10)
        self.souce_entry = ctk.CTkEntry(root, width = 400)
        self.souce_entry.pack(pady=10)


        self.destination_label = ctk.CTkLabel(root, text = "Input the destination")
        self.destination_label.pack(pady=10)
        self.destination_entry = ctk.CTkEntry(root, width = 400)
        self.destination_entry.pack(pady = 10)

        self.copy_button = ctk.CTkButton(root, text= "COPY", command = self.copy_file)
        self.copy_button.pack(pady=20)

        self.status_label = ctk.CTkLabel(root, text = '')
        self.status_label.pack(pady=10)

    def copy_file(self):

        source = self.souce_entry.get()
        destination = self.destination_entry.get()

        if not source or not destination:

            tk.messagebox.showerror("ERROR","Both Source and Destination are required")
            return
        

        file_copier = FileCopier(source,destination)
        success,message = file_copier.copy_file()


        if success:
            self.status_label.configure(text=message, text_color = 'green')
        else:
            self.status_label.configure(text = message, text_color = 'red')



if __name__ == '__main__':

    root = ctk.CTk()
    app = FileCopierApp(root)
    root.mainloop()

