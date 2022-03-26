import pytest
import tempfile,os,hashlib
from pathlib import Path

from ..hashes import source_hashes,are_hash_lists_same


class Test_are_hash_lists_same():
    a = hashlib.sha1(b'a').hexdigest()
    b = hashlib.sha1(b'b').hexdigest()
    c = hashlib.sha1(b'c').hexdigest()
    d = hashlib.sha1(b'd').hexdigest()
    
    def test_with_different_lists(self):
        
        list1 = [self.a,self.b,self.c]
        list2 = [self.a,self.b,self.c,self.d]
        
        assert False == are_hash_lists_same(list1,list2)
        
    def test_with_different_by_same_length(self):
        list1 = [self.a,self.b,self.d]
        list2 = [self.a,self.b,self.c]
        assert False == are_hash_lists_same(list1,list2)
    
    def test_same_lists(self):
        list1 = [self.a,self.b,self.c]
        list2 = [self.c,self.b,self.a]
        assert True == are_hash_lists_same(list1,list2)

class Test_source_hashes:
    
    def add_file_to_dir(self,source,filename,content=''):
        with open(source / filename,'w') as file:
            file.write(content)
        
    
    def test_get_last_data(self):
        source = tempfile.TemporaryDirectory()
        data_dir = tempfile.TemporaryDirectory()
        
        self.add_file_to_dir(Path(source.name),'nie_mam.txt','nothing')
        
        sh = source_hashes(Path(data_dir.name) / 'data.json')
        assert sh.get_last_data() == {}
        
        sh.save_current_source(source.name)
        
        self.add_file_to_dir(Path(source.name),'cos_innego.txt','nothing1')
        
        assert True == sh.is_changed(source.name)
        
        
        
        