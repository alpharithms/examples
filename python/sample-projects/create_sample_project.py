# Author: Zack West (alphazwest@gmail.com)
# License: MIT

import os
from shutil import rmtree
import string
from random import choice

# Define the current location
HERE = os.path.abspath(os.path.dirname(__file__))


def create_sample_project(
        num_dirs: int, num_files: int,
        random_content_len: int = 256,
        root_name: str = "sample_project",
        base_dirname: str = "sample_dir",
        base_filename: str = "sample_file",
        print_output: bool = False
):
    """
    Creates a local subdirectory with random files, containing random data, such that
    local sample projects can be quickly and completely setup.
    Args:
        num_dirs: the number of directories to create.
        num_files: the number of files per directory to create.
        random_content_len: the length, in characters, of random content created for each file.
        root_name: the name of the root project directory.
        base_dirname: basename for directories, will be appended with the integer count as "basename_i"
        base_filename: basename for files, will be created as "basename_i_j.txt" where i is the dir, j is the file.
        print_output: optional switch to output a tab-indented version suited for use with ASCII tree generators.

    Example output using 2 num_dirs, 3 num_files, and setting print_output to True:
        sample_project
            sample_dir_0
                sample_file_0_0.txt
                sample_file_0_1.txt
                sample_file_0_2.txt
            sample_dir_1
                sample_file_1_0.txt
                sample_file_1_1.txt
                sample_file_1_2.txt

    Returns:
        a list of all files and directories created
    """
    # init container for output
    output = []

    # Define a local root for the sample project, create dir
    sample_project_directory = os.path.abspath(os.path.join(HERE, root_name))

    # deletes existing
    if os.path.exists(sample_project_directory):
        rmtree(sample_project_directory)

    # Create new
    os.mkdir(sample_project_directory)
    if print_output:
        print(root_name)

    # Create random directories
    for i in range(num_dirs):
        new_dirname = f"{base_dirname}_{i}"
        new_dir = os.path.abspath(os.path.join(sample_project_directory, new_dirname))
        os.mkdir(new_dir)
        output.append(new_dir)

        if print_output:
            print("    ", new_dirname)

        # Create random files in directory
        for j in range(num_files):
            new_filename = f"{base_filename}_{i}_{j}.txt"
            new_file = os.path.abspath(os.path.join(new_dir, new_filename))
            if print_output:
                print("        ", new_filename)
            with open(new_file, 'w')as file:

                # Creates a random string of characters
                file.write("".join([choice(string.ascii_letters) for _ in range(random_content_len)]))
                output.append(new_file)

    return output


if __name__ == "__main__":

    # Creates a sample project with two subdirectories each containing 3 files
    # and prints the output as 4-space separated entries where each level receives
    # +4 spaces to mimic the visuals of a tab. Example Output:
    create_sample_project(2, 3, print_output=True)
