Manny's Finite State Automata
=============================

Manny's Finite State Automata is a regex state machine builder and validator. This is a project developed for ICOM4036.

How To Run
----------

To run the program do the following:

First, install the dependencies of the project:
```
pip install -r requirements.txt
```
We suggest you use a `virtualenv` for this.

Afterwards:

```
py main.py
```

Once the program starts, a popup window will appear. Once you click Ok, you might encounter an error in which the program window will not accept input. If this occurs, click the terminal in which you launched the program and click the program window again.

Limitations
------------
This program does not contain validation. Any incorrect regular expressions will produce unwanted regular expression state machines.

### Valid Tokens
+ (
+ )
+ *
+ |
+ alphanumeric color_values


### Known Errors
+ (ab|ab) - Combining two characters with an | will produce an unwanted regex.
+ f(asterisk) w(asterisk) - Placing two tokens with * back to back will cause errors.
