# Photostreamer for the Raspberry Pi

[![CircleCI branch](https://img.shields.io/circleci/project/achavez/photostreamer-pi/rewrite.svg)](https://circleci.com/gh/achavez/photostreamer-pi) [![Codecov](https://img.shields.io/codecov/c/github/achavez/photostreamer-pi/rewrite.svg)](https://codecov.io/github/achavez/photostreamer-pi?ref=rewrite) [![Requires.io](https://img.shields.io/requires/github/achavez/photostreamer-pi/rewrite.svg)]()

This branch is a top-to-bottom rewrite of the original photostreamer-pi application, using Django and a proper job queue to handle uploads instead of the previous patchwork of custom code. It will also include an admin that can be used to update settings and allow photographers additional control over what is sent back to photostreamer-server.

Unlike the original version, this version will also have complete test coverage and use Python 3.

### Hardware

This is the hardware we use and recommend.  There are many other options, but we have not tested them and can't vouch for their suitability for this use.

##### Project Board

The photostreamer-pi application runs on the Raspberry Pi.  Best results are achieved with the [Raspberry Pi 2 Model B.](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/)

##### Case
The Pi needs a case to protect it while being used in the field.  Several models are available; we use [this slim case enclosure from GeauxRobot.](http://www.amazon.com/gp/product/B00NH8NU3Q?psc=1&redirect=true&ref_=oh_aui_detailpage_o00_s05) It requires assembly, but once built it's easy to open and it fits well with the battery we recommend.

##### WiFi
Photostreamer connects to the Internet via WiFi

