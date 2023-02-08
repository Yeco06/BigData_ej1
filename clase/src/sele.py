# python program
import pandas as pd
import yaml
import os

# read config file
config_path= "C:/Users/chaco/OneDrive/Documentos/ULEAD/Ciencias de datos/Big Data/clase/config/config.yml"
config=yaml.load(open(config_path),Loader=yaml.FullLoader)

df=pd.read_csv(config["file_path"])

# print all jugadores
print(df)