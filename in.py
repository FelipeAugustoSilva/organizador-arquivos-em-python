import os
cwd = os.getcwd()


full_list = os.listdir(cwd)
#print(files_list)

files_list = [i for i in full_list if os.path.isfile(i) and '.py' not in i] #  os.path.isfile so captura arquivos, ignorando pastas e and '.py' ignorando arquivos python
#print(files_list)
types = [i.split('.')[1] for i in files_list] 
print(types) # ['txt', 'jnlp', 'pdf', 'mp4', 'pdf', 'pdf', 'pdf', 'pdf', 'ini', 'pdf', 'pdf', 'exe', 'html', 'pdf', 'zip', 'zip', 'psf', 'txt', 'docx']

types = set([i.split('.')[1] for i in files_list]) 
print(types) #{'html', 'zip', 'txt', 'docx', 'ini', 'exe', 'mp4', 'pdf', 'psf', 'jnlp'}

types = list(set([i.split('.')[1] for i in files_list])) 
print(types) #['html', 'zip', 'txt', 'docx', 'ini', 'exe', 'mp4', 'pdf', 'psf', 'jnlp']

#Cria as pastas com base no .estensão dos arquivos
for file_type in types:
    os.mkdir(file_type)

for file in files_list:
    from_path = os.path.join(cwd, file)
    to_path = os.path.join(cd, file.split('.')[-1], file)

    os.replace(from_path, to_path)