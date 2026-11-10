import json


def parse_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def stringify(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    keys = sorted(data1.keys() | data2.keys())

    result = ['{']
    for key in keys:
        if key not in data1:
            result.append(f'  + {key}: {stringify(data2[key])}')
        elif key not in data2:
            result.append(f'  - {key}: {stringify(data1[key])}')
        elif data1[key] == data2[key]:
            result.append(f'    {key}: {stringify(data1[key])}')
        else:
            result.append(f'  - {key}: {stringify(data1[key])}')
            result.append(f'  + {key}: {stringify(data2[key])}')
    result.append('}')

    return '\n'.join(result)