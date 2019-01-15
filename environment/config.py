from .devices import TankMotor

ENVIRONMENT_CONFIG = {
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
        'tm': ('tank_motor', ('outA', 'outB'))
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
    'tank_motor': (lambda device_object: TankMotor(device_object), [(-2,-2), (2,2), (-3,3), (3,-3)], (0,0))
}