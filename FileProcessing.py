import os


def create_file(filename):
    try:
        with open(filename,'w') as fo:
            fo.write('Hello World!')
            print(f'File with {filename} created Successfully...')
    except IOError:
        print(f'Error could not created file with file name {filename}')


def read_file(filename):
    try:
        with open(filename,'r') as fo:
            content = fo.read()
            print(content)
    except IOError:
        print(f'Error could not read {filename} content.')


def write_file(filename,content):
    try:
        with open(filename,'w') as fo:
            fo.write(content)
            print(f'Content write into  {filename} Successfully...')
    except IOError:
        print(f'Error could not write content into file with file name {filename}')


def append_file(filename,content):
    try:
        with open(filename,'a') as fo:
            fo.write(content)
            print(f'Content added into  {filename} Successfully...')
    except IOError:
        print(f'Error could not write content into file with file name {filename}')


def rename_file(filename,newFileName):
    try:
        os.rename(filename,newFileName)
        print(f'File Rename is successfull...')
    except IOError:
        print(f'Error')
