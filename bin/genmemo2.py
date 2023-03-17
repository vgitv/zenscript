#!/bin/python3

import subprocess
import re

p = subprocess.Popen(["/bin/find", "-mindepth", "2", "-name", "*.html"], stdout=subprocess.PIPE)
output = p.communicate()[0].decode()
tree = output.split('\n')[:-1]
tree.sort()

# for i, elt in enumerate(tree):
#     print(i, elt)
# 
# print()

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
print('<h1 id="maintitle">Notes</h1>')

previousSection = ''

for i, elt in enumerate(tree):
    temp = elt.split('/')
    currentSection = '/'.join(temp[1:-2])
    if currentSection == previousSection:
        print('<li><a href="{ref}">{link}</a></li>'.format(ref=elt, link=temp[-2].replace('_', ' ')))
    #}
    else:
        if i > 0:
            print('</ul>')
        #}
        for j, title in enumerate(currentSection.split('/')):
            if len(previousSection.split('/')) > j:
                if title != previousSection.split('/')[j]:
                    print('<h{n}>{section}</h{n}>'.format(n=j+1, section=title.replace('_', ' ')))
                #}
            else:
                print('<h{n}>{section}</h{n}>'.format(n=j+1, section=title.replace('_', ' ')))
            #}
        print('<ul>')
        print('<li><a href="{ref}">{link}</a></li>'.format(ref=elt, link=temp[-2].replace('_', ' ')))
    previousSection = currentSection
    #}
#}

print('</ul>')
print('</body>')
print('</html>')
