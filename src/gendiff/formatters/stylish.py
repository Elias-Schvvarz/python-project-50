def stringify(value, depth):
    if isinstance(value, dict):
        indent_size = 4
        current_indent = ' ' * ((depth + 1) * indent_size)
        bracket_indent = ' ' * (depth * indent_size)

        lines = ['{']
        for key, val in value.items():
            formatted_val = stringify(val, depth + 1)
            lines.append(f'{current_indent}{key}: {formatted_val}')
        lines.append(bracket_indent + '}')
        return '\n'.join(lines)

    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if value == '':
        return ''
    return str(value)


def render(ast, depth=1):
    indent_size = 4
    current_indent = ' ' * (depth * indent_size - 2)
    bracket_indent = ' ' * ((depth - 1) * indent_size)

    lines = ['{']

    for node in ast:
        key = node['key']
        node_type = node['type']

        if node_type == 'added':
            val = stringify(node['value'], depth)
            val_str = f' {val}' if val != '' else ''
            lines.append(f'{current_indent}+ {key}:{val_str}')

        elif node_type == 'deleted':
            val = stringify(node['value'], depth)
            val_str = f' {val}' if val != '' else ''
            lines.append(f'{current_indent}- {key}:{val_str}')

        elif node_type == 'unchanged':
            val = stringify(node['value'], depth)
            val_str = f' {val}' if val != '' else ''
            lines.append(f'{current_indent}  {key}:{val_str}')

        elif node_type == 'changed':
            old_val = stringify(node['old_value'], depth)
            new_val = stringify(node['value'], depth)

            old_str = f' {old_val}' if old_val != '' else ''
            new_str = f' {new_val}' if new_val != '' else ''

            lines.append(f'{current_indent}- {key}:{old_str}')
            lines.append(f'{current_indent}+ {key}:{new_str}')

        elif node_type == 'nested':
            children_str = render(node['children'], depth + 1)
            lines.append(f'{current_indent}  {key}: {children_str}')

    lines.append(bracket_indent + '}')
    return '\n'.join(lines)