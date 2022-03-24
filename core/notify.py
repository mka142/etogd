from ossaudiodev import SNDCTL_SYNTH_MEMAVL
import apprise
from typing import Union

def notify(schema:Union[str,list],*args, **kwargs):
    apobj = apprise.Apprise()
    
    if not len(schema):
        return
    
    if type(schema) == list:
        for service in schema:
            apobj.add(service)
    else:
        apobj.add(schema)
        
    apobj.notify(*args, **kwargs)