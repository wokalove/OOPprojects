import fs
dir = fs.open_fs('mem://')
dir.makedirs('fruit')

dir.makedirs('vegetables')

with dir.open('fruit/apple.txt', 'w') as apple: apple.write('braeburn')

dir.tree()