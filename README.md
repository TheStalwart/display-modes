# Display Modes

A detailed database of tested display modes of various GPUs.

This project aims to document maximum supported display modes of GPUs,
as well as weird edge cases like NVIDIA GTX 770 unable to output 1440p natively via HDMI port.

GPU vendor documentation is always vague
and does not account for modern features like HDR and stream compression,
so instead of keeping results of my testing in a private stash
i've built a simple frontend for public use.

## Monitors used for testing

As of writing this section, i have a fleet of machines with different GPUs to test with a couple modern displays whose native modes usually exceed GPU output capabilities.
My goal is to eventually document actual capabilities and edge cases of every GPU in my possession.
VGA output testing with high refresh CRT monitors is a distant goal, but should be interesting.

- HDMI
  - [Samsung QN75C](https://www.rtings.com/tv/reviews/samsung/qn85c-qn85cd-qled) (4K 120hz, HDR, FreeSync Premium)
  - [LG 27GN800](https://www.lg.com/us/monitors/lg-27gn800-b-gaming-monitor) (1440p 144hz, HDR, G-Sync Compatible)
  - [ROG Strix XG17](https://rog.asus.com/us/monitors/below-23-inches/rog-strix-xg17ahpe-model/spec/) (1080p 240hz, SDR, FreeSync Premium)
- DisplayPort
  - [LG 27GN800](https://www.lg.com/us/monitors/lg-27gn800-b-gaming-monitor) (1440p 144hz, HDR, G-Sync Compatible)
- USB-C
  - [ROG Strix XG17](https://rog.asus.com/us/monitors/below-23-inches/rog-strix-xg17ahpe-model/spec/) (1080p 240hz, SDR, FreeSync Premium)

## Project supporters

- waywern2012 (provided LG 27GN800 monitor)

## Development environment

Install requirements:
`pip install -r requirements.txt`

Rebuild JSON for frontend:
`python compile.py`

Run a HTTP server of your choice, e.g. [Five Server for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=yandeu.five-server)
