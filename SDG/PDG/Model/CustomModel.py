class CustomModel:
    # list of all spawned objects
    ObjectWithInfo : []
    ObjectID : int
    ObjectName : str
    #MeshObjectRef : bproc.python.types.MeshObjectUtility.MeshObject

    def __init__(self, id : int, name : str):
        self.ObjectID = id
        self.ObjectName = name
    