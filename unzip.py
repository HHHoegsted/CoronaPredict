import os, zipfile

path = r'./data'
directory = os.listdir(path)
files = []
for file in directory:
    files.append(file)

for file in files:
    foldername = r'./data/'+str(file).split('.')[0]
    filename = r'./data/' + str(file)
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(foldername)
    os.remove(filename)

