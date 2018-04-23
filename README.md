# servopi

This Python module allows a user to use the Parallax Propeller Servo Controller.

### Usage

Example of basic usage:

```python
import servopi

# Let's assume the controller is connected to a USB port named '/dev/ttyUSB0' in Linux
# A context manager safely closes the serial device when finished
with servopi.controller('/dev/ttyUSB0') as controller:
	
	# Move servo 1 to position 1100 over a 0.23 second duration
	controller.move(servo.ONE, 1100, 0.23)
	
	# Move servo 2 to position 580 over a 0.33 second duration
	controller.move(servo.ONE, 580, 0.33)
```

A full demonstration is also included in the project:

```python
import servopi.demo

# Let's assume the controller is connected to a USB port named '/dev/ttyUSB0' in Windows
servopi.demo.run_demo('/dev/ttyUSB0')
```

### Documentation

There is no official documentation for servopi, however the python [source code](servopi/__init__.py) is small and well documented. The code is based off of the serial protocol documentation for the [Parallax Propeller Servo Controller](https://www.parallax.com/downloads/propeller-servo-controller-guide). Consult also the source code of the [demo program](servopi/demo/__init__.py) for a more detailed usage example.

### Dependencies

This pure-python module works in Python 3.x and legacy Python 2.x. It has been tested in Windows 7, OS X and Linux (Raspbian).

Requires [pySerial](https://github.com/pyserial/pyserial). Windows users will need to install [drivers for the Propeller](https://www.parallax.com/usbdrivers).

### Installation

Run the following in the terminal:

```
python setup.py install
```

### License

Released under the [MIT license](LICENSE).
