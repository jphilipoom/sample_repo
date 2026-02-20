# Reads in in_file, passes to conversion function, writes output to outfile
# I decided to make these separate files to allow you to comment out one call or
# the other more easily for more streamlined debugging.

from pre_to_post import prefix_to_postfix
from solver import postfix_solver


def ingest_file(file_path, solve_equation):
    # Reads in file line by line, cleans each line, passes to prefix_to_postfix function,
    # and reformats the output for export.
    # Lines that contain only spaces or tabs will be skipped
    output = ''
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line = line.rstrip(' \t\n')

            if line != '':
                postfix_str = prefix_to_postfix(line)
                output = output + postfix_str + '\n'

                if solve_equation:
                    ans = postfix_solver(postfix_str)
                    output = output + ans + '\n'

    return output


def output_file(file_path, output):
    # Writes output to file
    with open(file_path, 'w') as g:
        g.write(output)

    return
