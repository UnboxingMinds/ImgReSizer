#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
This is where your module level help string goes.

.. module:: `Img`
   :platform: Unix, Windows
   :synopsis: Put a synopsis of what this module does here.

.. moduleauthor:: Tumurtogtokh Davaakhuu <tumurtogtokh@gmail.com>
'''
# IMPORT STANDARD
import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve
import threading

# IMPORT Local

logging.basicConfig(filename='logfile.log', level=logging.DEBUG)


class Img:
    '''
    Image Wrapper
    '''

    def __init__(self, home_dir='./data/', max_con_dl=0):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        self.downloaded_bytes = 0
        self.download_lock = threading.Lock()
        if max_con_dl > 1:
            self.max_concurrent_dl = max_con_dl
            self.sem_lock = threading.Semaphore(max_con_dl)
        else:
            self.sem_lock = threading.Semaphore()
        os.makedirs(self.input_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)

    def download_img(self, url, keep_log=False):
        # download each image and save to the input dir
        img_filename = urlparse(url).path.split('/')[-1]
        dest_path = self.input_dir + os.path.sep + img_filename
        
        # downloading images with limit of self.max_concurrent_dl
        self.sem_lock.acquire()
        try:
            with self.download_lock:
                urlretrieve(url, dest_path)
                img_bytes = os.path.getsize(dest_path)
                self.downloaded_bytes += img_bytes
            if keep_log:
                logging.info("<Img> Image downloaded to: " + dest_path)
                logging.info("<Img> Image size: " + str(img_bytes) + ' bytes')
        finally:
            self.sem_lock.release()    
    
    def download_images(self, img_url_list, keep_log=True):
        '''
        Download images from url using threads
        '''
        # validation
        if not img_url_list:
            return
        os.makedirs(self.input_dir, exist_ok=True)
        # ---------------------------------------------------------------------

        # start time for logging
        start = time.perf_counter()

        threads = []
        # Download starts
        for url in img_url_list:
            t = threading.Thread(target=self.download_img, args=(url,))
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()

        # end time for loggin
        end = time.perf_counter()

        if keep_log:
            logging.info("<Img> Downloaded: {} images in {} seconds".
                         format(len(img_url_list), end - start))


# -----------------------------------------------------------------------------
__all__ = ['Img']


def main():
    '''
    Just runs help if necessary
    '''
    import __main__
    help(__main__)


if __name__ == "__main__":
    main()
