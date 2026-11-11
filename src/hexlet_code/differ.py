def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    result = []

    for key in keys:
        if key not in data1:
            result.append({
                'key': key,
                'type': 'added',
                'value': data2[key]
            })
        elif key not in data2:
            result.append({
                'key': key,
                'type': 'deleted',
                'value': data1[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            result.append({
                'key': key,
                'type': 'unchanged',
                'value': data1[key]
            })
        else:
            result.append({
                'key': key,
                'type': 'changed',
                'old_value': data1[key],
                'value': data2[key]
            })
    return result