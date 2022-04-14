import os
#To give command line inputs we use argparse
import argparse
import yaml
import logging




if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="default")
    args.add_argument("--datasource",default=None)
    #if default will be null it will chooe all the configurations from the config file
    parsed_args=args.parse_args()
    print(parsed_args.config)


