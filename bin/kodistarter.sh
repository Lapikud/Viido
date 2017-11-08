#!/bin/bash
echo "Kodi starter"
while true;do
    echo -e "HTTP/1.0 201 No Content\n\r\n\r" | nc -l 127.0.0.1 6969 > /dev/null
    if [[ -z "$(ps aux | grep /usr/bin/kodi | grep -v grep)" ]]; then
        echo "Starting kodi"
        kodi &
    else
        echo "Kodi is already running"
    fi
done
