# Display Modes

A detailed database of tested display modes of various GPUs.

This project aims to document maximum supported display modes of GPUs,
as well as weird edge cases like NVIDIA GTX 770 unable to output 1440p natively via HDMI port.

GPU vendor documentation is always vague
and does not account for modern features like HDR and stream compression,
so instead of keeping results of my testing in a private stash
i've built a simple frontend for public use.

## Monitors used for testing

As of writing this section, i have a fleet of machines with different GPUs to test with a couple displays whose native modes usually exceed GPU output capabilities.
My goal is to eventually document actual capabilities and edge cases of every GPU in my possession.

- HDMI
  - [Samsung QN75C](https://www.rtings.com/tv/reviews/samsung/qn85c-qn85cd-qled) (4K 120hz, HDR, FreeSync Premium)
  - [LG 27GN800](https://www.lg.com/us/monitors/lg-27gn800-b-gaming-monitor) (1440p 144hz, HDR, G-Sync Compatible)
  - [ROG Strix XG17](https://rog.asus.com/us/monitors/below-23-inches/rog-strix-xg17ahpe-model/spec/) (1080p 240hz, SDR, FreeSync Premium)
- DisplayPort
  - [LG 27GN800](https://www.lg.com/us/monitors/lg-27gn800-b-gaming-monitor) (1440p 144hz, HDR, G-Sync Compatible)
- USB-C
  - [ROG Strix XG17](https://rog.asus.com/us/monitors/below-23-inches/rog-strix-xg17ahpe-model/spec/) (1080p 240hz, SDR, FreeSync Premium)
- VGA
  - [Dell P1130](https://icecat.biz/en/p/dell/200-23385/monitors+crt-p1130-4702527.html) (2048 x 1536 @ 80hz, 1600x1200 @ 85hz, 1280x1024 @ 85hz)
  - [LG 775FT](https://www.manualslib.com/manual/769275/Lg-Flatron-775ft.html?page=18#manual) (1280x1024 @ 60hz, 1024x768 @ 85hz, 800x600 @ 100hz)

## Project supporters

- waywern2012 (provided LG 27GN800 monitor)

## Development environment

Install requirements:
`pip install -r requirements.txt`

Rebuild JSON for frontend:
`python compile.py`

Run a HTTP server of your choice, e.g. [Five Server for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=yandeu.five-server)
