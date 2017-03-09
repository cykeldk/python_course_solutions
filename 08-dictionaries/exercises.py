image = {'color': 'greyscale', 'size': 289983, 'type': 'jpg',
         'address': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Moby_Dick_p510_illustration.jpg'}
for key, value in image.items():
    print('{0} : {1}'.format(key,value))


print('is color in image? {}'.format('color' in image.keys()))
