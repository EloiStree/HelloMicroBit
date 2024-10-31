from microbit import *
import music

int_press_count =0
bool_a_pressing =False
bool_b_pressing =False
bool_touch_logo_pressing =False
bool_touch_0_pressing =False
bool_touch_1_pressing =False
bool_touch_2_pressing =False


while True:

    bool_a_pressing = button_a.is_pressed()
    bool_b_pressing = button_b.is_pressed()
    bool_touch_logo_pressing = pin_logo.is_touched()
    bool_touch_0_pressing = pin0.is_touched()
    bool_touch_1_pressing = pin1.is_touched()
    bool_touch_2_pressing = pin2.is_touched()
    
    byte_light_level_255 = display.read_light_level()
    byte_light_level_9 = (byte_light_level_255/255.0)*9.0

    byte_temperature_level_55 = temperature()
    byte_temperature_level_9 = ((byte_temperature_level_55+5)/55)*9.0
    int_compass_360 = compass.heading()
    byte_compass_9 =(int_compass_360/360.0)*9.0

    int_microphone_255 = microphone.sound_level()
    byte_microphone_9 = (int_microphone_255/255.0)*9.0
    
    if bool_a_pressing:
        display.set_pixel(0,0,9)
    else:
        display.set_pixel(0,0,0)
    if bool_b_pressing:
        display.set_pixel(1,0,9)
    else:
        display.set_pixel(1,0,0)

    if bool_touch_0_pressing:
        display.set_pixel(0,1,9)
    else:
        display.set_pixel(0,1,0)
    if bool_touch_1_pressing:
        display.set_pixel(1,1,9)
    else:
        display.set_pixel(1,1,0)
    if bool_touch_2_pressing:
        display.set_pixel(2,1,9)
    else:
        display.set_pixel(2,1,0)
    if bool_touch_logo_pressing:
        display.set_pixel(3,1,9)
    else:
        display.set_pixel(3,1,0)
        
    # https://python.microbit.org/v/3/reference/light-level
    display.set_pixel(0,4,int(byte_light_level_9))
    # https://python.microbit.org/v/3/reference/temperature
    display.set_pixel(1,4,int(byte_temperature_level_9))
    # https://python.microbit.org/v/3/reference/compass
    display.set_pixel(2,4,int(byte_compass_9))
    #https://python.microbit.org/v/3/reference/microphone
    display.set_pixel(3,4,int(byte_microphone_9))

    if False and pin_logo.is_touched():
            display.show(Image('00300:'
                               '03630:'
                               '36963:'
                               '03630:'
                               '00300'))
            sleep(1000)
            display.clear()
        
    
