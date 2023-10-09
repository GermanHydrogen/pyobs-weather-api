from enum import Enum


class SensorType(Enum):
    Temperature = "temp"
    Rain = "rain"
    Pressure = "press"
    SunAltitude = "sunalt"
    WindSpeed = "windspeed"
    Humidity = "humid"
    WindDirection = "winddir"
    SkyMagnitude = "skymag"
    SkyTemperature = "skytemp"
