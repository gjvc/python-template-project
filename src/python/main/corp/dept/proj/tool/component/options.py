#! /usr/bin/env python

import sys

import optparse


class OptionParser( object ):

    def __init__( self, prog=sys.argv[ 0 ] ):
        self._parser = optparse.OptionParser( prog=prog )


    @property
    def parser( self ):
        return self._parser


    def parse( self ):

        self.parser.add_option( '--verbose', action='store_true',   default=False )
        self.parser.add_option( '--debug',   action='store_true',   default=False )
        options, args = self.parser.parse_args()

        return options, args

