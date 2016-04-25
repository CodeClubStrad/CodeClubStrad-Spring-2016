#How to add javascript to your web pages
If you didn't already do it in [session_9](../2016_04_18_session_9/), make a new folder in 'Documents' called 'html'. Inside this new folder make two more folders, one called 'media' and one called 'css'.

Open the text editor on the Pi (usually on the Accessories menu).

##Javascript example 1: telling the time
Type this into a new file:

```html
<!DOCTYPE html>
<html>
<head>
<title>My first javascript test</title>

</head>
<body>
<h1>Telling the time</h1>

<button type="button"
onclick="document.getElementById('demo').innerHTML = Date()">
Click me to display Date and Time.</button>

<p>The time is:</p>
<p id="demo"></p>

</body>
</html> 
```
Save this into a text file called (for example) “my_javascript_time.html” in the 'html' folder.

Now open it in the web browser (Internet -> Epiphany).

What do you see?

Click the button - what happens? And again?

## Adding CSS styles
Now add this line after the ```</title>``` tag:
```html
<link rel="stylesheet" type="text/css" href="css/my_styles_v1.css">
```
If you didn't already do this in [session_9](../2016_04_18_session_9/), type this into a new text editor window:

```css
body {
    background-color: lightblue;
}

h1 {
    color: orange;
    text-align: center;
    height: 100px;
    border: 1px solid AliceBlue;
}

p {
    font-family: "Times New Roman";
    font-size: 14px;
    border: 1px dashed Brown;
}
```
Save this into a text file called “my_styles_v1.css” in the 'css' folder you made earlier.

Now reload the webpage. 

What happens? You can change any of the styles - see the reference section below for some options to try.

## Javascript example 2: Combining javascript and css
Remember the button that told the time? We can make it change styles instead. Copy your first javascript file and change it to be:

```html
<!DOCTYPE html>
<html>
<head>
<title>My second javascript test</title>
<link rel="stylesheet" type="text/css" href="css/my_styles_v1.css">
</head>
<body>
<h1>Changing the font</h1>

<p id="demo">Some random text.</p>

<button type="button" onclick="myFunction()">Click Me!</button>

<script>
function myFunction() {
    var x = document.getElementById("demo");
    x.style.fontSize = "25px";           
    x.style.color = "red"; 
    x.innerHTML = "Some random text which we have changed!";
}
</script>

</body>
</html> 
```
Save this in to the html folder and load it in to the web browser.  Click the button. What happens?

## Javascript example 3:Turning on the light
Put the two images from the USB stick into the 'media' folder you created earlier.

Now make a new text file (or copy the one above) and type this into it:

```html
<!DOCTYPE html>
<html>
<head>
<title>My third javascript test: light bulb</title>
<link rel="stylesheet" type="text/css" href="css/my_styles_v1.css">
</head>
<body>
<h1>Turning the light on!</h1>

<p>Click the light bulb to turn on/off the light.</p>

<img id="myImage" onclick="changeImage()" src="media/pic_bulb_off.gif" width="100" height="180">

<p id="demo">The bulb is: Off</p>

<script>
function changeImage() {
    var text = document.getElementById("demo");
    var image = document.getElementById('myImage');
    if (image.src.match("bulb_on")) {
        image.src = "media/pic_bulb_off.gif";
        text.innerHTML = "The bulb is: Off";
    } else {
        image.src = "media/pic_bulb_on.gif";
        text.innerHTML = "The bulb is: On";
    }
}
</script>

</body>
</html>
```
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