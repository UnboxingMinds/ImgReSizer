#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
This is where your module level help string goes.

.. module:: `Image Re-Sizer`
   :platform: Unix, Windows
   :synopsis: Put a synopsis of what this module does here.

.. moduleauthor:: Tumurtogtokh Davaakhuu <tumurtogtokh@gmail.com>
'''
# IMPORT STANDARD
import time
import os
import logging

# IMPORT Local
import PIL
from PIL import Image

logging.basicConfig(filename='logfile.log', level=logging.DEBUG)


class ImageSizerController:
    '''
    ImageSizer Processor
    '''

    def __init__(self, img, img_url_list, targets, log=True):
        '''
        :arg img: Img class
        :type img: Img object
        :arg img_url_list: list of img urls
        :type img_url_list: str list
        :arg targets: image height sizes
        :type targets: int list
        '''
        self.images = img
        self.images.download_images(img_url_list, log)
        self.target_sizes = targets
        self.keep_log = log

    def perform_resizing(self):
        '''
        Processing images
        '''
        # validation
        if not os.listdir(self.images.input_dir):
            return
        os.makedirs(self.images.output_dir, exist_ok=True)
        # ---------------------------------------------------------------------
        num_images = len(os.listdir(self.images.input_dir))
        # start time for logging
        start = time.perf_counter()

        if self.keep_log:
            logging.info(f'Beginning image resizing at {start}')

        # Processing
        for filename in os.listdir(self.images.input_dir):
            orig_img = Image.open(
                self.images.input_dir + os.path.sep + filename)
            for basewidth in self.target_sizes:
                tmp_img = orig_img
                # calculate target height of the resized image
                # to maintain the aspect ratio
                wpercent = (basewidth / float(tmp_img.size[0]))
                hsize = int((float(tmp_img.size[1]) * float(wpercent)))
                # perform resizing
                tmp_img = tmp_img.resize((basewidth, hsize), PIL.Image.LANCZOS)
                # save the resized image to the output dir with a modified name
                new_filename = os.path.splitext(filename)[0] + \
                    '_' + str(basewidth) + os.path.splitext(filename)[1]
                tmp_img.save(self.images.output_dir +
                             os.path.sep + new_filename)

            # os.remove(self.images.input_dir + os.path.sep + filename)
        # end time for logging
        end = time.perf_counter()

        if self.keep_log:
            logging.info("Created {} thumbnails in {} seconds".
                         format(num_images, end - start))


__all__ = ['ImageSizerController']


def main():
    '''
    Just runs help if necessary
    '''
    import __main__
    help(__main__)


if __name__ == "__main__":
    main()
