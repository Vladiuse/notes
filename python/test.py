def transform(string):
    li = string.split(',')
    li = map(lambda iso: f'{iso}', li)
    return list(li)

print(transform(input()))