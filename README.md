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

4. There is a Python env attached in the Project Code. Make sure it is activated.
	
    4.1. This should automatically activate but if not for to Tools -> Python -> Python Environment -> Add Environment and add the Existing Environment 

5. Choose wanted start up item:

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

Below is a description of each part, the corresponding specific test command, and the strategy used.

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

MiniMax decision making algorithms work well for zero-sum games. The algorithm assumes it is playing agaisnt an optimal player. It 
It works by assigning pacman was aiming for the maximum score and the ghosts aiming for the minimum score. This works because an increase in the pacmans score means a decrease in the ghosts score (zero-sum game).  
To keep a maximum score if the pacman knows there is no option but to die it walks into a ghost to end the game with the max points possible.

Note that this agent will not win every game (as expected) both because the ghost may not make the optimal move and because of the depth limitation.

The minimax algorithm has limitions though. One must limit the depth searched because it would not be fast enough to play through an entire possibility of game outcomes every move. Limiting the depth works but the algorithm is no longer returning the most optimal move for the full game but just of that depth search.
![mini max algo](imgs/MiniMaxAlgo.JPG)

##### Files Edited

```
multiAgents.py:147
    - MinimaxAgent
```

#### Q3 Alpha-Beta Pruning


##### Description 

This algorithm builds on the Minimax search by removing the nodes that need to be evaluated.
Nodes are removed that are certainily a worse move than a previously examined move option. This elimates going down the tree of a move that it not usefull.

![alpha beta algo](imgs/AlphaBetaTree.JPG)

The algorithm pseudocode is:
![alpha beta algo](imgs/AlphaBeta.JPG)



##### Files Edited

```
multiAgents.py:217
    - MinimaxAgent
```

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
https://towardsdatascience.com/how-a-chess-playing-computer-thinks-about-its-next-move-8f028bd0e7b1
https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning