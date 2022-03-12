import typing
from pathlib import Path
import shutil
from .config import BASE_DIR

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

def zip_folder(path:typing.Union[str,Path],file_name:typing.Union[str,Path]) -> typing.Union[None,str]:
    """Function that generates zip from given path

    Args:
        path (typing.Union[str,Path]): destination to zip
        file_name (str): zipped file name without extension

    Returns:
        bool: 
    """
    try:
        destination_path = shutil.make_archive(file_name,'zip',path)
        return destination_path
    except Exception as e:
        print(e)
        return None