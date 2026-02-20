# Parses arguments

from pathlib import Path
import argparse

from file_processing import ingest_file
from file_processing import output_file

# Parse command line arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
arg_parser.add_argument("out_file", type=str, help="Output File Pathname")
arg_parser.add_argument("--solve_equation", action='store_true',
                        help="Flag indicating whether to solve the input equations")
args = arg_parser.parse_args()

in_path = Path(args.in_file)
out_path = Path(args.out_file)

# Call the functions to read in, process, and output files
output = ingest_file(in_path, args.solve_equation)
output_file(out_path, output)
