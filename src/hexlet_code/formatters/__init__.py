from hexlet_code.formatters import plain, stylish


def format_diff(ast, format_name='stylish'):
    if format_name == 'stylish':
        return stylish.render(ast)
    elif format_name == 'plain':
        return plain.render(ast)
    raise ValueError(f"Unknown format: {format_name}")