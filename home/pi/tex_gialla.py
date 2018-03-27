import os
import urllib2
import time
import datetime
import RPi.GPIO as io
import MySQLdb
import math
from math import floor
from time import sleep
io.setmode(io.BCM)

door_sensor = 19
sensorTrigger = True
start_time = 0
end_time = 0
elapsed_time = 0
io.setup(door_sensor, io.IN, pull_up_down=io.PUD_UP)

# function for the door opening
def door_open():
    print("Door Open")
    db = MySQLdb.connect(host='192.168.1.3',db='porte',user='porte',passwd='porte' )
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql="INSERT INTO `porte`.`log` (`id`, `nome`, `orario`, `stato`) VALUES (NULL, 'gialla20', CURRENT_TIMESTAMP, '1');"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

def door_close():
    print("Door Close")
    db = MySQLdb.connect(host='192.168.1.3',db='porte',user='porte',passwd='porte' )
    cursor = db.cursor()
    time_sensor = time.time()
    # Prepare SQL query to INSERT a record into the database.
    sql="INSERT INTO `porte`.`log` (`id`, `nome`, `orario`, `stato`) VALUES (NULL, 'gialla20', CURRENT_TIMESTAMP, '0');"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()
def verifica(elapsed_time):
    print ("verifica")
    if elapsed_time > 120.0:
        os.system("sudo /home/pi/mail-time.sh")
        urllib2.urlopen("http://192.168.1.173/gpio.php?on=ON").close
        sleep(10)
        urllib2.urlopen("http://192.168.1.173/gpio.php?off=OFF").close
    else: print(elapsed_time, "secondi")

while True:
    time.sleep(0.2)
    if io.input(door_sensor): # if door is opened
        if (sensorTrigger):
            door_open() # fire GA code
            start_time = datetime.datetime.now()
            print(start_time)
        sensorTrigger = False # make sure it doesn't fire again
    if not io.input(door_sensor): # if door is closed
        if not (sensorTrigger):
            door_close() # fire GA code
            end_time = datetime.datetime.now()
            print(end_time)
            elapsed_time = math.floor((end_time - start_time).seconds)
            print(elapsed_time)
            verifica(elapsed_time)
        sensorTrigger = True # make sure it doesn't fire again
