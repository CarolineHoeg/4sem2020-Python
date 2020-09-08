import os
import argparse

def get_file_names(folder_path,out='output.txt'):
    """Takes a path to a folder and writes all filenames 
    in the folder to a specified output file

    Parameters:
    folder_path: The path to the folder
    out: The name of the output file. Default output.txt
    """
    files = os.listdir(folder_path)
    with open(out, 'w') as file_object:
        for file in files:
            file_object.write("%s\n" % file)

def get_all_file_names(folder_path,out='output.txt'):
    """Takes a path to a folder and write all filenames
    recursively (files of all sub folders to)
    
    Parameters:
    folder_path: The path to the folder
    out: The name of the output file. Default output.txt
    """
    directory = os.walk(folder_path)
    with open(out, 'w') as file_object:
        for root, files in directory:
            for name in files:
                print(os.path.join(root, name))
                file_object.write("%s\n" % os.path.join(root, name))

def print_line_one(file_names):
    """Takes a list of filenames and 
    print the first line of each

    Parameters:
    file_names: List of file names
    """
    for file in file_names:
        with open(file) as file_object:
            print(file_object.readline())

def print_emails(file_names):
    """Takes a list of filenames and 
    print each line that contains an email (just look for @)

    Parameters:
    file_names: List of file names
    """
    for file in file_names:
        with open(file) as file_object:
            for line in file_object.readlines():
                if '@' in line:
                    print(line)

def write_headlines(md_files, out='output.txt'):
    """Takes a list of md files and 
    writes all headlines (lines starting with #) to a file

    Parameters:
    md_files: List of .md file names
    out: The name of the output file. Default output.txt
    """
    headlines = []
    for file in md_files:
        with open(file) as file_object:
            for line in file_object.readlines():
                if line.startswith('#'):
                    headlines.append(line)
    with open(out, 'w') as output_file_object:
        for headline in headlines:
            output_file_object.write("%s\n" % headline)

## Cannot get it to work:
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A program that can write filenames to the console or to the output file')
