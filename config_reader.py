import os
import json

config_dir = os.path.join(__file__,'..')
with open(os.path.join(config_dir,'config.json'), 'rt' ) as f:
    data = json.load(f)



