import os
folder = input("Enter folder path: ")
files = os.listdir(folder)
file_count = {}
for file in files:
    if os.path.isfile(os.path.join(folder, file)):
        name, extension = os.path.splitext(file)
        if extension in file_count:
            file_count[extension] += 1
        else:
            file_count[extension] = 1
for ext in file_count:
    print(f"{ext}: {file_count[ext]}")