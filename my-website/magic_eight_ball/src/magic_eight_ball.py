#!/usr/bin/python
print 'Content-Type: text/html'
print

import random

def eightBall():
    f = open('../text/quotes.txt', 'r')
    x = []
    for line in f:
        x.append(line)
    f.close()
    return x[random.randrange(0,len(x))]

import cgi

form = cgi.FieldStorage()
Question = form.getvalue('Question')

print '''<html>
            <head><title>Magic Eight Ball</title></head>
            <table>
                <td>
                <img src="../pics/8_ball_face.jpg" height="290" width="320">
                </td>
                <td>
         '''

if Question != None:
    print eightBall()

print '''       </td>
            </table>
	<a href="magic_eight_ball.html"> Ask another question </a>
        </html>'''
