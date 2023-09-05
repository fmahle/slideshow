#!/bin/bash
#pkill Xvfb
#Xvfb :10 -screen 0 1920x1080x24 & export DISPLAY=:10
python3 ~/slideshow/generate.py &
while true; do
    if ! pgrep firefox; then
        echo "start"
        /usr/bin/firefox --new-window --kiosk ~/slideshow/generated_slideshow.html &
    fi
    sleep 10
done
