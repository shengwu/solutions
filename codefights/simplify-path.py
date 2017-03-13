# pretty bad, but it seems to pass the tests

def simplifyPath(path):
    parts = filter(lambda x: x and x != '.', path.split('/'))
    i = 0
    while i < len(parts):
        if parts[i] == '..' and i > 0:
            parts = parts[:i-1] + parts[i+1:]
            i -= 1
        elif parts[i] == '..':
            parts = parts[1:]
        else:
            i += 1
    return '/' + '/'.join(parts)
