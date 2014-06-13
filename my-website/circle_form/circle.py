#!/usr/bin/python

#import modules
import cgi, cgitb, math

#create a form object
form = cgi.FieldStorage()
cgitb.enable()

#retreive the values: must one a string or "None"
radius = form.getvalue('radius') #getvalue --> gets name (here, name="radius")
diameter = form.getvalue('diameter')
circumference = form.getvalue('circumference')
area = form.getvalue('area')
fontColor = form.getvalue('fontColor')

#create a page string
page = "Content-Type: text/html\n\n"
page +=  '''
<html>
    <head>
        <title> Circle Functions </title> '''

if fontColor != None:
    page += '<font color="' + fontColor + '">'
    
page += '''
    </head>
    <body>
    <h2>Results:</h2>
    <p> '''

if radius == None:
    radius = 0.0
    page += 'Invalid input.  Enter a number.'
    
else:
    page += 'Radius: ' + str(float(radius))
    if diameter != None:
        page += '<br>Diameter: ' + str(2.0*int(radius))
    if circumference != None:
        page += '<br> Circumference: ' + str(2.0*math.pi*int(radius))
    if area != None:    
        page += '<br>Area: ' + str(int(radius)**2*math.pi)

page += '''
        </form>
    </body>
</html>
'''

#print the page
print page
