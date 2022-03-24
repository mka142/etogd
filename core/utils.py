import typing
from pathlib import Path
import shutil
import magic
from datetime import datetime
import os

def parse_path(path:str) -> typing.Union[str,Path]:
    
    """Returns type of path and pathlib.Path obj

    Args:
        path (str): _description_

    Returns:
        typing.Union[str,Path]: _description_
    """
    p = Path(path)
    
    if not p.exists():
        raise Exception("Given path does not exist")
    
    destination_type = 'folder'
    
    if p.is_file():
        destination_type = 'file'
    
    return (destination_type,Path)

def get_file_mime_type(file_path):
    mime = magic.Magic(mime=True)    
    return mime.from_file(file_path)

def zip_folder(file_name:typing.Union[str,Path],path:typing.Union[str,Path]) -> typing.Union[None,str]:
    """Function that generates zip from given path

    Args:
        path (typing.Union[str,Path]): destination to zip
        file_name (str): name of the file zip that will be created name without extension

    Returns:
        bool: 
    """
    try:
        print(file_name,path)
        destination_path = shutil.make_archive(file_name,'zip',path)
        return destination_path
    except Exception as e:
        print(e)
        return None
    
def current_time_suffix_for_file():
    return datetime.now().strftime('%Y-%m-%d %H-%M-%S')


def make_archive(source, destination):
    base = os.path.basename(str(destination))
    name = base.split('.')[0]
    format = base.split('.')[1]
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    #print(source, destination, archive_from, archive_to)
    shutil.make_archive(name, format, archive_from, archive_to)
    shutil.move('%s.%s'%(name,format), destination)
