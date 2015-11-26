import serial
import time

com = serial.Serial('COM17', 9600);
time.sleep(2)

com.write('-1')
print 'The LED is ', com.readline()

while True:
	print '>',
	n = raw_input();
	if n == 'exit':
		break
	com.write(n)
	print 'Arduino said : ', com.readline()

print 'All done !'
com.close()
