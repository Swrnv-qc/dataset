import os

path = '/workspaces/dataset/New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/Corn/valid/Corn_(maize)___Common_rust_'
num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print(f'The number of files in {path} is {num_files}.')
