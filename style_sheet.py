# style details for the helioviewer stats plots

import os

class hvService:
    def __init__(self, name, color, linestyle):
        self.color = ''
        self.linestyle = ''
        self.name = ''
    

screenshot = hvService('screenshot', 'blue', '')
hv = hvService('helioviewer.org movie', 'red', '')
jhv = hvService('JHelioviewer movie', 'green', '')
embed = hvService('embedded', 'pink', '')

all_services = {"screenshot": screenshot,
                "hv": hv,
                "jhv": jhv,
                "embed": embed}

data_directory = os.path.expanduser('~/hv/txt/spd/')
image_directory = os.path.expanduser('~/hv/img/spd/')
format = 'png'