# doors-monitor
Monitor open/close doors with an raspberry p3 with magnetic contact and/or relays

* Download and install raspbian on SD Card
* Configure wifi o network
* Update / dist-upgrade
* sudo apt-get install python-gpiozero python-pkg-resources python-mysqldb
* git clone git://git.drogon.net/wiringPi // cd wiringPi/ // ./build
* sudo crontab -e -> insert */1 * * * * sudo /home/pi/tex_check.sh
* In raspi-config Enable autologin console

# fix indent error
expand -t 4 script.py > fixed_script.py

# mail alert when open doors

* sudo apt-get install ssmtp mailutils
* edit /etc/ssmtp/ssmtp.conf and /etc/ssmtp/revaliases
