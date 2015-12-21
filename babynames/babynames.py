#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with
    the year string followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    year_regex = re.compile(r'<h3 align="center">Popularity in ([0-9]+)</h3>')
    name_regex = re.compile(
        r'<tr align="right"><td>([0-9]+)</td>'
        r'<td>([A-Za-z]+)</td><td>([A-Za-z]+)</td>')

    output = []
    with open(filename, encoding="utf-8") as fp:
        for line in fp.readlines():
            year = year_regex.match(line)
            rank_name = name_regex.match(line)
            if year:
                year = year.group(1)
                output.append(year)
            if rank_name:
                rank = rank_name.group(1)
                male = rank_name.group(2)
                female = rank_name.group(3)
                output.append("{} {}".format(male, rank))
                output.append("{} {}".format(female, rank))
    output = [output[0]] + sorted(output[1:])
    print(output)
    return output


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    if args[0] == '--summaryfile':
        del args[0]
        for arg in args:
            extract_names(arg)

if __name__ == '__main__':
    main()
