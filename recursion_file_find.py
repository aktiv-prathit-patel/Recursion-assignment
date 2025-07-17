'''Problem Scenario: Finding a File in a Folder
Imagine you have a file system with folders and files. You want to recursively search for a specific file within a folder structure with the use of recursion.


Problem:

file_to_find = "'/'.join(list_path)"

O/P: File 'birthday.png' found at: /documents/personal/photos/birthday.png'''
file_system = {
    "documents": {
        "work": {
            "report.docx": None,
            "summary.xlsx": None,
        },
        "personal": {
            "photos": {
                "vacation.jpg": None,
                "birthday.png": None,
            },
        },
    },
    "downloads": {
        "software": {
            "setup.exe": None,
        },
        "music": {
            "song.mp3": None,
        },
    },
}
stop = 1
# Recursion Function to find file in file system
def dict_open(my_dict):
    global stop
    for i,j in my_dict.items():
        if i == file_to_find:
            list_path.append(i)
            stop = 0
            print("file_to_find = ",file_to_find)
            return
        elif isinstance(j, dict):
            if file_to_find not in list_path:list_path.append(i)
            dict_open(j)
            if stop: list_path.remove(i)

file_to_find = input('enter what you found : ')
list_path = []
dict_open(file_system)
if file_to_find in list_path:
    print(f'O/P: File {file_to_find} found at: /{"/".join(list_path)}')
else: print(f"{file_to_find} file not found in file_system")