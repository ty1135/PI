import RPi.GPIO as GPIO


class Servo(object):
    def __init__(self, pins):
        self.pins = pins
        self.left_pins = pins[2:]
        self.right_pins = pins[:2]

        self._setup()

        self.steering_wheel = SteeringWheel(self)

    def _setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

    def turn_off(self):
        GPIO.cleanup(self.pins)




class SteeringWheel(object):
    def __init__(self, servo):
        self.servo = servo

    def forward(self):
        self._side_forward(self.servo.left_pins)
        self._side_forward(self.servo.right_pins)

    def left_forward(self):
        self._side_forward(self.servo.right_pins)
        self._side_stop(self.servo.left_pins)

    def right_forward(self):
        self._side_forward(self.servo.left_pins)
        self._side_stop(self.servo.right_pins)

    def backward(self):
        self._side_backward(self.servo.left_pins)
        self._side_backward(self.servo.right_pins)

    def left_backward(self):
        self._side_stop(self.servo.left_pins)
        self._side_backward(self.servo.right_pins)

    def right_backward(self):
        self._side_stop(self.servo.right_pins)
        self._side_backward(self.servo.left_pins)

    def stop(self):
        self._side_stop(self.servo.left_pins)
        self._side_stop(self.servo.right_pins)

    @staticmethod
    def _side_forward(pins):
        a, b = pins
        GPIO.output(a, True)
        GPIO.output(b, False)

    @staticmethod
    def _side_backward(pins):
        a, b = pins
        GPIO.output(a, False)
        GPIO.output(b, True)

    @staticmethod
    def _side_stop(pins):
        a, b = pins
        GPIO.output(a, False)
        GPIO.output(b, False)



if __name__ == "__main__":
    import time


    print("...")

    servo = Servo([32, 36, 38, 40])
    servo.steering_wheel.left_forward()

    time.sleep(3)
    servo.turn_off()

