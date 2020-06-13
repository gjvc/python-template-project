#! /usr/bin/env python

from .options import OptionParser


class ExampleComponentApplication( object ):

    def __init__( self ):
        pass


    def main( self ):
        parser = OptionParser( self.__class__.__name__ )
        options, args = parser.parse()

