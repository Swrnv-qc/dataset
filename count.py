import os

path = '/path/to/folder'
num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print(f'The number of files in {path} is {num_files}.')
