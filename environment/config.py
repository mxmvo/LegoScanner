from .devices import TankMotor, LargeMotor

SYSTEM_CONFIG = {
    'get_state_mode': 'dict' # list or dict
}

DEVICES_CONFIG = {
    'sensors':{
        'bot': ('large_motor', 'outA'),
        'top': ('large_motor', 'outB'),
        #'ts1': ('touch_sensor', 'in1'),
        #'ts2': ('touch_sensor', 'in2'),
        'cs': ('color_sensor', 'in4')
    },
    'actionables':{
        #'tm': ('tank_motor', ('outA', 'outB'))
        'bot': ('large_motor', 'outA'),
        'top': ('large_motor', 'outB')
    }
}

OBJECTS_CONFIG = {
    'sensors': 'EnvSensor',
    'actionables': 'EnvActionable'
}

SENSORS_CONFIG = {
    'large_motor': ['position'],
    'touch_sensor': ['is_pressed'],
    'color_sensor': ['raw']
}

ACTIONABLES_CONFIG = {
    #'tank_motor': (lambda device_object: TankMotor(device_object), [(-2,-2), (2,2), (-3,3), (3,-3)], (0,0)),
    'large_motor': (lambda device_object: LargeMotor(device_object), [-14, -12, -10, -8, 8, 10, 12, 14], 0),
    #'large_motor.bot': (lambda device_object: LargeMotor(device_object), [-20,-10,10,20], (0,0))

}

ENVIRONMENT_CONFIG ={
    'free_cycle' : 5
}