f = open('./names.txt', 'wt')
with f:
    f.write('Ali\n')
    f.write('Mehdi\n')
    f.write('Sepideh\n')
    f.write('Ziba\n')
    f.write('Zeynab\n')
    f.writelines([
        'Reza\n',
        'Morteza\n',
        'Sara\n'
    ])

with open('./names.txt', 'rt') as f:
    print(f.read())
