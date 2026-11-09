import json


def parse_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    # Собираем все уникальные ключи и сортируем их по алфавиту
    keys = sorted(data1.keys() | data2.keys())

    result = ['{']
    for key in keys:
        if key not in data1:
            result.append(f'  + {key}: {data2[key]}')
        elif key not in data2:
            result.append(f'  - {key}: {data1[key]}')
        elif data1[key] == data2[key]:
            result.append(f'    {key}: {data1[key]}')
        else:
            result.append(f'  - {key}: {data1[key]}')
            result.append(f'  + {key}: {data2[key]}')
    result.append('}')

    return '\n'.join(result)