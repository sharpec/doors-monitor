import os
import urllib2
import time
import RPi.GPIO as io
import MySQLdb
import threading
io.setmode(io.BCM)

door_sensor = 16
sensorTrigger = True

io.setup(door_sensor, io.IN, pull_up_down=io.PUD_UP)

#def timer():
#  threading.Timer(30.0, timer).start()
#  urllib2.urlopen("http://192.168.1.173/gpio.php?off=OFF").close
  #print("Ciao mondo!")
#timer()

#def hello():
#    urllib2.urlopen("http://192.168.1.173/gpio.php?off=OFF").close
#    return

# function for the door opening
def door_open():
    print("Door Open")
#    urllib2.urlopen("http://192.168.1.173/gpio.php?on=ON").close
    db = MySQLdb.connect(host='192.168.1.3',db='porte',user='porte',passwd='porte' )
    cursor = db.cursor()
    time_sensor = time.time()
    # Prepare SQL query to INSERT a record into the database.
    sql="INSERT INTO `porte`.`log` (`id`, `nome`, `orario`, `stato`) VALUES (NULL, 'pedonale20', CURRENT_TIMESTAMP, '1');"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()
#    t = threading.Timer(3.0, hello)
#    t.start()
#    time.sleep(30)
#    urllib2.urlopen("http://192.168.1.173/gpio.php?off=OFF").close

# function for the door closing
def door_close():
    print("Door Close")
#    urllib2.urlopen("http://192.168.1.173/gpio.php?off=OFF").close
    db = MySQLdb.connect(host='192.168.1.3',db='porte',user='porte',passwd='porte' )
    cursor = db.cursor()
    time_sensor = time.time()
    # Prepare SQL query to INSERT a record into the database.
    sql="INSERT INTO `porte`.`log` (`id`, `nome`, `orario`, `stato`) VALUES (NULL, 'pedonale20', CURRENT_TIMESTAMP, '0');"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

while True:
    time.sleep(0.2)
    if io.input(door_sensor): # if door is opened
        if (sensorTrigger):
            door_open() # fire GA code
            sensorTrigger = False # make sure it doesn't fire again
    if not io.input(door_sensor): # if door is closed
        if not (sensorTrigger):
            door_close() # fire GA code
            sensorTrigger = True # make sure it doesn't fire again
