# -*- coding: utf-8 -*-

import re
match=re.match('Hello[ \t]*(.*)world','Hello        Python world')
print match.group(1)

mt = re.match('/(.*)/(.*)/(.*)','/usr/home/lumberjack')
print mt.group()
print mt.groups()
