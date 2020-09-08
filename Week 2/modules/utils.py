import os
import argparse

def files_in_folder(folder_path, output_file):
    """Takes a path to a folder and writes all filenames 
    in the folder to a specified output file

    Parameters:
    folder_path: The path to the folder
    output_file: The name of the output file
    """
    files = os.listdir(folder_path)
    with open(output_file, 'w') as file_object:
        for file in files:
            file_object.write("%s\n" % file)

def files_in_folder_recursive(folder_path, output_file):
    """Takes a path to a folder and write all filenames
    recursively (files of all sub folders to)
    
    Parameters:
    folder_path: The path to the folder
    output_file: The name of the output file
    """
    directory = os.walk(folder_path)
    with open(output_file, 'w') as file_object:
        for root, files in directory:
            for name in files:
                print(os.path.join(root, name))
                file_object.write("%s\n" % os.path.join(root, name))

def print_first(files):
    """Takes a list of filenames and 
    print the first line of each

    Parameters:
    files: List of file names
    """
    for file in files:
        with open(file) as file_object:
            print(file_object.readline())

def print_emails(files):
    """Takes a list of filenames and 
    print each line that contains an email (just look for @)

    Parameters:
    files: List of file names
    """
    for file in files:
        with open(file) as file_object:
            for line in file_object.readlines():
                if '@' in line:
                    print(line)

def write_headlines(output_file, files):
    """Takes a list of md files and 
    writes all headlines (lines starting with #) to a file

    Parameters:
    output_file: Name of the file to write the headlines to
    files: List of .md file names
    """
    headlines = []
    for file in files:
        with open(file) as file_object:
            for line in file_object.readlines():
                if line.startswith('#'):
                    headlines.append(line)
    with open(output_file, 'w') as output_file_object:
        for headline in headlines:
            output_file_object.write("%s\n" % headline)

## Cannot get it to work:
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A program that can write filenames to the console or to the output file')
    parser.add_argument('method', help='Name of the method to call. Existing methods are called: "files_in_folder", "files_in_folder_recursive", "print_first"')
    parser.add_argument('--folder_path', help='Name of the folder path. Needed for "files_in_folder", "files_in_folder_recursive"')
    parser.add_argument('--output_file', help='Name of the output file. Needed for "files_in_folder", "files_in_folder_recursive"')
    parser.add_argument('--files', help='List of file names. Needed for "print_first"')
    args = parser.parse_args()

    if args.method == 'files_in_folder':
        files_in_folder(args.folder_path, args.output_file)
