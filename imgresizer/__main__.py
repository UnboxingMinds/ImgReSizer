#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
------------------------------------------------------------
This is where your module level help string goes.

.. module:: `Main`
   :platform: Unix, Windows
   :synopsis: Put a synopsis of what this module does here.

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
    TARGET = cli.process_target_file()
    DATA = config['data']
    INCOMING = config['input_dir']
    OUTGOING = config['output_dir']

    img_sizer = ImageSizerController(Img(DATA, INCOMING, OUTGOING),
                                     IMG_URLS, TARGET)
    # img_sizer.perform_resizing()
    img_sizer.make_imgs()


if __name__ == '__main__':
    main()
