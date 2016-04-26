    Warning!
    The examples below were tested on and work with the Epiphany web browser, it does not necessarily work on earlier web browsers on RPi. For example we have found that the onClick handler is not always implemented.
    # Frustrating

#How to add javascript to your web pages
If you didn't already do it in [session_9](../2016_04_18_session_9/), make a new folder in 'Documents' called 'html'. Inside this new folder make two more folders, one called 'media' and one called 'css'.

Open the text editor on the Pi (usually on the Accessories menu).

##Javascript example 1: telling the time
Have a look at the [code](javascript1_time.html).

Open it in the web browser (Internet -> Epiphany).

What do you see?

Click the button - what happens? And again?

## Adding CSS styles
Now add this line after the ```</title>``` tag:
```html
<link rel="stylesheet" type="text/css" href="css/my_styles_v1.css">
```
Now save it as a new file - e.g. [javascript1_time_css.html](javascript1_time_css.html)

If you didn't already do this in [session_9](../2016_04_18_session_9/), create a css file something like [this](css/my_styles_v1.css) and save this into a text file called “my_styles_v1.css” in the 'css' folder you made earlier.

Now reload the webpage. 

What happens? You can improve it (which wouldn't be hard) by changing any of the styles in the css file - see the reference section below for some options to try.

## Javascript example 2: Combining javascript and css
Remember the button that told the time? We can make it change styles instead. Copy your first javascript file and change it to resemble [this one](javascript2_font_css.html).

Well done, you have written a junction in javascript :-)

Save this in to the html folder and load it in to the web browser.  Click the button. What happens?

## Javascript example 3:Turning on the light
Put the two images from the USB stick into the 'media' folder you created earlier. Ff you can't find them they are at http://www.w3schools.com/js/js_intro.asp. You need the two light bulbs (on & off).

Now make a new text file (or copy the one above) and type something like [this](javascript3_lightbulb_css.html) into it. Of course you could leave out the horrrible css formating or improve it.

Save this into the html folder and load it in to the web browser. Click the button - what happens?

## Reference

###Some colours to try
```
AliceBlue
AntiqueWhite
Aqua
Aquamarine
Azure
Beige
Bisque
Black
BlanchedAlmond
Blue
BlueViolet
Brown
BurlyWood
CadetBlue
Chartreuse
Chocolate
Coral
CornflowerBlue
```

###Some fonts to try
```
"Book Antiqua"
"Comic Sans MS"
"Arial Black"
"Courier New"
```

###Some alignments to try
```
left
right
```

###Some border options to try
```
border-width	Specifies the width of the border. Default value is "medium" - try pixel sizes
border-style	Specifies the style of the border. Default value is "none" - try dotted, double or dashed
border-color	Specifies the color of the border. Default value is the color of the element
```

For more ideas see http://www.w3schools.com/css/default.asp

Examples adapted from http://www.w3schools.com/js/default.asp