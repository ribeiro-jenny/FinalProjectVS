# Final Project - Pacman

For my final project I completed two of the USC Berkely Pacman AI homework projects.

## Links to Project Source Descriptions

Part 1: MultiAgent
http://ai.berkeley.edu/multiagent.html

Part 2: Tracking
http://ai.berkeley.edu/tracking.ht

### How to Run on Windows Visual Studio 2019
1. Open Visual Studio

2. Tools -> Python -> Python Environments 
        2.1 This will open up a side window now click "Add Environments"
        2.2 This will open a pop-up. Go to Python installation and install 2.7

3. If this doesn't work follow microsofts instruction guide :  https://docs.microsoft.com/en-us/visualstudio/python/installing-python-support-in-visual-studio?view=vs-2019

2. There is a Python env attached in the Project Code. Make sure it is activated.
	2.1. This should automatically activate but if not for to Tools -> Python -> Python Environment -> Add Environment and add the Existing Environment 

3. Choose wanted start up item:

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

## Discussion

Below is a description of each part, the corresponding specific test command (you may need to add/modify a startup item if it is not a main one listed above), and the strategy used.

#### Autograder

This will run the provided autograder from UC Berkely. Their grading requirements are described in the links above. These can be run without the graphical component by using `--no-graphics`. Modify the "scriptArguments" in `launch.vs.json`.
The autograder checks for the algorithms correctness and also runs the algorithm in game. So the autograder grade is based on the algorithms tests and the average score/wins of the in game tests.

### Part 1

#### Q1 Reflex Agent

##### Description 

The task was to design a better evaluation function for pacmans next move. The stratagy for this function was to 
increase the score for moves that go towards food, decrease the score based on the ghost position (the closer the ghost the worse the deduction), and check if the ghost was in a killable state (which will increase the score).
It was useful to use the reciprical of the food distance and enemy distance because the closer they were meant the greater impact on the score.

This is not meant to be a perfect agent but an introduction into the project.

##### Files Edited

```
multiAgents.py:76
    - ReflexAgent:evaluationFunction()
```

#### Q2 MiniMax Agent

##### Description 

MiniMax algorithms work well for zero-sum games. 

![alt text](/img/MiniMaxAlgo.JPG)

##### Files Edited
MinimaxAgent class stub in multiAgents.py.
#### Q3
##### Description 
##### Files Edited
#### Q4

##### Description 
##### Files Edited
#### Q5

##### Description 
##### Files Edited
### Part 2

#### Q1
##### Description 
##### Files Edited
#### Q2
##### Description 
##### Files Edited
#### Q3
##### Description 
##### Files Edited
#### Q4
##### Description 
##### Files Edited
#### Q5
##### Description 
##### Files Edited
## Refrences

http://ai.berkeley.edu/lecture_slides.html