# make_server is used to create this simple python webserver
from wsgiref.simple_server import make_server

# import Raspberry Pi GPIO support into Python environment
import RPi.GPIO as GPIO
# import a sleep function from time module
from time import sleep

led1 = 10
led2 = 22
led3 = 27

but="<form method=\"get\" action=\"/on\"><button type=\"submit\">on gagz</button></form><form method=\"get\" action=\"/off\"><button type=\"submit\">off gagz</button></form><form method=\"get\" action=\"/red\"><button type=\"submit\">red</button></form><form method=\"get\" action=\"/blue\"><button type=\"submit\">blue</button></form><form method=\"get\" action=\"/green\"><button type=\"submit\">green</button></form>"

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)


def simple_app(env, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    if env["PATH_INFO"] == "/on":
        print("user asked for /on")
        GPIO.output(led1,False)
        GPIO.output(led2,False)
        GPIO.output(led3,False)
       
        return(but)

    elif env["PATH_INFO"] == "/off":
        print("user asked for /off")
        GPIO.output(led1, True)
        GPIO.output(led2, True)
        GPIO.output(led3, True)
        return(but)

    elif env["PATH_INFO"] == "/blue":
        print("user asked for /blue")
        GPIO.output(led1, True)
        GPIO.output(led2, True)
        GPIO.output(led3, False)
        return(but)

    elif env["PATH_INFO"] == "/red":
        print("user asked for /red")
        GPIO.output(led1, False)
        GPIO.output(led2, True)
        GPIO.output(led3, True)
        return(but)

    elif env["PATH_INFO"] == "/green":
        print("user asked for /green")
        GPIO.output(led1, True)
        GPIO.output(led2, False)
        GPIO.output(led3, True)
        return(but)


    else:
        GPIO.output(led1, True)
	GPIO.output(led2, True)
	GPIO.output(led3, True)
        print("user asked for something else")
        return(but)


httpd = make_server("", 8001, simple_app)
print "Serving on port 8001..."
httpd.serve_forever()
