#!/usr/bin/env python3
"""
pwiki.py - A simple command line query program for Wikipedia.org

This is a simple command line interface for Jonathan Goldsmith's wikipedia
Python module which is availible on Pypi
(https://pypi.org/project/wikipedia/). It allows users to search for articles
and summaries on Wikipedia.org.

LICENSE:

Copyright © 2020 James Nicholson

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import argparse
import sys
import wikipedia as wiki


def argument_parser():
    """
    Parse the command line arguments and return them.
    """
    parser = argparse.ArgumentParser(
        description='A simple Wikipedia query tool')
    parser.add_argument("-f", "--full",
                        help="Print the full article text",
                        action="store_true")
    parser.add_argument("--lang", nargs='?',
                        help="Set language (default English)")
    parser.add_argument("query_string",
                        action='store',
                        help="The search term for Wikipedia.org")

    args = parser.parse_args()
    return args


def get_full_article(input_string):
    """
    Parse and return the full text of a Wikipedia article.
    """
    article = wiki.page(input_string)
    return article.content


def get_summary(input_string):
    """
    Parse and return a summary of a Wikipedia article.
    """
    article_summary = wiki.summary(input_string, sentences=2)
    return article_summary


def set_language(input_string):
    """
    Set Wikipedia to the desired language.
    """
    wiki.set_lang(input_string)


def main():
    """
    The main function calls the helper functions to pull a wikipedia article of
    the users choice and display it via STDOUT.
    """
    args = argument_parser()

    # Set the query language for the search
    if args.lang is True:
        set_language(args.lang)
    else:
        set_language('en')

    # If a full article is requested, return it
    if args.full is True:
        output_string = get_full_article(args.query_string)
        print(output_string)
    # If a summary is requested, return that
    elif args.full is False:
        output_string = get_summary(args.query_string)
        print(output_string)
    # Otherwise, exit with an error
    else:
        print("\nThere was a problem with your query! Exiting...\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
