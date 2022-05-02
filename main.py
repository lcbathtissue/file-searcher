import os

# target_loc = r"C:\Users\CLX Ra"
target_loc = input("Please enter a location to begin searching (e.g. C:\\\\): ")
print()
# type file extensions in lower case
types = []
# types = [
#     # ".sldprt",
#
#     ".jpg",
#     ".jpeg",
#     ".png",
#     ".gif",
#     ".tiff",
#     ".exif",
#     ".bmp",
#     ".heif",
#     ".svg",
# ]
file_type = input("Enter filetype(s) , one on each line, in lower case , type 'next' to proceed (e.g. .jpg): ")
types.append(file_type)
while file_type != "next":
    file_type = input()
    types.append(file_type)


future_search_paths = []
found_files = []
error_file = open("permission_errors.txt", "w")
error_file.close()


def recursive_search(start_path):
    global future_search_paths, types, found_files
    try:
        folder_contents = os.listdir(start_path)
        for file in folder_contents:
            path = start_path + "\\" + file
            if os.path.isdir(path) is True:
                future_search_paths.append(path)
            else:
                for type in types:
                    if path.endswith(type.lower()) is True:
                        print(path)
                        found_files.append(path)
    except PermissionError:
        error_file = open("permission_errors.txt", "a")
        error_file.write(f"{start_path}\n")
        error_file.close()


recursive_search(target_loc)

for path in future_search_paths:
    recursive_search(path)
print()

output_file = open("output.txt", "w")
output_file.close()

output_file = open("output.txt", "a")
for found_file in found_files:
    print(found_file)
    output_file.write(f"{found_file}\n")
output_file.close()
