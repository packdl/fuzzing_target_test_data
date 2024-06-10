import shutil
import os
from pathlib import Path
import random

def copy_files(new_location, chosen_files):
    
    with open(os.path.join(new_location, 'README'),'w') as FILE_:
        for indiv_file in chosen_files:
            FILE_.write(str(os.stat(indiv_file).st_size) + indiv_file+'\n')
    
            shutil.copy(indiv_file,new_location)


def get_files(new_location, max_size=1024, max_num_files=10, ext=None):
        
    if not Path(new_location).exists():
        os.mkdir(new_location)
        
    potential_files = []

    for dirpath, dirs, filename in os.walk('.'):
        for name in filename:

            if ext and ext not in name:
                continue
            FILE_ = os.path.join(dirpath, name)
            fileinfo = os.stat(FILE_)
            if fileinfo.st_size > max_size:
                continue
            potential_files.append(FILE_)
    
    potential_files = list(set(sorted(potential_files, key=lambda x: os.stat(x).st_size)))
    for x in potential_files:
        print(str(os.stat(x).st_size) +f' {x}')

    if max_num_files >= len(potential_files):
        copy_files(new_location, potential_files)
    else:
        copy_files(new_location, random.choices(potential_files, k=max_num_files))