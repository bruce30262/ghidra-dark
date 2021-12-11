#!/usr/bin/env python3

import yaml

""" Get flatlaf config """
flatlaf_version, flatlaf_style = None, None
try:
    with open("config.yml", "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        flatlaf_version = config['flatlaf']['version']
        flatlaf_style = config['flatlaf']['style']
except FileNotFoundError:
    print("Cannot find \"config.yml\" in the directory. Please make sure there's such file in the same folder ( check config_example.yml )")
    exit(1)
except:
    import traceback
    traceback.print_exc()
    exit(1)

