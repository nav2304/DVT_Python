#Execution start point

import os
import configparser
import com.Synechron.DataValidationTool.Config as configs

os.putenv("ProjectDir", os.path.dirname(os.path.abspath(__file__)))
currentFolder = os.path.dirname(os.path.abspath(__file__))
print(currentFolder)
configs.config = configparser.ConfigParser()
configs.config.sections()
configs.config.read('files/Properties/projectProperties.ini')
print(configs.config['default']['ProjectName'])
