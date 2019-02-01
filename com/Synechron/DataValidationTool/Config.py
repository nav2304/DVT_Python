# Global Properties Load from properties folder
import configparser
import os
from configparser import ConfigParser


#
# class Config:
#
#
#     def __init__(self):
#         self.config.sections()
#         self.config.read('C:/Users/Vaijnath/PycharmProjects/DVT_Python/files/Properties/projectProperties.ini')
#         print(self.config['default']['ProjectName'])

# Singleton Class for global configuratiosn
class Config:
    class __Config:
        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, arg):
        if not Config.instance:
            Config.instance = Config.__Config(arg)
        else:
            Config.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)
