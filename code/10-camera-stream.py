import socket
import subprocess
import picamera
from time import sleep

# Start server
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)
print "video server started"
print "use vlc player with url --> tcp/h264://ip_address:8000"

# Set duration
duration = 60

# Accept connection
connection, addr = server_socket.accept()
stream = connection.makefile('wb')
print "new connection from", addr[0]

# Set up camera module
camera = picamera.PiCamera()
print "camera ready"

camera.resolution = (640, 480)
camera.framerate = 25

try:
	camera.start_recording(stream, format='h264')
	print "start streaming for ", duration, " sec."
	camera.wait_recording(duration)
	camera.stop_recording()

finally:
	connection.close()
	server_socket.close()
print "connection closed successfully"

