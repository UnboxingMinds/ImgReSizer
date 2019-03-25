#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
------------------------------------------------------------
Main entry for ImgReSizer.

.. module:: `Main`
   :platform: Unix
   :synopsis: Takes configuration json with :py:class: imgresizer.CommandLine and run image processing

.. moduleauthor:: Tumurtogtokh Davaakhuu <tumurtogtokh@gmail.com>
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


def main():
    cli = CommandLine()
    config = cli.load_configuration()

    if cli.exit:
        sys.exit(0)

    IMG_URLS = cli.process_img_url_file()
    TARGET = config['targets']
    MAX_THREADS = config['num_threads']
    DATA = config['data']
    INCOMING = config['input_dir']
    OUTGOING = config['output_dir']

    img_sizer = ImageSizerController(Img(DATA, INCOMING, OUTGOING, MAX_THREADS),
                                     IMG_URLS, TARGET)
    # img_sizer.perform_resizing()
    img_sizer.make_imgs()


if __name__ == '__main__':
    main()
