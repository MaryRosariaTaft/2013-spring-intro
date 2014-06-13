#!/usr/bin/python
print 'Content-Type: text/html'
print

##CGI: common gateway interface; allows user to input information

##bart.stuy.edu/~mary.taft/hello_get.py?FirstName=Mary&LastName=Taft

import cgi #it's a module

form = cgi.FieldStorage()
FirstName = form.getvalue('FirstName')
MiddleInitial = form.getvalue ('MiddleInitial')
LastName = form.getvalue('LastName')

print '''<html>
            <title> CGI </title>
            <body> Hello'''
if FirstName != None:
    print FirstName.strip().title()
if MiddleInitial != None:
    print MiddleInitial.title() + '.'
if LastName != None:
    print LastName.strip().title()
print '''   </body>
         </html>'''
