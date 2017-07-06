import serial
import re
ser = serial.Serial("/dev/ttyAMA0",38400)
buf = ser.read(ser.inWaiting())
print 'lala'
print buf
##buf = ser.read(ser.inWaiting()).split('/n')
##for line in buf:
##    print(line)
##    pattern = re.compile(line)
##    match = pattern.match('GNRMC')
##    print(match)
##    if match:
##	print("find")
##        print (data[3],data[5])
