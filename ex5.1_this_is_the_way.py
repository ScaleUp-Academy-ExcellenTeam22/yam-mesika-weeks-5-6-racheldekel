import os
INPUT_FOLDER_MESSAGE="insert the path to the folder:"
# function that print the file in folder that start with "deep"
def print_deep_folder():
    folder_path = input(INPUT_FOLDER_MESSAGE)
    directory_list = os.listdir(folder_path)
    only_deep = [f for f in directory_list if f.startswith("deep")]
    print(only_deep)

#print the program
if __name__ == '__main__':
    print_deep_folder()