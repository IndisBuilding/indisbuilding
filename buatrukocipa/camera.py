import picamera
import emailgambar
from time import sleep
from emailgambar import email
camera = picamera.PiCamera()

#a = raw_input("Take Picture? y/n")
#ask = str(a)
qual= "10"
res_x = "640"
res_y = "480"

camera.resolution = (int(res_x), int(res_y))
camera.framerate = 30
sleep(2)
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g
camera.hflip = True
camera.vflip = True
camera.capture('image1.jpg')
#print "Berhasil mengambil foto..."
camera.close()
email()
#print "Berhasil mengunggah foto."
