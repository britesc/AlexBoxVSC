from machine import ADC
import gc
import gui.includes.inc_gui_display as gui

temp_sensor = ADC(4)

# Menu screens_1001.py
# Display Internal Temperature

""" Create and Display Internal Temperature. """
def display_internal_temperature():
    gc.enable()
    val=0
    gui.display_boxes(0,255,255,"c","System Temp","cpu_temp.565")
    
    gui.display.upscaled_text(5,55, "The internal CPU",gui.display.color(0,255,255),upscaling=2)
    gui.display.upscaled_text(5,86, "Temperature is:",gui.display.color(0,255,255),upscaling=2)    

    # Reading and printing the internal temperature
    temperatureC = round(read_internal_temperature(), 2)
    temperatureF = round(celsius_to_fahrenheit(temperatureC), 2)
    
    outC = f"Celsius:    {temperatureC}"
    gui.display.upscaled_text(5,117, outC,gui.display.color(0,255,255),upscaling=2)
    outF = f"Fahrenheit: {temperatureF}"
    gui.display.upscaled_text(5,148, outF,gui.display.color(0,255,255),upscaling=2)
    gui.display.rect(60,180,200,40,gui.display.color(0,255,255),False)

#     gui.display.upscaled_text(145,195, "OK",gui.display.color(0,0,255),upscaling=2)
    
    if temperatureC < 0:
        val = 20 - (temperatureC * -1) 
    else:
        val = 20 + temperatureC
 
    per = int((val * 0.95))
    pix = int(per * 1.85)
#     print(f"Percentage: {per}")
    gui.display.rect(66,185,pix,30,gui.display.color(0,255,0),True)
    
    if per >= 90:
        gui.display.upscaled_text(120,195, "Too Hot",gui.display.color(0,0,255),upscaling=2)
    elif per >= 80:
        gui.display.upscaled_text(120,195, "Warning",gui.display.color(0,0,255),upscaling=2)
    elif per <= 50:
        gui.display.upscaled_text(145,195, "OK",gui.display.color(0,0,255),upscaling=2)
    elif per <= 10:
        gui.display.upscaled_text(118,195, "Too Cold",gui.display.color(0,0,255),upscaling=2)
    else:
        gui.display.upscaled_text(121,195, "Error",gui.display.color(0,0,255),upscaling=2)

    gc.collect()
    if gui.backlight.value() == False:
        gui.backlight.on()
        
def read_internal_temperature():
    # Read the raw ADC value
    adc_value = temp_sensor.read_u16()

    # Convert ADC value to voltage
    voltage = adc_value * (3.3 / 65535.0)

    # Temperature calculation based on sensor characteristics
    temperature_celsius = 27 - (voltage - 0.706) / 0.001721

    return temperature_celsius

def celsius_to_fahrenheit(temp_celsius): 
    temp_fahrenheit = temp_celsius * (9/5) + 32 
    return temp_fahrenheit        

if __name__ == "__main__":
    display_internal_temperature()        