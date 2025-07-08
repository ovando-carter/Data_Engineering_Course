import os
current_directory_path = os.getcwd()
file_path = current_directory_path + '\data_ints.txt'
file_path = os.path.normcase(file_path)
print(file_path)