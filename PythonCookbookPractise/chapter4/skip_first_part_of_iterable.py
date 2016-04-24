from itertools import dropwhile

text = r"""
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times, this information is provided by
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
"""
with open('drop_file') as f:
    for l in dropwhile(lambda line: line.startswith('#'), f):
        print(l, end=' ')

for i in (line for line in text.splitlines() if not line.startswith('#')):
    print(i)

