#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (IndexError, ValueError, ZeroDivisionError, TypeError) as e:
        sys.stderr.write(f"Exception: {e}\n".format(e))
        return None
