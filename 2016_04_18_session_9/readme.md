#How to make web pages
Make a new folder in 'Documents' called 'html'.
Open the text editor on the Pi (usually on the Accessories menu).

##HTML example
Type this into a new file:

```html
<html>
<head>
<title>Title of page</title>

</head>
<body>
<h1>My heading 1</h1>
<p>Some text</p>

<h2>My heading 2</h2>
<p>Some more text</p>

</body>
</html>
```
Save this into a text file called (for example) “my_webpage.html” in the 'html' folder.

Now open it in the web browser (Internet -> Epiphany).

What do you see?

Dull isn't it?

##CSS example
Now add this line after the ```</title>``` tag:
```html
<link rel="stylesheet" type="text/css" href="my_styles_v1.css">
```
Now type this into a new text editor window:

```css
body {
    background-color: lightblue;
}

h1 {
    color: orange;
    text-align: center;
}

p {
    font-family: "Times New Roman";
    font-size: 12px;
    border: 1px solid AliceBlue;
}
```
Save this into a text file as called “my_styles_v1.css”.

Now reload the webpage. 

What happens?

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