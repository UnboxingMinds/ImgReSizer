#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
This is where your module level help string goes.

.. module:: `Main`
   :platform: Unix, Windows
   :synopsis: Put a synopsis of what this module does here.

.. moduleauthor:: Tumurtogtokh Davaakhuu <tumurtogtokh@gmail.com>

------------------------------------------------------------
USE: python <PROGNAME> (options)
OPTIONS:
    -h : print this help message
    -t FILE : target size FILE
    -i FILE : image urls FILE
    -l : keep log configuration (default: without)
------------------------------------------------------------
'''
# IMPORT STANDARD
import sys
import os

# IMPORT Local
from imgresizer import Img
from imgresizer import ImageSizerController
from imgresizer import CommandLine

# =============================================================================
# MAIN

if __name__ == '__main__':
    config = CommandLine()
    print(config.process_img_url_file())
    print(config.process_target_file())

    if config.exit:
        sys.exit(0)
    IMG_URLS = config.process_img_url_file()
    TARGET = config.process_target_file()
    HOME = os.getcwd()
    DATA = '/home/tumurtogtokh/Desktop/ImgReSizer/data'

    img_sizer = ImageSizerController(Img(DATA), IMG_URLS, TARGET)
    img_sizer.perform_resizing()
