# pToD_create

This is a simple python (Python 3) script to help systematists to automate the process of creating directories based on filenames and moving the files to their respective directories.
It cycles through the files in the current directory, checks for the file extension (or the presence of a negated pattern) and creates directories based on the file's basenames (names without extensions).

## Usage

`python pToD_create.py <file_extension> [<pattern_to_not_include>]`

* where `<file_extension>` is the extension (without the ".") of the files in which the directory creation will be based on.
* and `<pattern_to_not_include>` (without the brackets) is the pattern present in the names of the files that should be ignored.

Note that Windows users will have to use 'python.exe', 'py.exe', or any other proper command to invoke python interpreter on their system.

## A simple example

Usually, you would want to create different directories to store sequence alignment files from different genes to process them separately.

Suppose you have the following files in your current directory: a1.fas, a2.fas, a3.ref.fas, a4.fas.
* Running `python pToD_create.py fas` will create four directories: a1, a2, a3.ref and a4. Additionally it will move the files to their respective directories.
* Running `python pToD_create.py fas ref` will create three directories: a1, a2 and a4, but not a3.ref (which will be ignored).
