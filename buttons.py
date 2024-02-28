import RPi.GPIO as GPIO
from time import sleep
from main import login_with_credentials

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button 1
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button 2
# GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button 3
# GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button 4

# Setup LED
GPIO.setup(18, GPIO.OUT)  # Processing LED

try:
    while True:
        if GPIO.input(17) == GPIO.LOW:  # Button 1 is pressed
            GPIO.output(18, GPIO.HIGH)
            login_with_credentials(1)
            sleep(0.5)  # Simple debounce
            GPIO.output(18, GPIO.LOW)

        if GPIO.input(27) == GPIO.LOW:  # Button 2 is pressed
            GPIO.output(18, GPIO.HIGH)
            login_with_credentials(2)
            sleep(0.5)  # Simple debounce
            GPIO.output(18, GPIO.LOW)
        
        # if GPIO.input(22) == GPIO.LOW:  # Button 3 is pressed
        #     GPIO.output(18, GPIO.HIGH)
        #     login_with_credentials(3)
        #     sleep(0.5)
        #     GPIO.output(18, GPIO.LOW)
        
        # if GPIO.input(23) == GPIO.LOW:  # Button 4 is pressed
        #     GPIO.output(18, GPIO.HIGH)
        #     login_with_credentials(4)
        #     sleep(0.5)
        #     GPIO.output(18, GPIO.LOW)

finally:
    GPIO.cleanup()  # Clean up GPIO on exit
