from flask import Flask, request, render_template
import serial
import time

app = Flask(__name__)
com = serial.Serial('COM17', 9600)
time.sleep(2)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/on')
def on():
	com.write('1')
	return com.readline()
	#return 'on'

@app.route('/off')
def off():
	com.write('0')
	return com.readline()
	#return 'off'

@app.route('/status')
def status():
	com.write('-1')
	return com.readline()
	#return 'status'

if __name__ == '__main__':
	app.run('0.0.0.0')
