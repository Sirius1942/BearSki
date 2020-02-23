#!/usr/bin/env python

import sys

if __name__ == '__main__':
    try:
        from BearSki.CommandLine import CommandLine 
    except ImportError as exc:
        raise ImportError(
            "Couldn't import BearSki. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    CommandLine(sys.argv)
