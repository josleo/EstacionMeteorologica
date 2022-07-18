# Set up BCM GPIO numbering.
GPIO.setmode(GPIO.BCM)
# Set up input pins.
SENSOR_1_INPUT = 18
GPIO.setup(SENSOR_1_INPUT, GPIO.IN)

# Initiate the loop.
while True:
    # Get signals from Arduino as digital input values.
    SENSOR_1_VALUE = GPIO.input(SENSOR_1_INPUT)
    # Print values.
    print (SENSOR_1_VALUE)
    sleep(1)

