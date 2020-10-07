#! /usr/bin/env python

import sys

from .app import ExampleComponentApplication


def main():
    return ExampleComponentApplication().main()


if __name__ == '__main__':
    sys.exit( main() )

