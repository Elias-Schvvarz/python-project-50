from hexlet_code.parser import parse_data
from hexlet_code.differ import build_diff
from hexlet_code.formatters import stylish


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_data(file_path1)
    data2 = parse_data(file_path2)

    ast = build_diff(data1, data2)

    if format_name == 'stylish':
        return stylish.render(ast)

    raise ValueError(f"Unknown format: {format_name}")