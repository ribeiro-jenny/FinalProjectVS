# Final Project - Pacman

## Description

Part 1: 
http://ai.berkeley.edu/multiagent.html

Part 2:
http://ai.berkeley.edu/tracking.ht

### How to Run on Windows Visual Studio 2019

1. Have Python 2.7 downloaded in Visual Studio
	- https://docs.microsoft.com/en-us/visualstudio/python/installing-python-support-in-visual-studio?view=vs-2019
2. There is a Python env attached in the Project Code. Make sure it is activated.
3. Choose wanted start up item

|    start up item				| corresponding command           |  
|-------------------------------|---------------------------------|
| regular pacman				| python pacman.py                |
| multiagent autograder			| python autograder.py            |   
| multiagent reflex agent		| python pacman.py -p ReflexAgent |  
| multiagent minimax agent		| python pacman.py -p MinimaxAgent|  
| multiagent alpha-beta agent	| python pacman.py -p AlphaBetaAgent -l trappedClassic -a depth=3 -q  |  
| multiagent expecti-max agent  | python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q |  
| tracking autograder			| python autograder.py            |  


### How to Run Linux

Assigment Links have instructions for Linux. In short:

1. Open terminal at `multiagent` or `tracking`

Autograder: `python autograder.py`

PacMan Classic: `python pacman.py`

For specific run commands to each part refer to the assigments or the table above. This are mainly used in testing and the autograder can be run for an overall view.
Part 1 Specific Example: `python pacman.py -p ReflexAgent` 

## Results
