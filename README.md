# JARVIS (Just a Rather Very Intelligent System)

#### This was my attempt to make a voice assistant similar to JARVIS (in iron man movie)
#### Let's be honest, it's not as intelligent as in the movie, but it can do a lot of cool things and automate your daily tasks you do on your personal computers/laptops.

## Built with

<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>


## Features

#### For a cool demo of this project watch this [YouTube video](https://youtube.com/@midnightchess-nb7kh?si=aRhS9Ch_tfK5BjlS)

It can do a lot of cool things, some of them being:

- Greet user
- Tell current time and date
- Launch applications/softwares 
- Open any website
- Tells about weather of any city
- Tells about any person (via Wikipedia)
- Can search anything on Google 
- Can play any song on YouTube
- Plays music
- Send email (with subject and content)
- Has a cool Graphical User Interface
- Has focus mode for studying

## API Keys
there's no need for API keys.


## Code Structure


    ├── driver
    ├── Jarvis              # Main folder for features 
    │   ├── password        # enter password to access jarvis
    │   ├── features        # All functionalities of JARVIS 
    │   └── utils           # GUI images
    ├── __init__.py         # Definition of feature's functions
    ├── gui.ui              # GUI file (in .ui format)
    ├── main.py             # main driver program of Jarvis
    ├── requirements        # all dependencies of the program

- The code structure if pretty simple. The code is completely modularized and is highly customizable
- To add a new feature:
  -  Make a new file in features folder, write the feature's function you want to include
  - Add the function's definition to __init__.py
  - Add the voice commands through which you want to invoke the function

## Team Members
- Developing Ninjas(1st year iiit pune) ; Akshat , Manorath , Rachit , Satyam.

## Future Improvements
- Generalized conversations can be made possible by incorporating Natural Language Processing
- GUI can be made more nicer to look at and functional
- More functionalities can be added
