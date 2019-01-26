# Enum To Create the definite connection Types
# importing enum for enumerations 
from enum import Enum


# creating enumerations using class
class ConnectionType(Enum):
    Oracle = "Oracle"
    SQLServer = "SQLServer"
    MySQL = "MySQL"
    File="File"