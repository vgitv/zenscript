#!/bin/python3

import subprocess
import re

p = subprocess.Popen(["/usr/bin/tree", "-ifna", "-P", "*.html", "-I", "main.html"],
        stdout=subprocess.PIPE)
output = p.communicate()[0].decode()
tree = output.split('\n')[1:-3]


print('<!DOCTYPE html>')
print('<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">')
print('<head>')
print('  <meta charset="utf-8" />')
print('  <meta name="generator" content="pandoc" />')
print('  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />')
print('  <title>main</title>')
print('  <style type="text/css">')
print('      code{white-space: pre-wrap;}')
print('      span.smallcaps{font-variant: small-caps;}')
print('      span.underline{text-decoration: underline;}')
print('      div.column{display: inline-block; vertical-align: top; width: 50%;}')
print('  </style>')
print('  <link rel="stylesheet" href="style01.css" />')
print('</head>')
print('<body>')

previous = 't'


for i,elt in enumerate(tree):
    if bool(re.search("\.html$", tree[i])):
        if previous == 't':
            print('<ul>')
        #}
        print('<li><a href="{ref}">{link}</a></li>'.format(
            ref=tree[i],
            link=tree[i].split('/')[-1].split('.html')[0]))
        previous = 'h'
    else:
        if previous == 'h':
            print('</ul>')
        #}
        print('<h{n}>{section}</h{n}>'.format(
            n=tree[i].count('/'),
            section=tree[i].split('/')[-1]))
        previous = 't'
#}

print('</ul>')
print('</body>')
print('</html>')
