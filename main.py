#! /usr/bin/python
# -*- coding: utf-8 -*-

import argparse, logging
import json


def main(args):
    with open(args.cfg) as config_f:
        config = json.load(config_f)

        
if __name__ == "__main__":
    logging.setLevel(logging.DEBUG)    
    parser = argparse.ArgumentParser(description='OCRTrain launch')
    parser.add_argument('--cfg', required=True, type=str, help='config path')
    args = parser.parse_args()
    main(args)
