## pwiki - Pull article and summaries from Wikipedia.organization


Pwiki allows the user to pull Wikipedia articles or summaries in plain text using a command line interface. If the program is run in a shell that allows redirection and/or piping, then the output can be sent to a file and/or parsed if required.


### Usage


Pwiki is a command line utility and gives some options about how to call it. The -h option shows a use message:

```bash
$ ./pwiki.py -h
usage: pwiki.py [-h] [-f] [--lang [LANG]] query_string

A simple Wikipedia query tool

positional arguments:
  query_string   The search term for Wikipedia.org

optional arguments:
  -h, --help     show this help message and exit
  -f, --full     Print the full article text
  --lang [LANG]  Set language (default English)
```



### Requirements


This program requires only the Wikipedia Python module which is available on Pypi at this address https://pypi.org/project/wikipedia/ . Credit for the Wikipedia module goes to Jonathan Goldsmith.
