import pytest
import hashlib

from ..utils import extract_sources_dirs


class Test_extract_sources_dirs():
    def test_with_one_dir(self):
        env_var = 'some_app_data:/etod/sources/some_dir'
        result = extract_sources_dirs(env_var)
        
        assert result == [('some_app_data','/etod/sources/some_dir')]
    def test_with_more_dirs(self):
        env_var = 'some_app_data:/etod/sources/some_dir,somme_other_app_data:/etod/sources/some_other_dir'
        result = extract_sources_dirs(env_var)
        
        assert result == [('some_app_data','/etod/sources/some_dir'),('somme_other_app_data','/etod/sources/some_other_dir')]
        
