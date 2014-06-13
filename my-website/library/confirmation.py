#!/usr/bin/python

import cgi,cgitb

form = cgi.FieldStorage()
cgitb.enable()

title = form.getvalue('title')
author = form.getvalue('author')
publisher = form.getvalue('publisher')
year = form.getvalue('year')
isbn = form.getvalue('isbn')
classification = form.getvalue('classification')
ficnon = form.getvalue('ficnon')
Softcover = form.getvalue('Softcover')
Hardcover = form.getvalue('Hardcover')
Spiralbound = form.getvalue('Spiralbound')
summary = form.getvalue('summary')

book = []

if title != None:
    book.append(title)
else:
    book.append("")

if author != None:
    book.append(author)
else:
    book.append("")

if publisher != None:
    book.append(publisher)
else:
    book.append("")

if year != None:
    book.append(year)
else:
    book.append("")

if isbn != None:
    book.append(isbn)
else:
    book.append("")

book.append(classification)

if ficnon != None:
    book.append(ficnon)
else:
    book.append("")

entry = ""
if Softcover != None:
    entry += "Softcover "
if Hardcover != None:
    entry += "Hardcover "
if Spiralbound != None:
    entry += "Spiralbound "
book.append(entry)

if summary != None:
    book.append(summary)
else:
    book.append("")

a = open('database.csv','a')
for each in book[:-1]:
    a.write(each+',')
a.write(book[-1])
a.write('\n')
a.close()

print "Content-Type: text/html\n\n"
print  '''
<html>
    <head> <title> Confirmation </title> </head>
         '''

print '''<body>
    Congratulations!  Your data has been entered:
    <p> '''
print book
print '''
    <p>
    <a href="catalog.py">View catalog</a>
    </body>
</html>
'''
