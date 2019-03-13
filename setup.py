# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["requests>=2", "Pillow>=5.4", "imagesize>=1.1"]
# with open("requirements.txt") as req_files:
    # requirements = req_files.read().splitlines()

setup(
    name="ImgReSizer",
    version="0.0.1",
    author="Tumurtogtokh Davaakhuu",
    author_email="tumurtogtokh@gmail.com",
    description="A package to re-size images",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/UnboxingMinds/ImgReSizer",
    packages=find_packages(),
    # install_requires=parse_requirements('requirements.txt', session='hack'),
    install_requires = requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: MIT License",
    ],
)