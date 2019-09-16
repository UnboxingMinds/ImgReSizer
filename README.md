[![Coverage Status](https://coveralls.io/repos/github/UnboxingMinds/ImgReSizer/badge.svg?branch=master)](https://coveralls.io/github/UnboxingMinds/ImgReSizer?branch=master)

# Image ReSizer
This simple package re-sizes images from a given list of urls.

## Installation

`pip install imgresizer`

## Usage
It expects you to pass ita configuration as command line parameter. \
`imgresizer -c <path/to/conf_json>`

A sample json:

```json
{
    "targets": [
        400,
        200,
        100
    ],
    "data": "data",
    "num_threads": 8,
    "input_dir": "incoming",
    "output_dir" : "outgoing",
    "image_urls" : "/path/to/urls.txt"
}
```
Firstly, it downloads them and stores them inside **data/input_dir** directory. Then it starts processing images to re-size and store re-sized image to **data/output_dir** with its new size added to its name.

Additionally, you can pass `-l true` so that it logs the process.

## Issues
Nothing yet. But it will need to speed up.

## Tasks
- [ ] Implement thread pooling
- [ ] Make it re-size local images

## License
ImgReSizer is released under the [MIT license] (https://choosealicense.com/licenses/mit/#)
