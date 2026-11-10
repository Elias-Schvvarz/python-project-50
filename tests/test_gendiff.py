import os

import pytest

from hexlet_code import generate_diff
from hexlet_code.parser import parse_data


def test_parse_data():
    file_path = get_fixture_path('file1.json')
    data = parse_data(file_path)
    assert isinstance(data, dict)
    assert data['host'] == 'hexlet.io'


def get_fixture_path(file_name):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'test_data', file_name)


def read_file(file_name):
    path = get_fixture_path(file_name)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()


@pytest.mark.parametrize('format_name', ['stylish'])
def test_gendiff(format_name):
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_file('expected.txt')

    result = generate_diff(file1, file2)
    assert result.strip() == expected