import argparse
import os
import json
import sys
import numpy as np
from .configs import pdg_configuration as pc

#from blenderproc.python.types.MeshObjectUtility import MeshObject
#import blenderproc as bproc



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


def GetConfigurationObject(jsonPath : str):
    Successfull, jsonStr = ReadConfigJson(jsonPath)
    if(not Successfull):
        print("Couldn't read json file!")
        return None
    
    return pc.Root.from_dict(jsonStr)


def GetNewScaleFromCentimeters(targetCm : float):
    # Convert target size to Blender units (1 unit = 1 meter)
    targetSizeBlender = targetCm / 100.0