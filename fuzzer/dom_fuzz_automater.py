import os
import sys
import argparse
import subprocess
import pathlib 

## create a function to take CLI arguments and create an error if argument not provided
parser = argparse.ArgumentParser(description='Automate browser')
parser.add_argument('-d', '--directory', help='Enter path to the directory containing test files')
parser.add_argument('-b', '--browser', help='Enter path to browser you want to fuzz')
args = parser.parse_args()

## create function edit_file() to add a string to a file called test.txt
def edit_file(file_name, string_to_add):
    with open(file_name, 'a') as file:
        file.write(string_to_add)

## create a function to loop over test cases and append js to close file
def loop_append():
    for file in os.listdir(args.directory):
        print('Appending to ' + file)
        edit_file(args.directory + '/' + file, '\n<script type="text/javascript">window.close();</script>')

#loop_append()

## create a function called fuzz_browser() to run a binary file

def fuzz_browser():
    for file in os.listdir(args.directory):
        print('Fuzzing ' + file)
        bashCommand = args.browser + ' ' + args.directory + '/' + file
        print(bashCommand)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

fuzz_browser()