import rpyc
from .devices import Device
from copy import deepcopy

class LegoConnector:
    def __init__(self, brick_ip):
        self.conn = rpyc.classic.connect(brick_ip)
        self.motor = self.conn.modules['ev3dev2.motor']
        self.sensor = self.conn.modules['ev3dev2.sensor.lego']
        # leds = conn.modules['ev3dev2.led']

    def _get_device(self, mode):
        return {
            'large_motor': lambda address: self.motor.LargeMotor(address),
            'touch_sensor': lambda address: self.sensor.TouchSensor(address),
            'color_sensor': lambda address: self.sensor.ColorSensor(address),
            'tank_motor': lambda address1, address2: self.motor.MoveTank(address1, address2)
        }[mode]

    def get_device(self, mode, address):
        # address can be a single address or 2 values
        dev = self._get_device(mode)

        if type(address) == list or type(address) == tuple:          
            return Device(mode, dev(*address))
        else:
            return Device(mode, dev(address))