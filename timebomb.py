#!/usr/bin/env python2
import os, re

for line in open("%(HOME)s/.timebomb" % os.environ):
    found = re.search('([\w]+).*([0-2][0-9]:[0-5][0-9]).*([0-2][0-9]:[0-5][0-9])', line)
    date = re.search('on ([0-3][0-9]\.[0-1][1-9](.20[0-9]{2}|))', line)
