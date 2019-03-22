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
from queue import Queue
from threading import Thread
from urllib.parse import urlparse
from urllib.request import urlretrieve

# IMPORT Local
import PIL
from PIL import Image

FORMAT = "[%(threadName)s, %(asctime)s, %(levelname)s, %(message)s]"
logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format=FORMAT)


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
        # self.images.download_images_queue(img_url_list, log)
        self.target_sizes = targets
        self.keep_log = log
        self.img_queue = Queue()
        self.dl_queue = Queue()
        self.img_list = img_url_list

    def download_imgs(self, keep_log=True):
        # start time for logging
        start = time.perf_counter()
        while not self.dl_queue.empty():
            try:
                url = self.dl_queue.get(block=False)
                img_filename = urlparse(url).path.split('/')[-1]
                dest_path = self.images.input_dir + os.path.sep + img_filename
                urlretrieve(url, dest_path)
                self.img_queue.put(img_filename)

                self.dl_queue.task_done()
            except Queue.Empty as err:
                logging.info(err)

        # end time for logging
        end = time.perf_counter()
        if keep_log:
            logging.info("Loaded: {} images in {} seconds".
                         format(len(self.img_list), end - start))

    def load_images(self, keep_log=True):
        '''
        Load images from dir
        '''
        # start time for logging
        start = time.perf_counter()

        # Load starts
        for url in self.img_list:
            img_filename = urlparse(url).path.split('/')[-1]
            self.img_queue.put(img_filename)
        # end time for logging
        end = time.perf_counter()

        self.img_queue.put(None)

        if keep_log:
            logging.info("Loaded: {} images in {} seconds".
                         format(len(self.img_list), end - start))

    def download_images(self, img_url_list, keep_log=True):
        '''
        Download images from url
        '''
        # validation
        if not img_url_list:
            return
        os.makedirs(self.images.input_dir, exist_ok=True)
        # ---------------------------------------------------------------------

        # start time for logging
        start = time.perf_counter()

        # Download starts
        for url in img_url_list:
            img_filename = urlparse(url).path.split('/')[-1]
            dest_path = self.images.input_dir + os.path.sep + img_filename
            urlretrieve(url, dest_path)
            self.img_queue.put(img_filename)

        # end time for loggin
        end = time.perf_counter()
        self.img_queue.put(None)

        if keep_log:
            logging.info("Downloaded: {} images in {} seconds".
                         format(len(img_url_list), end - start))

    def perform_resizing_queue(self):
        '''
        Processing images
        '''
        os.makedirs(self.images.output_dir, exist_ok=True)
        # ---------------------------------------------------------------------
        num_images = len(os.listdir(self.images.input_dir))
        # start time for logging
        start = time.perf_counter()

        # Processing
        while True:
            filename = self.img_queue.get()
            if filename:
                orig_img = Image.open(
                    self.images.input_dir + os.path.sep + filename)
                for basewidth in self.target_sizes:
                    tmp_img = orig_img
                    # calculate target height of the resized image
                    # to maintain the aspect ratio
                    wpercent = (basewidth / float(tmp_img.size[0]))
                    hsize = int((float(tmp_img.size[1]) * float(wpercent)))
                    # perform resizing
                    tmp_img = tmp_img.resize(
                        (basewidth, hsize), PIL.Image.LANCZOS)
                    # save the resized image to the output dir with a modified name
                    new_filename = os.path.splitext(filename)[0] + \
                        '_' + str(basewidth) + os.path.splitext(filename)[1]
                    tmp_img.save(self.images.output_dir +
                                 os.path.sep + new_filename)

                # os.remove(self.images.input_dir + os.path.sep + filename)
                self.img_queue.task_done()
            else:
                self.img_queue.task_done()
                break
        # end time for logging
        end = time.perf_counter()

        if self.keep_log:
            logging.info("Created {} thumbnails in {} seconds".
                         format(num_images, end - start))

    def make_imgs(self):
        start = time.perf_counter()
        logging.info('Making images')

        for img_url in self.img_list:
            self.dl_queue.put(img_url)

        num_ts = 8
        for _ in range(num_ts):
            tr = Thread(target=self.download_imgs)
            tr.start()
        # t1 = Thread(target=self.download_images, args=([self.img_list]))
        # t1 = Thread(target=self.load_images)
        t2 = Thread(target=self.perform_resizing_queue)
        # t1.start()
        t2.start()
        # t1.join()
        # ts = []
        # for _ in range(num_ts):
        #     t = Thread(target=self.perform_resizing_queue)
        #     t.start()
        #     ts.append(t)

        self.dl_queue.join()
        self.img_queue.put(None)

        # for t2 in ts:
        #     t2.join()
        t2.join()

        end = time.perf_counter()

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
