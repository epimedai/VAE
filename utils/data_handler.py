import urllib.request as urllib
from IPython.display import clear_output
import time
import numpy as np
import zipfile
import os
import h5py

DATA_PATH = 'data/'
FILE_NAME = 'cheng_data.zip'

def download_data(url='https://ndownloader.figshare.com/articles/1512427/versions/5'):
    file_name = FILE_NAME
    if os.path.exists(DATA_PATH+file_name):
        print ('Already downloaded - you can continue')
        return
    
    open_url = urllib.urlopen(url)
    open_file = open(DATA_PATH+file_name, 'wb')
    
    meta = open_url.info()
    file_size = int(open_url.getheader("Content-Length"))
    
    file_size_dl = 0
    block_size = 8192
    prev = -1
    
    used_time = []
    while True:
        start = time.time()
        buffer = open_url.read(block_size)
        if not buffer:
            break
            
        file_size_dl += len(buffer)
        open_file.write(buffer)
        status = int(file_size_dl*100/file_size)
        stop = time.time()
        delta_time = stop-start
        used_time.append(delta_time)
        
        if status != prev:
            clear_output(wait=True)
            time_left = np.mean(used_time)*((file_size-file_size_dl)/block_size)
            print ('{}% done.\tETA: {} minutes'.format(status, int(time_left/60)))
        
        prev = status
        
        
    open_file.close()
    
def extract_data():
    if os.path.exists(DATA_PATH+'mat_files/'):
        print('Already extracted - you can continue')
        return
    
    with zipfile.ZipFile(DATA_PATH+FILE_NAME,"r") as zip_ref:
        zip_ref.extractall(DATA_PATH + 'temp/')
    
    for f in os.listdir(DATA_PATH+'temp/'):
        if f.endswith(".zip"):
            with zipfile.ZipFile(DATA_PATH+'temp/'+f,"r") as zip_ref:
                zip_ref.extractall(DATA_PATH+'mat_files/')
            
    print('Done extracting')
    
def load_mat(path):

    with h5py.File(path, 'r') as f:
        img = f['cjdata']['image']
        img = np.rot90(np.array(img))
        img = np.rot90(img)
        img = np.rot90(img)
        
    return img

def load_data():
    def _normalize(array):
        temp = (array-np.min(array))/(np.max(array)-np.min(array))
        return np.array(temp).astype(np.float32)

    x = []
    for root, _, files in os.walk(DATA_PATH+'mat_files/'):
        for file in files:
            if file.endswith(".mat"):
                img = load_mat(os.path.join(root, file))
                if img.shape!= (512,512):
                    continue
                img = _normalize(img)
                x.append(img)
    x = np.array(x)
    x = x.reshape((*x.shape, 1))
    return x
