import time
import spidev
import random
import time
from twilio.rest import Client

account_sid = ''                #Fill with account ID
auth_token = ''                 #Fill with auth token
recieving_number = ''           #Fill with number you are texting    
sending_number = ''             #Fill with number assigned by twilio
cont = True
fakeText = False                #Set to true for demos or testing
lowerThresh = 1.9               #Arbitrarily set based on tests on plants
upperThresh = 3                 #Arbitrarily set based on tests on plants
watered = False

def getVoltage():
    return random.randint(0, 100)/100

def sendText(sender, receiver, message):
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body=message,
                        from_=sender,
                        to=receiver
                    )
    print(message.sid)

spi_ch = 0

# Enable SPI
spi = spidev.SpiDev(0, spi_ch)
spi.max_speed_hz = 1200000

def read_adc(adc_ch, vref = 3.3):

    # Make sure ADC channel is 0 or 1
    if adc_ch != 0:
        adc_ch = 1

    # Construct SPI message
    #  First bit (Start): Logic high (1)
    #  Second bit (SGL/DIFF): 1 to select single mode
    #  Third bit (ODD/SIGN): Select channel (0 or 1)
    #  Fourth bit (MSFB): 0 for LSB first
    #  Next 12 bits: 0 (don't care)
    msg = 0b11
    msg = ((msg << 1) + adc_ch) << 5
    msg = [msg, 0b00000000]
    reply = spi.xfer2(msg)

    # Construct single integer out of the reply (2 bytes)
    adc = 0
    for n in reply:
        adc = (adc << 8) + n

    # Last bit (0) is not part of ADC value, shift to remove it
    adc = adc >> 1

    # Calculate voltage form ADC value
    voltage = (vref * adc) / 1024

    return voltage

# Report the channel 0 and channel 1 voltages to the terminal
try:
    last_water = "Sat Jan 09 07:54:21 2022"
    while cont:
        adc_0 = read_adc(0)
        adc_1 = read_adc(1)
        v = round(adc_0, 2)
        print('Voltage: ' + str(round(adc_0, 2)))

        if v > upperThresh:
            if watered == True:
                if fakeText: 
                    print("Using Fake Texts:")
                    print("The plant is dry, it needs water")
                    print("Previous watering: " + str(last_water))
                    last_water = str(time.ctime(int(time.time())))
                    watered = True
                    print('-'*30)
                else:
                    sendText(sending_number, recieving_number, "The plant is dry, it has been watered")
                    fakeText = True
            elif watered == False:
                if fakeText: 
                    print("Using Fake Texts:")
                    print("The plant is dry, it needs water")
                    print("Previous watering: " + str(last_water))
                    last_water = str(time.ctime(int(time.time())))
                    watered = True
                    print('-'*30)
                else:
                    sendText(sending_number, recieving_number, "\nYour plant is dry, it needs water!\n Previous watering: " + str(last_water) + 'Love, Bob')
                    fakeText = True
        elif v < upperThresh:
            watered = False
        else:
            print("Plant doesn't need water at this time")
        time.sleep(10)

finally:
    spi.close()
    GPIO.cleanup()
