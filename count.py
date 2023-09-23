import os

path = '/workspaces/dataset/New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/Corn/train/Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot'
num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print(f'The number of files in {path} is {num_files}.')
