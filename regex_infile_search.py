#!/usr/bin/python

import argparse
import os
import sys
import re


class printColor:
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'


parser = argparse.ArgumentParser(
    description='Search regex in input file. All match results will be stored in files [--name]*.rgxprslt')

parser.add_argument('-i', '--input', metavar='',
                    help='input file with content, where to search')
parser.add_argument('-r', '--regex', metavar='', help='regular expression')
parser.add_argument('-n', '--name', metavar='', help='name of search results')

args = parser.parse_args()

inputFile = args.input
regex = args.regex
name = args.name

if inputFile is None:
    print "-i, --input" + printColor.RED + \
        "     input file path is not defined" + printColor.END
    sys.exit(1)

if regex is None:
    print "-r, --regex" + printColor.RED + \
        "     regular expression is not defined" + printColor.END
    sys.exit(1)

if name is None:
    print "-n, --name" + printColor.RED + \
        "     regular expression is not defined" + printColor.END
    sys.exit(1)

if os.path.exists(inputFile) == False:
    print printColor.RED + \
        "File {} was not found".format(
            os.path.abspath(inputFile)) + printColor.END
    sys.exit(1)

file = open(inputFile, "r")
content = file.read()

print "Searching {} in {}".format(regex, os.path.abspath(inputFile))

matches = re.findall(regex, content)

if not matches:
    print "No matches found."
    sys.exit(0)

print "Regex search finished " + printColor.GREEN + "successfully" + printColor.END + \
    " with results:"

for i in range(0, len(matches)):
    outputFile = "{}{}.rgxprslt".format(name, i)
    result = open(outputFile, "w")
    result.write(matches[i])
    result.close()
    print printColor.BLUE + \
        "{}".format(os.path.abspath(outputFile)) + printColor.END

sys.exit(0)
