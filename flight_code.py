'''
An example code framework. 
'''
# Import libraries
import random

# Define constants

# Function Definitions
def read_sensor():
    '''
    Reads the sensor and returns its value.
    
    Inputs:
    None
    
    Outputs:
    Sensor reading in volts
    '''
    sensor_val = random.random()
    return sensor_val

def convert_sens_to_dist(reading):
    '''
    Converts the sensor value into a real-world 

    Inputs:
    reading: the value of the sensor

    Outputs:
    dist: the corresponding distance, in cm
    '''
    print(reading)
    return None

# Flight code
print("Running flight code.")
sensor_value = read_sensor()
dist_from_object = convert_sens_to_dist(sensor_value)