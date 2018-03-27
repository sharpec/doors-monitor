#!/bin/bash
ps ax |grep -v grep |grep tex_gialla.py >  /dev/null
if [[ $? -ne 0 ]] ; then
        echo "Restarting Gialla:     $(date)" >> /var/log/porte.txt
        sudo python /home/pi/tex_gialla.py &
fi

ps ax |grep -v grep |grep tex_pedonale.py >  /dev/null
if [[ $? -ne 0 ]] ; then
        echo "Restarting Pedonale:   $(date)" >> /var/log/porte.txt
        sudo python /home/pi/tex_pedonale.py &
fi

ps ax |grep -v grep |grep tex_led.py >  /dev/null
if [[ $? -ne 0 ]] ; then
        echo "Restarting Led:        $(date)" >> /var/log/porte.txt
        sudo python /home/pi/tex_led.py &
fi
