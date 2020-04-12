import sys

class BadFilenameError(Exception):
    pass

def write_to_file(file_name):
    try:
        if not file_name:
            raise BadFilenameError('File name is required')
        my_file = open(file_name, 'x+')
        my_file.write('Meatballs\n')
        my_file.close()
    finally:
        print('This will always called')

file_name = 'recipes.txt'
try:
    write_to_file(file_name)
except FileExistsError :
    print(f"The {file_name} file already exists")
except OSError :
    print(f"OSError in writing to file")
except Exception as err:
    print(f"Unable to write to file: {type(err)}: {err}")
    sys.exit(1)
else:
    print('operation completed successfully')

print('After funtion')

