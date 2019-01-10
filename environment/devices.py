class Device:
    def __init__(self, device_type, device_object):
        self.type = device_type
        self.object = device_object

class TankMotor:
    def __init__(self, device_object):
        self.tank_motor = device_object.object
        self.action_function = lambda action: self.tank_motor.on(*action)
        self.stop_action_function = lambda: self.tank_motor.stop()
        self.reset_action_function = lambda: self.tank_motor.reset()