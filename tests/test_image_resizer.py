#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil
import pytest

from imgresizer import ImageSizerController
from imgresizer import Img

# Clear test files
if not os.path.exists('data'):
    os.mkdir('data')
shutil.rmtree('data')

IMG_URLS = []
DATA = 'data'
TARGET = [32, 64, 200]
INCOMING = 'incoming'
OUTGOING = 'outgoing'

with open('tests/img_urls.txt', 'r') as test_img_urls:
    for line in test_img_urls.readlines():
        IMG_URLS.append(line)

test_img = Img(DATA, INCOMING, OUTGOING)
img_sizer = ImageSizerController(Img(DATA, INCOMING, OUTGOING),
                                 IMG_URLS, TARGET)


@pytest.mark.skip('No such file or directory: data/incoming')
def test_image_input_before_test():
    assert os.listdir(test_img.input_dir) == [], 'Input should be empty'

    assert os.listdir(test_img.output_dir) == [], \
        'Output dir should be empty when initialised'


@pytest.mark.skip('TODO')
def test_image_input():
    # TODO: need to change it as controller is not calling download_images
    # of Img class
    assert len(os.listdir(test_img.input_dir)) == len(IMG_URLS), \
        'input dir should have test images populated'


@pytest.mark.skip('Too long to run?')
def test_image_sizer_controller():
    img_sizer.make_imgs()

    assert len(os.listdir(test_img.output_dir)) == len(IMG_URLS) * \
        len(TARGET), 'Output images should be multiplied by test_target size'


@pytest.mark.skip('CLEARING')
def test_clean():
    # Clear test files
    shutil.rmtree(test_img.input_dir)
    shutil.rmtree(test_img.output_dir)
    assert not os.path.exists(test_img.input_dir)
    assert not os.path.exists(test_img.output_dir)
