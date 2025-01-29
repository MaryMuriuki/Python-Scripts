import os
folder_path = r"C:\Users\May\Desktop\Python-scripts\txt files"
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        new_name = filename.replace(".txt", "_new.txt")
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} > {new_name}")