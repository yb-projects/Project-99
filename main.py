# PRO C99 - Project - Super Files
# Not enough information was provided, so I took help from the internet and the Python documentation.
import customtkinter # Installed this package from PIP
import os, time, shutil

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x400")
app.title("Super Files 📁")

heading = customtkinter.CTkLabel(app, text="Super Files 📁", fg_color="transparent", font=("Arial", 32))

path = ""
days = 30
days_in_seconds = time.time() - (days * 24 * 60 * 60) # Learnt this from the internet
"""
time.time() gives the seconds elapsed since 1970 which was the year when time was invented in Computers.
Days = 30
Hours in a day = 24
Hour = 60 min
Minutes = 60 sec

So, 30 days = (seconds elapsed since 1970) - {30 * 24 * 60 * 60 (used calculator)} = 2592000
"""

print(days)

def remove_folder(path):
	if not shutil.rmtree(path): # Learnt this from the internet
		print("Removed")
	else:
		print("Cannot remove")



def remove_file(path):
	if not os.remove(path): # Learnt this from the internet
		print("Removed")
	else:
		print("Cannot remove")


def time(path):
	ctime = os.stat(path).st_ctime # Got this from hints
	return ctime # Got this from hints

def delete_files(path):
    if(os.path.exists(path)): # Checking whether path exists.
        for root_folder, folders, files in os.walk(path): # Got this from Python documentation and the internet
            if days_in_seconds >= time(root_folder):
                remove_folder(root_folder)
                break
            else: # Learnt this from the internet
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)
                    if days_in_seconds >= time(folder_path):
                        remove_folder(folder_path)
                
                for file1 in files:
                    file_path = os.path.join(root_folder, file1)
                    if days_in_seconds >= time(file_path):
                        remove_file(file_path)
                    else:
                        if days_in_seconds >= time(path):
                            remove_file(path)
    else:
        print("The path is not found. Please try again.")


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)
    if (choice == "Create a new file ➕"):
        toplevel = customtkinter.CTkToplevel(app) 
        toplevel.geometry("400x400")
        toplevel.title("Create a new file ➕")

        heading = customtkinter.CTkLabel(toplevel, text="Create a new file ➕", fg_color="transparent", font=("Arial", 32))
        heading.pack(padx=20, pady=20)

        file_name = customtkinter.CTkEntry(toplevel, placeholder_text="Enter the file name including path", width=255, height=50, font=("Arial", 16))
        
        file_name.pack(padx=30, pady=30)

        button = customtkinter.CTkButton(toplevel, text="Create File", command=lambda entry=file_name: open(entry.get(), "x"), width=200, height=50, font=("Arial", 21))

        button.pack(padx=32, pady=32)

        toplevel.mainloop()
    
    elif (choice == "Delete all files from last 30 days 🗑️"):
        toplevel = customtkinter.CTkToplevel(app) 
        toplevel.geometry("400x400")
        toplevel.title("Delete all files from last 30 days 🗑️")

        heading = customtkinter.CTkLabel(toplevel, text="Delete all files from last 30 days 🗑️", fg_color="transparent", font=("Arial", 18))
        heading.pack(padx=20, pady=20)

        path_entry = customtkinter.CTkEntry(toplevel, placeholder_text="Enter the path", width=255, height=50, font=("Arial", 16))
        
        path_entry.pack(padx=30, pady=30)

        button = customtkinter.CTkButton(toplevel, text="Delete Files", command=lambda entry=path_entry: delete_files(entry.get()), width=200, height=50, font=("Arial", 21))

        button.pack(padx=32, pady=32)

        toplevel.mainloop()



optionmenu = customtkinter.CTkOptionMenu(app, values=["Select an option: ", "Create a new file ➕", "Delete all files from last 30 days 🗑️"],
                                         command=optionmenu_callback)
heading.pack(padx=20, pady=20)
optionmenu.pack(padx=70, pady=70)
app.mainloop()