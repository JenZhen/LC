import argparse
import os
from heapq import heappush, heappop

class SortValueError(Exception):
    pass

def configArgParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d',
                        '--input_dir',
                        type=str,
                        default='',
                        required=True,
                        help="input directory")
    parser.add_argument('-o',
                        '--output_file',
                        type=str,
                        default='',
                        required=True,
                        help="output file")
    return parser

def get_input_files(input_dir):
    file_name_list = []
    # Append '/' if input does not contain
    if input_dir[-1] != '/':
        input_dir += '/'

    if not os.path.isdir(input_dir):
        err_msg = "Input directory: " + input_dir + " does not exists."
        raise Exception(err_msg)

    for file in os.listdir(input_dir):
        if file.endswith('.txt'):
            file_name_list.append(input_dir + file)
    return file_name_list

def isEOF(file_content):
    return file_content == ''

def isEmptyLine(file_content):
    # 1. empty line aka "\n"
    # 2. multiple empty string " " * n or '\t' etc
    return file_content.isspace()

def merge_files(file_name_list, output_file):
    file_handler_factory = []
    try:
        for file in file_name_list:
            fh = open(file, 'r')
            file_handler_factory.append(fh)
        output_fh = open(output_file, 'w')
        prev_pushed_line = ''
        heap = []

        # Initialize heap with first non-empty line in each input file
        for fh in file_handler_factory:
            line_content = fh.readline()
            if isEOF(line_content):
                # If input file is empty, continue to next file
                continue

            while isEmptyLine(line_content):
                # Search till non-emtpy line push in heap, or
                # Search till EOF, continue to next file
                line_content = fh.readline()
                if isEOF(line_content):
                    break

            if not isEOF(line_content):
                heappush(heap, (line_content, fh))

        while heap:
            (top_line, fh) = heappop(heap)
            if top_line != prev_pushed_line:
                # Avoid duplicate line written into the output file
                output_fh.write(top_line)
                prev_pushed_line = top_line

            new_line = fh.readline()
            while isEmptyLine(new_line):
                new_line = fh.readline()
                if isEOF(new_line):
                    break

            # Check invalid lexicographical order
            if not isEOF(new_line):
                if new_line < prev_pushed_line:
                    err_msg = 'new_line: ' + new_line + \
                              ' should be ordered before prev_pushed_line: ' + \
                              prev_pushed_line
                    raise SortValueError(err_msg)
                else:
                    heappush(heap, (new_line, fh))

    except SortValueError as e:
        print('Found Sorting Error --\n%s\nAborting...' %e.message)
        # Clear previous content into output_file.
        # Simply close and reopen it with 'w' mode
        output_fh.close()
        output_fh = open(output_file, 'w')
    except Exception as e:
        print('Error in merging files: %s' %repr(e))
        output_fh.close()
        output_fh = open(output_file, 'w')
    finally:
        # Always close all files
        for fh in file_handler_factory:
            fh.close()
        output_fh.close()

if __name__ == '__main__':
    parser = configArgParser()
    args = parser.parse_args()

    input_dir = args.input_dir
    output_file = args.output_file

    try:
        # Retrieve all input files given input directory
        file_name_list = get_input_files(input_dir)
        merge_files(file_name_list, output_file)
    except Exception as e:
        print('Error: ' + e.message)
