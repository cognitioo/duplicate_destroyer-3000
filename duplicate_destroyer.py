import os
from collections import Counter

print("Note- if the file have security allowed then the \n" \
        " python request to check inside the file will be denied\n" \
        " so before pasteing the path make sure that the *the spesific\n" \
        " area's permission is denied* it doesn't harm anything after\n " \
        "changing you can turn on this thing easily👍 ")

file_path = input("Enter the file path: ").strip()


# Try listing if it's a folder
if os.path.isdir(file_path):
    try:
        contents = os.listdir(file_path)
        print("📂 Folder contents:", contents)
    except PermissionError:
        print("❌ Permission denied while listing the folder!")

my_list = contents

counts = Counter(my_list)
duplicates = [item for item,count in counts.items() if count > 1]

if duplicates:
    print(f"these are the duplicates{duplicates}")
    dup_list = [duplicates]
    response = input("If you want to delete the duplicate files (y/n) or you just can simply countinu the")
    files_to_delete = duplicates[1:]
    if response == 'y':
        for file_name in files_to_delete:
            folder_path = os.path.join(file_path, file_name)
            if os.path.isfile(folder_path):
                os.remove(file_path)
                print(f"deleted files{folder_path}")
    else:
        print("Nope maybe something went wrong ")            

else:
    print("There is no any duplicates👍")    
