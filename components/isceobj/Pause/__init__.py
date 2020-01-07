#!/usr/bin/env python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copyright: 2012 to the present, california institute of technology.
# all rights reserved. united states government sponsorship acknowledged.
# any commercial use must be negotiated with the office of technology transfer
# at the california institute of technology.
# 
# this software may be subject to u.s. export control laws. by accepting this
# software, the user agrees to comply with all applicable u.s. export laws and
# regulations. user has the responsibility to obtain export licenses,  or other
# export authority as may be required before exporting such information to
# foreign countries or providing access to foreign persons.
# 
# installation and use of this software is restricted by a license agreement
# between the licensee and the california institute of technology. it is the
# user's responsibility to abide by the terms of the license agreement.
#
# Author: Eric Gurrola
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




## pause is a raw_input wrapper
def pause(cont="go",ex="exit",ignore=False, message="", bell=True):
    """pause function.  Pauses execution awaiting input.
    Takes up to three optional arguments to set the action strings:
    cont   = first positional or named arg whose value is a string that causes execution
              to continue.
              Default cont="go"
    ex     = second positional or named arg whose value is a string that causes execution
              to stop.
              Default ex="exit"
    ignore = third positional or named arg whose value cause the pause to be ignored or
              paid attention to.
              Default False
    message = and optional one-time message to send to the user"
    bell    = True: ring the bell when pause is reached.
    """
    if not ignore:
        x = ""
        if message or bell:
            message += chr(7)*bell
            print(message)
        while x != cont:
            try:
                x = raw_input(
                    "Type %s to continue; %s to exit: " % (cont, ex)
                    )
            except KeyboardInterrupt:
                return None
            if x == ex:
                # return the "INTERUPT" system error.
                import errno
                import sys
                return sys.exit(errno.EINTR)
            pass
        pass
    return None
