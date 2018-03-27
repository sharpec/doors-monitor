# doors-monitor
Monitor open/close doors with an raspberry p3 with magnetic contact and/or relays

# Install Raspbian
Download and install raspbian on SD Card

# Configure wifi o network
sudo iwlist wlan0 scan
nano /etc/wpa_supplicant/wpa_supplicant.conf

``(country=IT

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev

update_config=1

network={

    ssid="YOURSSID"
    
    psk="yourpassword"
    
})``

# Update

sudo apt-get update && sudo apt-get dist-upgrade && sudo apt-get autoremove && sudo apt-get clean

# In raspi-config

Enable autologin console

nano .bashrc

if [ $(tty) == /dev/tty1 ]; then
/home/pi/autostart.sh
fi


