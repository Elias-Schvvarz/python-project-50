from gendiff.differ import build_diff
from gendiff.formatters import format_diff
from gendiff.parser import parse_data


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_data(file_path1)
    data2 = parse_data(file_path2)

    ast = build_diff(data1, data2)
    return format_diff(ast, format_name)