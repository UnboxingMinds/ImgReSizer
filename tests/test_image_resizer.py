#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil

from imgresizer import ImageSizerController
from imgresizer import Img

# Clear test files
if not os.path.exists('data'):
    os.mkdir('data')    
shutil.rmtree('data')

IMG_URLS = []
DATA = 'data'
TARGET = [32, 64, 200]

# with open('tests/test_urls.txt', 'r') as test_img_urls:
#     for line in test_img_urls.readline():
#         IMG_URLS.append(line)

def test_image_sizer_controller():    
    test_img = Img(DATA)
    assert os.listdir(test_img.input_dir) == [], 'Input should be empty'
    
    # img_sizer = ImageSizerController(test_img, IMG_URLS, TARGET)
    # assert os.listdir(test_img.output_dir) == [], \
    # 'Output dir should be empty when initialised'

    # TODO: need to change it as controller is not calling download_images 
    # of Img class
    # assert len(os.listdir(test_img.input_dir)) == len(IMG_URLS), \
    # 'input dir should have test images populated'
    

    # img_sizer = ImageSizerController(test_img, IMG_URLS, TARGET)
    # img_sizer.perform_resizing()
    # img_sizer.make_imgs()

    # assert len(os.listdir(test_img.output_dir)) == len(IMG_URLS) * \
    # len(TARGET), 'Output images should be multiplied by test_target size'

    # Clear test files
    shutil.rmtree(test_img.input_dir)
    shutil.rmtree(test_img.output_dir)
    assert not os.path.exists(test_img.input_dir)
    assert not os.path.exists(test_img.output_dir)
