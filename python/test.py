

with open('/home/vlad/notes/notes/python/some.txt',) as file:
    text = file.read()
    text = text.lower()
print(text)
with open('/home/vlad/notes/notes/python/some.txt', 'w') as file:
    file.write(text)
print('DONE')