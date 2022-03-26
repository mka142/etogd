import hashlib
import json
from pathlib import Path
import os,sys

sys.path.append(str(Path(__file__).resolve().parent.parent))

from core.utils import parse_path

def hash_file(path,BLOCKSIZE=65536):
    hasher = hashlib.sha1()
    with path.open("rb") as file:
        buf = file.read(BLOCKSIZE)
        while buf:
            hasher.update(buf)
            buf = file.read(BLOCKSIZE)
    return hasher.hexdigest()

def create_source_hashes(path):
    result = []
    
    for folder,_,files in os.walk(path):
        for fn in files:
            result.append(hash_file(Path(folder) / fn))
    return result

def are_hash_lists_same(list1,list2):
    if len(list1) != len(list2):
        return False
    
    number_of_common_el_btw_list1_and_list2 = len(
        set(list1).union(set(list2))
                         )
    return number_of_common_el_btw_list1_and_list2 == len(list2)

class source_hashes:
    def __init__(self,filename):
        self.filename = filename
    
    def get_last_data(self):
        try:
            f  = open(self.filename)
            data  = json.load(f)
            f.close()
            return data
        except FileNotFoundError:
            return {}
        
    def get_list_for(self,path):
        data = self.get_last_data()
        return data.get(path,None)
        
    def save_current_source(self,path):
        data = self.get_last_data()
        data[path] = create_source_hashes(path)

        f = open(self.filename,'w')
        json.dump(data,f)
        f.close()
    
    def is_changed(self,path):
        last_hash = self.get_list_for(path)
        
        if last_hash is None:
            return True
        
        current_hash  = create_source_hashes(path)
        
        return not are_hash_lists_same(last_hash,current_hash)
        