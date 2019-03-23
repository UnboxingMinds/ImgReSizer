#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# IMPORT Standard
import os
import shutil
import pytest

# IMPORT Custom
from imgresizer import Img

DATA = 'data'
INCOMING = 'incoming'
OUTGOING = 'outgoing'


@pytest.fixture
def images():
    urls = []
    with open('tests/img_urls.txt', 'r') as test_img_urls:
        for line in test_img_urls.readlines():
            urls.append(line)
    return urls


def test_img_urls(images):
    assert len(images) == 20, 'IMG_URLS should have 20 link'


def test_image_before_init():
    '''
    Test before init for Img class
    '''
    test_data_path = 'test_data_path'
    assert not os.path.exists(test_data_path), \
        f'{test_data_path} should not exists'


def test_data_path():
    test_data_path = 'test_data_path'
    img = Img(test_data_path)
    assert img.input_dir == test_data_path + os.path.sep + 'incoming', \
        f'{img.input_dir} should match'
    assert img.output_dir == test_data_path + os.path.sep + 'outgoing', \
        f'{img.output_dir} should match'

    # Clear test dirs
    shutil.rmtree(test_data_path)
    assert not os.path.exists(test_data_path), 'Test file should be deleted'


def test_incoming_dir():
    img_default = Img()
    assert img_default.input_dir == './data/' + os.path.sep + 'incoming', \
        f'{img.input_dir} should match'
    assert img_default.output_dir == './data/' + os.path.sep + 'outgoing', \
        f'{img.output_dir} should match'

    # Clear test files
    shutil.rmtree(img_default.input_dir)
    shutil.rmtree(img_default.output_dir)
    assert not os.path.exists(
        img_default.input_dir), 'Test file should be deleted'
    assert not os.path.exists(
        img_default.input_dir), 'Test file should be deleted'


def test_image_init():
    '''
    Test init for Img class
    '''
    test_img = Img()
    assert os.path.isdir(test_img.input_dir), f'Is {test_img.input_dir} dir?'
    assert os.path.isdir(test_img.output_dir), f'Is {test_img.output_dir} dir?'
    assert os.listdir(test_img.input_dir) == [], \
        f'{test_img.input_dir} should be empty'
    assert os.listdir(test_img.output_dir) == [], \
        f'{test_img.output_dir} should be empty'


def test_download_images(images):
    '''
    Test download_images for Img class
    '''
    test_img = Img()
    test_img.download_images(images)
    assert len(os.listdir(test_img.input_dir)) == len(images), \
        f'After downloading, {test_img.input_dir} should have images'

    # Clear test files
    shutil.rmtree(test_img.input_dir)
    shutil.rmtree(test_img.output_dir)
    assert not os.path.exists(
        test_img.input_dir), 'Test file should be deleted'
    assert not os.path.exists(
        test_img.output_dir), 'Test file should be deleted'
