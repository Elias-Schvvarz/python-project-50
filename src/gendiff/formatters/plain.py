def stringify(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def render(ast, parent_path=''):
    lines = []

    for node in ast:
        key = node['key']
        node_type = node['type']

        current_path = f"{parent_path}.{key}" if parent_path else key

        if node_type == 'added':
            val = stringify(node['value'])
            lines.append(f"Property '{current_path}' was added with value: {val}")
        elif node_type == 'deleted':
            lines.append(f"Property '{current_path}' was removed")
        elif node_type == 'changed':
            old_val = stringify(node['old_value'])
            new_val = stringify(node['value'])
            lines.append(
                f"Property '{current_path}' was updated. From {old_val} to {new_val}"
            )
        elif node_type == 'nested':
            lines.append(render(node['children'], current_path))

    return '\n'.join(lines)