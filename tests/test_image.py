#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# IMPORT Standard
import os
import shutil

# IMPORT Custom
from ImgSizer import Img

IMG_URLS = \
    ['https://dl.dropboxusercontent.com/s/2fu69d8lfesbhru/pexels-photo-48603.jpeg',
     'https://dl.dropboxusercontent.com/s/zch88m6sb8a7bm1/pexels-photo-134392.jpeg',
     'https://dl.dropboxusercontent.com/s/lsr6dxw5m2ep5qt/pexels-photo-135130.jpeg',
     'https://dl.dropboxusercontent.com/s/6xinfm0lcnbirb9/pexels-photo-167300.jpeg',
     'https://dl.dropboxusercontent.com/s/2dp2hli32h9p0y6/pexels-photo-167921.jpeg',
     'https://dl.dropboxusercontent.com/s/fjb1m3grcrceqo2/pexels-photo-173125.jpeg',
     'https://dl.dropboxusercontent.com/s/56u8p4oplagc4bp/pexels-photo-185934.jpeg',
     'https://dl.dropboxusercontent.com/s/2s1x7wz4sdvxssr/pexels-photo-192454.jpeg',
     'https://dl.dropboxusercontent.com/s/1gjphqnllzm10hh/pexels-photo-193038.jpeg',
     'https://dl.dropboxusercontent.com/s/pcjz40c8pxpy057/pexels-photo-193043.jpeg',
     'https://dl.dropboxusercontent.com/s/hokdfk7y8zmwe96/pexels-photo-207962.jpeg',
     'https://dl.dropboxusercontent.com/s/k2tk2co7r18juy7/pexels-photo-247917.jpeg',
     'https://dl.dropboxusercontent.com/s/m4xjekvqk4rksbx/pexels-photo-247932.jpeg',
     'https://dl.dropboxusercontent.com/s/znmswtwhcdbpc10/pexels-photo-265186.jpeg',
     'https://dl.dropboxusercontent.com/s/jgb6n4esquhh4gu/pexels-photo-302899.jpeg',
     'https://dl.dropboxusercontent.com/s/rjuggi2ubc1b3bk/pexels-photo-317156.jpeg',
     'https://dl.dropboxusercontent.com/s/cpaog2nwplilrz9/pexels-photo-317383.jpeg',
     'https://dl.dropboxusercontent.com/s/16x2b6ruk18gji5/pexels-photo-320007.jpeg',
     'https://dl.dropboxusercontent.com/s/xqzqzjkcwl52en0/pexels-photo-322207.jpeg',
     'https://dl.dropboxusercontent.com/s/frclthpd7t8exma/pexels-photo-323503.jpeg',
     'https://dl.dropboxusercontent.com/s/7ixez07vnc3jeyg/pexels-photo-324030.jpeg',
     'https://dl.dropboxusercontent.com/s/1xlgrfy861nyhox/pexels-photo-324655.jpeg',
     'https://dl.dropboxusercontent.com/s/v1b03d940lop05d/pexels-photo-324658.jpeg',
     'https://dl.dropboxusercontent.com/s/ehrm5clkucbhvi4/pexels-photo-325520.jpeg',
     'https://dl.dropboxusercontent.com/s/l7ga4ea98hfl49b/pexels-photo-333529.jpeg',
     'https://dl.dropboxusercontent.com/s/rleff9tx000k19j/pexels-photo-341520.jpeg'
    ]

def test_image_init():
    '''
    Test init for Img class
    '''
    test_data_path = 'test_data_path'
    assert not os.path.exists(test_data_path), \
    f'{test_data_path} should not exists'

    img = Img(test_data_path)
    assert img.input_dir == test_data_path + os.path.sep +'incoming', \
    f'{img.input_dir} should match'
    assert img.output_dir == test_data_path + os.path.sep +'outgoing', \
    f'{img.output_dir} should match'
    
    # Clear test dirs
    shutil.rmtree(test_data_path)
    assert not os.path.exists(test_data_path), 'Test file should be deleted'

    img_default = Img()
    assert img_default.input_dir == './data/' + os.path.sep +'incoming', \
    f'{img.input_dir} should match'
    assert img_default.output_dir == './data/' + os.path.sep +'outgoing', \
    f'{img.output_dir} should match'

    # Clear test files
    shutil.rmtree(img_default.input_dir)
    shutil.rmtree(img_default.output_dir)
    assert not os.path.exists(img_default.input_dir), 'Test file should be deleted'
    assert not os.path.exists(img_default.input_dir), 'Test file should be deleted'

def test_image_down():
    '''
    Test download_images for Img class
    '''
    test_img = Img()
    assert os.path.isdir(test_img.input_dir), f'Is {test_img.input_dir} dir?'
    assert os.path.isdir(test_img.output_dir), f'Is {test_img.output_dir} dir?'
    assert os.listdir(test_img.input_dir) == [], \
    f'{test_img.input_dir} should be empty'
    assert os.listdir(test_img.output_dir) == [], \
    f'{test_img.output_dir} should be empty'
    
    test_img.download_images(IMG_URLS)
    assert len(os.listdir(test_img.input_dir)) == len(IMG_URLS), \
    f'After downloading, {test_img.input_dir} should have images'

    # Clear test files
    shutil.rmtree(test_img.input_dir)
    shutil.rmtree(test_img.output_dir)
    assert not os.path.exists(test_img.input_dir), 'Test file should be deleted'
    assert not os.path.exists(test_img.output_dir), 'Test file should be deleted'
