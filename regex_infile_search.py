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


class messages:
    NONE_INPUT = "input file path is not defined"
    NONE_REGEX = "regular expression is not defined"
    NONE_NAME = "regular expression is not defined"
    FILE_NOT_FOUND = "File {} was not found"
    SEARCHING = "Searching {} in {}"
    NO_MATCHES = "No matches found."
    FINISHED = "Regex search finished " + printColor.GREEN + \
        "successfully" + printColor.END + " with results:"
    DONE = "done"


need_print = False


def print_if_needed(string):
    if need_print:
        print string


def main(inputFile, regex, name):
    if inputFile is None:
        exit_message = messages.NONE_INPUT
        print_if_needed("-i, --input     " + printColor.RED +
                        exit_message + printColor.END)
        return exit_message

    if regex is None:
        exit_message = messages.NONE_REGEX
        print_if_needed("-r, --regex     " + printColor.RED +
                        exit_message + printColor.END)
        return exit_message

    if name is None:
        exit_message = messages.NONE_NAME
        print_if_needed("-n, --name      " + printColor.RED +
                        exit_message + printColor.END)
        return exit_message

    if os.path.exists(inputFile) == False:
        exit_message = messages.FILE_NOT_FOUND.format(
            os.path.abspath(inputFile))
        print_if_needed(printColor.RED + exit_message + printColor.END)
        return exit_message

    file = open(inputFile, "r")
    content = file.read()

    print_if_needed(messages.SEARCHING.format(
        regex, os.path.abspath(inputFile)))

    matches = re.findall(regex, content)

    if not matches:
        print_if_needed(messages.NO_MATCHES)
        return messages.NO_MATCHES

    print_if_needed(messages.FINISHED)

    for i in range(0, len(matches)):
        outputFile = "{}{}.rgxprslt".format(name, i)
        result = open(outputFile, "w")
        result.write(matches[i])
        result.close()
        print_if_needed(printColor.BLUE +
                        "{}".format(os.path.abspath(outputFile)) + printColor.END)
    return messages.DONE


if __name__ == "__main__":
    need_print = True
    parser = argparse.ArgumentParser(
        description='Search regex in input file. All match results will be stored in files [--name]*.rgxprslt')

    parser.add_argument('-i', '--input', metavar='',
                        help='input file with content, where to search')
    parser.add_argument('-r', '--regex', metavar='', help='regular expression')
    parser.add_argument('-n', '--name', metavar='',
                        help='name of search results')

    args = parser.parse_args()

    inputFile = args.input
    regex = args.regex
    name = args.name

    main(inputFile, regex, name)
