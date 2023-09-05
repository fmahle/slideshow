#!/bin/bash

lftp -c "debug; open <<login-password and url>>; mirror --delete --parallel=10 --use-pget-n=5 --no-empty-dirs /html/smartpanel/austausch/images ~/slideshow/images"

python3 ~/slideshow/generate.py
