# Bob: The Plant Moisture Monitor and SMS Notification System

![Bob](https://github.com/sprice134/hackathon2022/blob/main/Images/hackathon_logo.png?raw=true)

## Concept
With busy schedules due to classwork, sports, and other activities, college students tend to neglect their house plants. 

But what if there was a system that helped keep you and your plants happy?

**Bob** is here to help!

Bob is two parts: a soil moisture monitor and an SMS notification system.

When Bob measures your plant's soil and it's dry, he will text you a notification that it needs to be watered. Bob will also inform you of the last time you watered your plant.

## Objectives
1. **Measure Voltage Drop across the Soil**: A voltage divider circuit uses the varied resistance of wet and dry soil which creates a voltage drop that can be read by the Analog to Digital Converter and set to the Raspberry Pi.
2. **Interpret Voltage**: Convert analog voltages to digital inputs and interpret these numerical values to determine the watering needs of the plant.
3. **Send SMS to the user based on plant watering needs**: The SMS notification system uses Twilio to notify the user that their plant currently needs watering and the date of its most recent watering.

## Tools and Materials
| Hardware | Software | Other |
| ----------- | ----------- | ----------- |
| Digital Multimeter (DMM) | Python | Soil (testing) |
| 18 Gauge Wires | Linux environment | Potted Plant (final product) |
| Jumper Wires | **Twilio** for SMS messaging |   |
| 100 KΩ Resistor |   |   |
| MCP3002 Analog to Digital Converter (ADC) |   |   |
| Breadboard |   |   |
| Raspberry Pi |   |   |

## Challenges we ran into
1. **Resources**: There were important pieces of hardware that were difficult to find such as a DMM and an ADC.
2. **Lack of Experience with Raspberry Pi**: After some research, our group figured out how to wire the Raspberry Pi and get it to read the resistance so that it could be used in the python program.

## Accomplishments that we're proud of
- Creating a working final product
- Being resourceful and finding everything we needed on campus
- Working as an efficient and helpful team with no issues
- Combining the skills of team members with different knowledge backgrounds and skills

## What we learned
- How to use Twilio to send SMS messages in Python code
- How to wire a Raspberry Pi
- How to combine electrical engineering with computer science

## What's next for Bob
After sharing our idea with some friends that owned plants of their own, they thought the idea was great and some even said "I need that for my plants!"
Our main goal for Bob was to actually be able to water the dry plant for the user, but unfortunately, we did not have enough time to make this happen. With more time and materials, Bob would be able to transform from a moisture monitor to a full watering system. We would also turn the notification system into an app so that the user could track how often his or her plants need to get watered more easily.


![Hackathon logo](https://github.com/sprice134/hackathon2022/blob/main/Images/hackathon_logo.png?raw=true)