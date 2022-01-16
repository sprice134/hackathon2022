import time
import spidev
import random
import time
from twilio.rest import Client

account_sid = 'ACc9a0b8e191c56b877a2fdbd764240edf'
auth_token = 'afa2fc0421e2659a1c300f84f5ce9343'
stephen_num = '+14252312254'
porto_num = '+16035609830'
sending_number = "+18305297727"
cont = True
fakeText = False
lowerThresh = 1.9
upperThresh = 3
watered = False

def getVoltage():
    return random.randint(0, 100)/100

def sendText(sender, receiver, message):
    #account_sid = os.environ['ACc9a0b8e191c56b877a2fdbd764240edf']
    #auth_token = os.environ['25656f4ce141a376cfd1466343e8a80f']
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
                    sendText(sending_number, stephen_num, "The plant is dry, it has been watered")
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
                    sendText(sending_number, stephen_num, "\nYour plant is dry, it needs water!\n Previous watering: " + str(last_water) + 'Love, Bob')
                    fakeText = True
        elif v < upperThresh:
            watered = False
        else:
            print("Plant doesn't need water at this time")
        time.sleep(10)
    '''while True:
        adc_0 = read_adc(0)
        adc_1 = read_adc(1)
        print('Voltage: ' + str(round(adc_0, 2)))
        #print("Ch 0:", round(adc_0, 2), "V Ch 1:", round(adc_1, 2), "V")
        time.sleep(1)'''

finally:
    spi.close()
    GPIO.cleanup()
