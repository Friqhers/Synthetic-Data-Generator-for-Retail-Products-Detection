
#import examples.datasets.bop_object_physics_positioning.mymain as fridgeScene

import blenderproc as bproc
import argparse
import os
import json

import sys
#sys.path.append('/home/daimia/Desktop/Blenderproc/examples/daimia')
#sys.path.append('/home/daimia/Desktop/Blenderproc/examples')


#import configs.pdg_configuration as pc
from .configs import pdg_configuration as pc

#from examples.datasets.bop_object_physics_positioning import mymain as f
#from datasets.bop_object_physics_positioning import mymain
import requests



# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
def ReadConfigJson(jsonPath : str) -> bool | str:
    print("ReadConfigJson -> Reading configuration json at path: " + jsonPath)

    if(not os.path.exists(jsonPath)):
        print("ReadConfigJson -> File does not exists at path: " + jsonPath)
        return False, None
    
    with open(jsonPath, 'r') as file:
        data = json.load(file)

    return True, data
    
# def StartPort():
#     url = 'https://www.w3schools.com/python/demopage.php'
#     myobj = {'somekey': 'somevalue'}
#     x = requests.post(url, json = myobj)



# parser = argparse.ArgumentParser()
# parser.add_argument("config", nargs="?", default="D:/Unity Datasets/Configuration.json", help="Path to where the config json is saved")
# parser.add_argument("output_dir", nargs="?", default="D:/Unity Datasets/BlenderprocDatasets/", help="Path to where the final files will be saved ")
# parser.add_argument("port", nargs="?", default=100, help="Path to where the config json is saved")

# args = parser.parse_args()

# Successfull, jsonStr = ReadConfigJson(args.config)
# if(not Successfull):
#     print("Couldn't read json file! Exiting...")
#     exit()

# exit()
# root = pc.Root.from_dict(jsonStr)
# print(root)

# #@TODO: read json and write to object
# #read cmd arguments and start data generation

# if(root.Output.Scene == "FridgeScene"):
#     print(root.Output.Scene)

