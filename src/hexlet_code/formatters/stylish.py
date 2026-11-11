def stringify(value, depth):
    if not isinstance(value, dict):
        if isinstance(value, bool):
            return str(value).lower()
        if value is None:
            return 'null'
        return str(value)

    indent_size = 4
    current_indent = ' ' * (depth * indent_size)
    bracket_indent = ' ' * ((depth - 1) * indent_size)

    lines = ['{']

    for key, val in value.items():
        formatted_val = stringify(val, depth + 1)
        lines.append(f'{current_indent}{key}: {formatted_val}')

    lines.append(bracket_indent + '}')

    return '\n'.join(lines)


def render(ast, depth=1):
    indent_size = 4
    # Отступ для знаков (+, -, ' ') сдвинут на 2 пробела влево
    current_indent = ' ' * (depth * indent_size - 2)
    bracket_indent = ' ' * ((depth - 1) * indent_size)

    lines = ['{']
    for node in ast:
        key = node['key']
        node_type = node['type']

        if node_type == 'added':
            val = stringify(node['value'], depth)
            lines.append(f"{current_indent}+ {key}: {val}")
        elif node_type == 'deleted':
            val = stringify(node['value'], depth)
            lines.append(f"{current_indent}- {key}: {val}")
        elif node_type == 'unchanged':
            val = stringify(node['value'], depth)
            lines.append(f"{current_indent}  {key}: {val}")
        elif node_type == 'changed':
            old_val = stringify(node['old_value'], depth)
            new_val = stringify(node['value'], depth)
            lines.append(f"{current_indent}- {key}: {old_val}")
            lines.append(f"{current_indent}+ {key}: {new_val}")
        elif node_type == 'nested':
            children_str = render(node['children'], depth + 1)
            lines.append(f"{current_indent}  {key}: {children_str}")

    lines.append(bracket_indent + '}')
    return '\n'.join(lines)