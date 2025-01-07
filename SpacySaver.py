import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import time
class SpacySaver:
    def __init__(self, root):
        self.root = root
        self.root.title("SpacySaver")
        self.root.geometry("600x400")
        self.root.config(bg="#000000")
        self.backup_folder = ""
        self.source_folder = ""
        self.title_label = tk.Label(self.root, text="SPACYSAVER BACKUP SYSTEM", font=("Courier", 24, "bold"), fg="#00FF00", bg="#000000")
        self.title_label.pack(pady=30)
        self.backup_button = tk.Button(self.root, text="CHOOSE BACKUP FOLDER", font=("Courier", 14, "bold"), command=self.choose_backup_folder, fg="#00FF00", bg="#000000", relief="solid")
        self.backup_button.pack(pady=15)
        self.source_button = tk.Button(self.root, text="CHOOSE SOURCE FOLDER", font=("Courier", 14, "bold"), command=self.choose_source_folder, fg="#00FF00", bg="#000000", relief="solid")
        self.source_button.pack(pady=15)
        self.backup_action_button = tk.Button(self.root, text="START BACKUP", font=("Courier", 14, "bold"), command=self.start_backup, fg="#00FF00", bg="#000000", relief="solid")
        self.backup_action_button.pack(pady=15)
        self.autorun_button = tk.Button(self.root, text="ENABLE AUTORUN", font=("Courier", 14, "bold"), command=self.toggle_autorun, fg="#00FF00", bg="#000000", relief="solid")
        self.autorun_button.pack(pady=15)
        self.autorun_enabled = False
        self.last_backup_time = None
    def choose_backup_folder(self):
        self.backup_folder = filedialog.askdirectory(title="SELECT BACKUP FOLDER")
    def choose_source_folder(self):
        self.source_folder = filedialog.askdirectory(title="SELECT SOURCE FOLDER")
def start_backup(self):
    if not self.backup_folder or not self.source_folder:
        messagebox.showerror("Error", "Please select both source and backup folders.")
        return
    for root_dir, dirs, files in os.walk(self.source_folder):
        dirs[:] = [d for d in dirs if not d.startswith('.')]  
        for file_name in files:
            if file_name.startswith('.'):
                continue
            source_file = os.path.join(root_dir, file_name)
            relative_path = os.path.relpath(source_file, self.source_folder)
            backup_file = os.path.join(self.backup_folder, relative_path)

            backup_dir = os.path.dirname(backup_file)
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            try:
                shutil.copy2(source_file, backup_file)
            except PermissionError:
                print(f"Permission denied: {source_file}. Skipping this file.")
                continue
    messagebox.showinfo("Success", "Backup completed successfully!")
    def toggle_autorun(self):
        self.autorun_enabled = not self.autorun_enabled
        if self.autorun_enabled:
            self.autorun_button.config(text="DISABLE AUTORUN")
            self.auto_backup_check()
        else:
            self.autorun_button.config(text="ENABLE AUTORUN")
    def auto_backup_check(self):
        if self.autorun_enabled:
            current_mod_time = self.get_last_modified_time(self.source_folder)
            if self.last_backup_time is None or current_mod_time > self.last_backup_time:
                self.last_backup_time = current_mod_time
                self.start_backup()
            self.root.after(5000, self.auto_backup_check)
    def get_last_modified_time(self, folder):
        latest_mod_time = 0
        for root_dir, dirs, files in os.walk(folder):
            for file_name in files:
                file_path = os.path.join(root_dir, file_name)
                file_mod_time = os.path.getmtime(file_path)
                latest_mod_time = max(latest_mod_time, file_mod_time)
        return latest_mod_time
if __name__ == "__main__":
    root = tk.Tk()
    app = SpacySaver(root)
    root.mainloop()
