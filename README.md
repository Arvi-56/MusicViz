# MusicViz
Hello this is my code2 project
Ive decided to torture myself with the ambitious goal of creating a data viz from variables extracted from the computer microphone
(such as volume and pitch)

I have the data extraction working (see Tester.py) printing to a target.txt file 
and a working plain html (see yall.html) and a-frame page with just a circle (see 

I want to make the circle radius change with volume and the color to change with pitch
At least for pitch I know I will need a bunch of if statements.

Now I need to make a websocket that updates with the output of my Tester.py file and makes a circle with those changing variables.
I found a pretty nice example of a changing graph that does what I want (see index.html and websocket_server.py), but it is too complicated for me to extract the useful parts. I just need the parts that send, recieve, and update the variables.
