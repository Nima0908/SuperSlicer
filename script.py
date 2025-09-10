import os
import shutil

# Set the target directory
backup_dir = "backups"

# Create the backups folder if it doesn't exist
os.makedirs(backup_dir, exist_ok=True)

# Walk through the current directory and subdirectories
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".bak"):
            # Full path to the file
            file_path = os.path.join(root, file)
            # Destination path
            dest_path = os.path.join(backup_dir, file)
            
            # Move the file
            shutil.move(file_path, dest_path)
            print(f"Moved: {file_path} -> {dest_path}")

print("All .bak files have been moved to the 'backups' folder.")
