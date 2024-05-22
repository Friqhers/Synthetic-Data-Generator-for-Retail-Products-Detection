from typing import List
from typing import Any
from dataclasses import dataclass
import json

@dataclass
class UserProvidedCentimeterScale:
    X: float
    Y: float
    Z: float

    @staticmethod
    def from_dict(obj: Any) -> 'UserProvidedCentimeterScale':
        _X = float(obj.get("X"))
        _Y = float(obj.get("Y"))
        _Z = float(obj.get("Z"))
        return UserProvidedCentimeterScale(_X, _Y, _Z)
    
@dataclass
class DefaultRotation:
    X: float
    Y: float
    Z: float

    @staticmethod
    def from_dict(obj: Any) -> 'DefaultRotation':
        _X = float(obj.get("X"))
        _Y = float(obj.get("Y"))
        _Z = float(obj.get("Z"))
        return DefaultRotation(_X, _Y, _Z)

@dataclass
class General:
    GreyscaleType: str
    CameraDistanceMin: float
    CameraDistanceMax: float
    CameraElevationAngleMin: int
    CameraElevationAngleMax: int
    CameraPolarAngleMin: int
    CameraPolarAngleMax: int
    RandomOffsetFromCenter: bool
    PreventObjectCollision: bool
    RandomizeObjectPositions: bool
    RandomizeVisibilityOrderOfObjects: bool
    MaxLightDensity: int
    MinLightCount: int
    MaxLightCount: int
    RandomizeLightColor: bool
    RandomizeLightRange: bool
    MinLightRange: float
    MaxLightRange: float
    SkyBoxMaterialIDList: List[int]
    OccludedObjectPercentage: int
    EmptyImagePercentage: int
    SpawnRandomDistractorObjects: bool
    MinDistractorCount: int
    MaxDistractorCount: int
    ToggleAirRotationPosition: bool
    AirRotationPositionStartSampleNum: int

    @staticmethod
    def from_dict(obj: Any) -> 'General':
        _GreyscaleType = str(obj.get("GreyscaleType"))
        _CameraDistanceMin = float(obj.get("CameraDistanceMin"))
        _CameraDistanceMax = float(obj.get("CameraDistanceMax"))
        _CameraElevationAngleMin = int(obj.get("CameraElevationAngleMin"))
        _CameraElevationAngleMax = int(obj.get("CameraElevationAngleMax"))
        _CameraPolarAngleMin = int(obj.get("CameraPolarAngleMin"))
        _CameraPolarAngleMax = int(obj.get("CameraPolarAngleMax"))
        _RandomOffsetFromCenter = bool(obj.get("RandomOffsetFromCenter"))
        _PreventObjectCollision = bool(obj.get("PreventObjectCollision"))
        _RandomizeObjectPositions = bool(obj.get("RandomizeObjectPositions"))
        _RandomizeVisibilityOrderOfObjects = bool(obj.get("RandomizeVisibilityOrderOfObjects"))
        _MaxLightDensity = int(obj.get("MaxLightDensity"))
        _MinLightCount = int(obj.get("MinLightCount"))
        _MaxLightCount = int(obj.get("MaxLightCount"))
        _RandomizeLightColor = bool(obj.get("RandomizeLightColor"))
        _RandomizeLightRange = bool(obj.get("RandomizeVisibilityOrderOfObjects"))
        _MinLightRange = float(obj.get("MinLightRange"))
        _MaxLightRange = float(obj.get("MaxLightRange"))
        _SkyBoxMaterialIDList = [y for y in obj.get("SkyBoxMaterialIDList")]
        _OccludedObjectPercentage = int(obj.get("OccludedObjectPercentage"))
        _EmptyImagePercentage = int(obj.get("EmptyImagePercentage"))
        _SpawnRandomDistractorObjects = bool(obj.get("SpawnRandomDistractorObjects"))
        _MinDistractorCount = int(obj.get("MinDistractorCount"))
        _MaxDistractorCount = int(obj.get("MaxDistractorCount"))
        _ToggleAirRotationPosition = bool(obj.get("ToggleAirRotationPosition"))
        _AirRotationPositionStartSampleNum = int(obj.get("AirRotationPositionStartSampleNum"))
        return General(_GreyscaleType, _CameraDistanceMin, _CameraDistanceMax, _CameraElevationAngleMin, _CameraElevationAngleMax, _CameraPolarAngleMin, _CameraPolarAngleMax, _RandomOffsetFromCenter, _PreventObjectCollision, _RandomizeObjectPositions, _RandomizeVisibilityOrderOfObjects, _MaxLightDensity, _MinLightCount, _MaxLightCount, _RandomizeLightColor, _RandomizeLightRange, _MinLightRange, _MaxLightRange, _SkyBoxMaterialIDList, _OccludedObjectPercentage, _EmptyImagePercentage, _SpawnRandomDistractorObjects, _MinDistractorCount, _MaxDistractorCount, _ToggleAirRotationPosition, _AirRotationPositionStartSampleNum)


@dataclass
class Model:
    Name: str
    UserProvidedCentimeterScale: UserProvidedCentimeterScale
    DefaultRotation: DefaultRotation
    ScaleMode: int
    Scale: float
    MaxScale: float
    MinScale: float
    MinCount: int
    MaxCount: int
    Materials: List[object]
    RandomizeColor: bool
    RandomRotationAxis: str
    IsDistractor: bool
    RandomizeScale: bool
    RandomizeUpsideAndDownside: bool
    FixedAngles: bool
    Id: str
    Filepath: str

    @staticmethod
    def from_dict(obj: Any) -> 'Model':
        _Name = str(obj.get("Name"))
        _UserProvidedCentimeterScale = UserProvidedCentimeterScale.from_dict(obj.get("UserProvidedCentimeterScale"))
        _DefaultRotation = DefaultRotation.from_dict(obj.get("DefaultRotation"))
        _ScaleMode = int(obj.get("ScaleMode"))
        _Scale = float(obj.get("Scale"))
        _MaxScale = float(obj.get("MaxScale"))
        _MinScale = float(obj.get("MinScale"))
        _MinCount = int(obj.get("MinCount"))
        _MaxCount = int(obj.get("MaxCount"))
        _Materials = [y for y in obj.get("Materials")]
        _RandomizeColor = bool(obj.get("RandomizeColor"))
        _RandomRotationAxis = str(obj.get("RandomRotationAxis"))
        _IsDistractor = bool(obj.get("IsDistractor"))
        _RandomizeScale = bool(obj.get("RandomizeScale"))
        _RandomizeUpsideAndDownside = bool(obj.get("RandomizeUpsideAndDownside"))
        _FixedAngles = bool(obj.get("FixedAngles"))
        _Id = str(obj.get("Id"))
        _Filepath = str(obj.get("Filepath"))
        return Model(_Name, _UserProvidedCentimeterScale, _DefaultRotation, _ScaleMode, _Scale, _MaxScale, _MinScale, _MinCount, _MaxCount, _Materials, _RandomizeColor, _RandomRotationAxis, _IsDistractor, _RandomizeScale, _RandomizeUpsideAndDownside, _FixedAngles, _Id, _Filepath)


@dataclass
class Input:
    Models: List[Model]

    @staticmethod
    def from_dict(obj: Any) -> 'Input':
        _Models = [Model.from_dict(y) for y in obj.get("Models")]
        return Input(_Models)
    
@dataclass
class Output:
    RgbImageFormat: str
    DepthImageFormat: str
    MaskImageFormat: str
    Resolution: str
    DatasetFormat: str
    Scene: str
    AdditionalFiles: str
    NumberOfSamples: int

    @staticmethod
    def from_dict(obj: Any) -> 'Output':
        _RgbImageFormat = str(obj.get("RgbImageFormat"))
        _DepthImageFormat = str(obj.get("DepthImageFormat"))
        _MaskImageFormat = str(obj.get("MaskImageFormat"))
        _Resolution = str(obj.get("Resolution"))
        _DatasetFormat = str(obj.get("DatasetFormat"))
        _Scene = str(obj.get("Scene"))
        _AdditionalFiles = str(obj.get("AdditionalFiles"))
        _NumberOfSamples = int(obj.get("NumberOfSamples"))
        return Output(_RgbImageFormat, _DepthImageFormat, _MaskImageFormat, _Resolution, _DatasetFormat, _Scene, _AdditionalFiles, _NumberOfSamples)

@dataclass
class Root:
    Output: Output
    General: General
    Input: Input

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _Output = Output.from_dict(obj.get("Output"))
        _General = General.from_dict(obj.get("General"))
        _Input = Input.from_dict(obj.get("Input"))
        return Root(_Output, _General, _Input)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
