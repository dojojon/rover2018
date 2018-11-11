import serial
import time

# ttyACM0 for microBit board
ser = serial.Serial('/dev/ttyACM0', 115200) 

readOut = 0   #chars waiting from laser range finder

print ("Starting up")
connected = False
commandToSend = "reqTemp#" # get the distance in mm

while True:
    print ("Writing: ",  commandToSend)
    ser.write(str(commandToSend).encode())
    time.sleep(3)
    while True:
        try:
            print ("Attempt to Read")
#            readOut = ser.readline().decode('ascii')
            readOut = ser.read_until("#".encode()).decode('ascii')
            print ("Reading: ", readOut) 

            break
        except:
            pass
    print ("Restart")
    ser.flush() #flush the buffer 


