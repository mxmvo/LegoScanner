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

class LargeMotor:
    def __init__(self, device_object):
        self.motor = device_object.object
        self.motor.run_direct(duty_cycle_sp = 0)
        #self.stop_action_function = lambda: self.motor.stop()
        self.reset_action_function = lambda: self.motor.reset()

    def action_function(self, action):
        self.motor.duty_cycle_sp = action
        #self.action_function = lambda action: self.motor.duty_cycle_sp = action

    def stop_action_function(self):
        self.motor.duty_cycle_sp = 0
