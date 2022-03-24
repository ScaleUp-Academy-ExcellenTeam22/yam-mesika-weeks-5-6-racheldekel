import os


def print_deep_folder():
    """
    this function returns all the files that start with the word deep
    :return: the deep files in the path
    """
    folder_path = input("Insert the path to the folder:")
    directory_list = os.listdir(folder_path)
    deep_files = [f for f in directory_list if f.startswith("deep")]
    print(deep_files)


if __name__ == '__main__':
    print_deep_folder()
