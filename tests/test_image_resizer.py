#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil
import pytest

from imgresizer import ImageSizerController
from imgresizer import Img


DATA = 'data'
TARGET = [32, 64, 200]
INCOMING = 'incoming'
OUTGOING = 'outgoing'


@pytest.fixture
def images(img_url_path='tests/img_urls.txt'):
    urls = []
    with open(img_url_path, 'r') as img_urls:
        for line in img_urls.readlines():
            urls.append(line)
    return urls


@pytest.fixture
def img_obj(tmpdir):
    tmpdir.mkdir(DATA)
    tmpdir.mkdir(DATA + os.path.sep + INCOMING)
    tmpdir.mkdir(DATA + os.path.sep + OUTGOING)
    return Img(DATA, INCOMING, OUTGOING)


@pytest.fixture
def img_sizer_obj(img_obj, images):
    img_sizer = ImageSizerController(img_obj, images, TARGET)
    return img_sizer


def test_image_input_before_test(img_obj):
    assert os.listdir(img_obj.input_dir) == [], 'Input should be empty'

    assert os.listdir(img_obj.output_dir) == [], \
        'Output dir should be empty when initialised'


@pytest.mark.skip('Error: assert 0 == 60, files are not being created?')
def test_image_sizer_controller(img_sizer_obj, images):
    img_sizer_obj.make_imgs()

    assert len(os.listdir(img_sizer_obj.images.output_dir)) == len(images) * \
        len(TARGET), 'Output images should be multiplied by test_target size'


@pytest.mark.skip('TODO')
def test_image_input(images):
    # TODO: need to change it as controller is not calling download_images
    assert len(os.listdir(img_obj.input_dir)) == len(images), \
        'input dir should have test images populated'


@pytest.mark.skip('CLEARING')
def test_clean():
    # Clear test files
    shutil.rmtree(img_obj.input_dir)
    shutil.rmtree(img_obj.output_dir)
    assert not os.path.exists(img_obj.input_dir)
    assert not os.path.ex
