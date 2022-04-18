from distutils.command.config import config
from email.policy import default
import os
#To give command line inputs we use argparse
import argparse
import logging
import yaml




def read_parameters_from_yaml(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config





def main(config_path,datasource):
    config=read_parameters_from_yaml(config_path)
    print(config)



if __name__=="__main__":
    args=argparse.ArgumentParser()
    default_config_path=os.path.join("config","params.yaml")
    args.add_argument("--config",default=default_config_path)
    args.add_argument("--datasource",default=None)
    #if default will be null it will chooe all the configurations from the config file
    parsed_args=args.parse_args()
    print(parsed_args.config,parsed_args.datasource)
    main(config_path=parsed_args.config, datasource=parsed_args.datasource)


