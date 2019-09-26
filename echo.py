#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Ethan375"


import sys
import argparse
import subprocess


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(description="Perform transformation on input text.")
    parser.add_argument('text', help="text to be manipulated")
    parser.add_argument('-u', "--upper", action="store_true", help="convert text to uppercase")
    parser.add_argument('-l', "--lower", action="store_true", help="convert text to lowercase")
    parser.add_argument('-t', "--title", action="store_true", help="convert text to titlecase")

    args = parser.parse_args()

    main(args)


def main(args):
    """Implementation of echo"""
    echo_string = args.text

    if args.lower:
        echo_string = echo_string.lower()
    elif args.upper:
        echo_string = echo_string.upper()
    elif args.title:
        echo_string = echo_string.title()

    
    subprocess.call(['echo', echo_string])

if __name__ == '__main__':
    create_parser()
