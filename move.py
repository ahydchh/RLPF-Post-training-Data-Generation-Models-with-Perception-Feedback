import os
import shutil
from tqdm import tqdm
with open('dirs.txt','r') as ds:
    dirs = ds.readlines()
for dir_name in dirs:
    dir_name = dir_name.strip()
    source_folder = f'work_dirs/output_img/{dir_name}/val/val-100_scale5_samples5'
    for index in range(5):
        target_folder = os.path.join(source_folder, f'group_{index}')
            
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            
    for filename in tqdm(os.listdir(source_folder)):
        if filename.endswith(".jpg") and "_" in filename:
            name_part, index = filename.rsplit('_', 1)
            index = index.split('.')[0]
            
            target_folder = os.path.join(source_folder, f'group_{index}')
            
            new_filename = f'{name_part}.jpg'
            target_path = os.path.join(target_folder, new_filename)
            
            source_path = os.path.join(source_folder, filename)
            shutil.move(source_path, target_path)
