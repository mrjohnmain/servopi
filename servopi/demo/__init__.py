#!/usr/bin/env python

"""
Movement demonstration of the servo controller

Author: Tusli Software LLC (info@tuslisoftware.com), John Main (john@johnmain.co.uk)
Written: May 1, 2016
Updated: April 23, 2018

This is a demo program using the controller class. The main function is
`run_demo(port, debug)`. The motions of the controller are based on the demo VSA
software.

"""
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)
import servopi


###############################################################################
# Convenience Functions
###############################################################################

def initialize_positions(controller):
    """
    Initial starting positions of each servo.
    Shows how to use servopi.controller.set_position().

    Parameters
    ----------
    controller : servopi.controller instance

    """
    controller.set_position(controller.ONE, 880)
    controller.set_position(controller.TWO, 630)
    controller.set_position(controller.THREE, 580)
    controller.set_position(controller.FOUR, 525)
    controller.set_position(controller.FIVE, 515)
    controller.set_position(controller.SIX, 1030)
    controller.set_position(controller.SEVEN, 750)
    controller.set_position(controller.EIGHT, 750)

def rotate_to_angle(controller):
    """
    Initial starting positions of each servo.
    Shows how to use servopi.controller.set_position().

    Parameters
    ----------
    controller : servopi.controller instance

    """
    controller.rotate(controller.ONE, 90)
    controller.rotate(controller.TWO, 180)
    controller.rotate(controller.THREE, 270)
    controller.rotate(controller.FOUR, 60)
    controller.rotate(controller.FIVE, 30)
    controller.rotate(controller.SIX, 120)
    controller.rotate(controller.SEVEN, 150)
    controller.rotate(controller.EIGHT, 0)


def move_to_pulse_width(controller):
    """
    Opens and closes each finger servo individually.
    Shows how to use servopi.controller.move().

    Parameters
    ----------
    controller : servopi.controller instance

    """
    # Set the servo positions
    controller.move(controller.THREE, 1100, 0.23)
    controller.move(controller.THREE, 580, 0.33)
    controller.move(controller.FOUR, 1154, 0.23)
    controller.move(controller.FOUR, 525, 0.33)
    controller.move(controller.FIVE, 1150, 0.23)
    controller.move(controller.FIVE, 515, 0.33)
    controller.move(controller.SIX, 450, 0.23)
    controller.move(controller.SIX, 1030, 0.33)
    controller.move(controller.SEVEN, 1050, 0.23)
    controller.move(controller.SEVEN, 750, 0.33)
    controller.move(controller.EIGHT, 570, 0.23)
    controller.move(controller.EIGHT, 750, 0.33)


def bulk_move(controller):
    """
    Shows how to use servopi.controller.move() with multiple servos moving at
    once.

    Parameters
    ----------
    controller : servopi.controller instance

    """
    channels = [controller.ONE, controller.TWO, controller.THREE, controller.FOUR, controller.FIVE, controller.SIX]
    pulse_widths = [1100, 1154, 1150, 450, 1050, 570]

    controller.move(channels, pulse_widths, 0.23)




###############################################################################
# Main Function
###############################################################################

def run_demo(port, debug=False):
    """
    Runs demonstration using servopi module.

    Parameters
    ----------
    port : str
        The name of the serial port. Usually '/dev/ttyUSB0' for Linux,
        'COM3' for Windows, etc.
    debug : bool, optional
        Print debug messages.

    """
    # Initialize controller the Robot
    with servopi.controller(port, write_sleep=0.05, debug=debug) as controller:

        # Print some information about controller
        print("FW Version: " + str(controller.controller.get_fw_version_number()))

        # Run the demo movements
        initialize_positions(controller)
        rotate_to_angle(controller)
        move_to_pulse_width(controller)
        bulk_move(controller)

    print("Demo program finished.")
