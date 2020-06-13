#! /usr/bin/env python

import sys
import argparse

from .app import ExampleComponentApplication


def main():
    parser = argparse.ArgumentParser( 'ExampleComponent' )
    parser.add_argument( '--version', type=bool, default=False )
    options = parser.parse_args()
    return ExampleComponentApplication().main()


if __name__ == '__main__':
    sys.exit( main() )

