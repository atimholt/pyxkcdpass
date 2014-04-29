#!/usr/bin/python
#
# xkcdpass
# http://danielmcgraw.github.io/xkcdpass/
#
# pyxkcdpass
# https://github.com/ikkebr/xkcdpass
#
# Generate passwords like Randall Munroe (http://xkcd.com/936/)
# Default dictionary from http://www.englishclub.com/vocabulary/common-words-5000.htm
#

import os
import random
from optparse import OptionParser


usage = "xkcdpass.py [-h|--help] [-l|--length=<length>] [-d|--dictionary=<path>]"

parser = OptionParser(usage=usage)

default_dictionary = os.path.join(os.path.dirname(__file__), 'dictionary')
parser.add_option("-d", "--dictionary", dest="dictionary_path",
                  help="Specify a path to a dictionary", metavar="PATH", default=default_dictionary)

parser.add_option("-l", "--length", dest="password_length", type="int",
                  help="Specify the password length", metavar="LENGTH", default=4)


(options, args) = parser.parse_args()

if options.password_length < 1:
    parser.error("Your password should contain at least 1 word.")

if not os.path.isfile(options.dictionary_path):
    parser.error("I cannot find your dictionary file. Please make sure it is readable.")

with open(options.dictionary_path, "r") as dictionary:
    print " ".join( map(str.strip, random.sample( dictionary.readlines(), options.password_length )))
    
