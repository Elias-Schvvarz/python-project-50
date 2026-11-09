from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument('first_file', type=str, help='path to first file')
    parser.add_argument('second_file', type=str, help='path to second file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set output format (default: stylish)'
    )
    return parser.parse_args()