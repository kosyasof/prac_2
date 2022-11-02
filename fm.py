#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import shutil as sh


# In[1]:


def workplace(user_name):
    if os.path.isdir(os.path.expanduser('C:\\Users\\cosit') + f'\\{user_name}'):
        directory = os.path.expanduser('C:\\Users\\cosit') + f'\\{user_name}'
    else:
        directory = os.path.expanduser('C:\\Users\\cosit' + f'\\{user_name}')
        os.mkdir('C:\\Users\\cosit' + f'\\{user_name}')
    return directory

def create_folder(directory, folder_name):
    try:
        os.mkdir(directory + f'\\{folder_name}')
    except FileExistsError:
        print('Папка с таким названием уже существует!')
    

def create_file(directory, file_name, text=None):
    text_file = open(directory + f'\\{file_name}', "w", encoding='utf-8')
    if text:
        text_file.write(text)
    print(f'файл {file_name}.txt создан')

def rename_file(directory, file1, file2):
    try:
        os.rename(directory + f'\\{file1}', file2)
    except FileNotFoundError:
        print('Неверный путь к файлу!')
        
def get_data(directory, file):
    try:
        if os.access(directory + f'\\{file}', mode=2):
            with open(directory + f'\\{file}', 'r', encoding='utf-8') as f:
                print(' '.join([x.strip('\n') for x in f.readlines()]))
            f.close()
    except FileNotFoundError:
        print('Неверный путь к файлу!')
    
    
def replace_file(directory, file_name, folder):  
    try:
        os.replace(directory + f'\\{file_name}' + '.txt', directory + f'\\{folder}' + f'\\{file_name}')
    except FileNotFoundError:
        print('Неверный путь к файлу!')   
        
def remove_folder_or_file(directory, name):
    if os.path.isdir(directory + f'\\{name}'):
        os.rmdir(directory + f'\\{name}')
    else:
        os.remove(directory + f'\\{name}')
        
def copy_file(directory, file, dest):
    try:
            if os.path.isdir(directory + f'\\{file_name}'):
                sh.copytree(directory + f'\\{file_name}' + '.txt', directory + f'\\{folder}' + f'\\{file_name}')
            else:
                sh.copy(directory + f'\\{file_name}' + '.txt', directory + f'\\{folder}' + f'\\{file_name}')
    except FileNotFoundError:
        print('Неверный путь к файлу!') 
            
def make_archive(directory, archive_from, archive_to):
        shutil.make_archive( directory + f'\\{file_name}' + f'\\archive_from', directory + f'\\{file_name}' + f'\\{archive_to}.zip')


# In[ ]:




