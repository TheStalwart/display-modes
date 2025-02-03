# Display Modes

A detailed database of tested display modes of various GPUs.

This project aims to document maximum supported display modes of GPUs,
as well as weird edge cases like NVIDIA GTX 770 unable to output 1440p natively via HDMI port.

GPU vendor documentation is always vague
and does not account for modern features like HDR and stream compression,
so instead of keeping results of my testing in a private stash
i've built a simple frontend for public use.

## Project supporters

- waywern2012 (provided LG 27GN800 monitor)

## Development environment

Install requirements:
`pip install -r requirements.txt`

Rebuild JSON for frontend:
`python compile.py`

Run a HTTP server of your choice, e.g. [Five Server for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=yandeu.five-server)
