from hexlet_code.scripts.gendiff import parse_args
from hexlet_code.parser import parse_data


def main():
    args = parse_args()

    # Читаем и парсим файлы через отдельный модуль
    data1 = parse_data(args.first_file)
    data2 = parse_data(args.second_file)

    # В дальнейшем здесь будет вызов функции сравнения (diff)
    print("Parsed data 1:", data1)
    print("Parsed data 2:", data2)


if __name__ == '__main__':
    main()