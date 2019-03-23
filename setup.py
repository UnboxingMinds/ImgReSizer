# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["requests>=2", "Pillow>=5.4", "imagesize>=1.1"]

setup(
    name="imgresizer",
    version="0.0.1",
    author="Tumurtogtokh Davaakhuu",
    author_email="tumurtogtokh@gmail.com",
    description="A package to re-size images",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/UnboxingMinds/ImgReSizer",
    packages=find_packages(),
    install_requires = requirements,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    include_package_data = True,
    entry_points={
        "console_scripts":[
            "imgresizer=imgresizer.__main__:main",
        ]
    },
)