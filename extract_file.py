path_file = input().split("\\")
file_info = path_file[-1]
name = file_info.split(".")[0]
extension = file_info.split(".")[1]
print(f"File name: {name}")
print(f"File extension: {extension}")
