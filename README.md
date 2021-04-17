# Final Project - PacMan

For my final project I completed the UC Berkeley PacMan AI homework project 2 and 4.

## Links to Project Source Descriptions

Part 1: MultiAgent
http://ai.berkeley.edu/multiagent.html

Part 2: Ghostbuster Tracking
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

|    start up item				                | corresponding command                                                                             |  
|-----------------------------------------------|---------------------------------------------------------------------------------------------------|
| regular pacman				                | python pacman.py                                                                                  |
| 3. multiagent autograder			            | python autograder.py  --no-graphics                                                               |  
| 1.1 multiagent reflex agent		            | python pacman.py --frameTime 0 -p ReflexAgent -k 1                                                |  
| 1.2 multiagent minimax agent		            | python pacman.py --p MinimaxAgent -l minimaxClassic -a depth=4                                    |  
| 1.3 multiagent alpha-beta agent	            | python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic                                     |  
| 1.4 multiagent expecti-max agent              | python pacman.py -p ExpectimaxAgent -l smallClassic -a depth=3                                    |  
| 1.5 multiagent autograder q5			        | python autograder.py  -q q5                                                                       |  
| 4. tracking autograder			            | python autograder.py   --no-graphics                                                              |  
| 2 Tracking Buster Play			            | python busters.py                                                                                 |  
| 2.1-.2 ExactInference Play			        | python busters.py  -l bigHunt -a inference=ExactInference                                         |  
| 2.1-.2 ExactInference Greedy Buster Auto		| python busters.py -l bigHunt -s -a inference=ExactInference -p GreedyBustersAgent                 |  
| 2.3 GreedyBustersAgent Auto			        | python busters.py -p GreedyBustersAgent -s -a inference=ExactInference                            |  
| 2.4-.5 ParticleFilter Play			        | python busters.py  -k 1 -a inference=ParticleFilter                                               |  
| 2.4-.5 ParticleFilter Greedy Buster Auto		| python busters.py  -k 1 -s -a inference=ParticleFilter -p GreedyBustersAgent                      |  
|2.6-.7 JointParticleFilter Play			    | python busters.py  -k 3 -a inference=MarginalInference -g DispersingGhost                         |  
|2.6-.7 JointParticleFilter Greedy Buster Auto	| python busters.py -s -k 3 -a inference=MarginalInference -g DispersingGhost -p GreedyBustersAgent |  

### How to Run Linux

Assigment Links have instructions for Linux. In short:

1. Open terminal at `multiagent` or `tracking`

    Autograder: `python autograder.py`

    PacMan Classic: `python pacman.py`

For specific run commands to each part refer to the assigments or the table above.

## Discussion

Below is a description of each part, the corresponding specific test command/startup item, and the strategy used.

#### Autograder

The autograder is provided by UC Berkeley. Their grading requirements are described in the links above. These can be run without the graphical component by using `--no-graphics`. Modify the `"scriptArguments"` in `launch.vs.json`.
The autograder checks for the algorithms correctness and also runs the algorithm in game. The grade is based on the algorithms correctness and the average score/wins of the in game tests.

To run the autograde, especially the one that grades the particle filter, it is best to run on the Khoury server:

```
ssh username@login.neu.edu

git clone https://github.com/ribeiro-jenny/FinalProjectVS/settings

cd multiagent

python autograder.py

cd ../tracking

python autograder.py
```

### Part 1 Multi-Agent Search

This assignment explores different decision making algorithms for the both ghost and pacman agents.

#### Q1 Reflex Agent

##### Description 

The task was to design a better evaluation function for pacman's next move. The stratagy for this function was to 
increase the score for moves that go towards food, decrease the score based on the ghost position (the closer the ghost the worse the deduction), and check if the ghost was in a killable state (which will increase the score).
It was useful to use the reciprical of the food distance and enemy distance because the closer they were meant the greater impact on the score. Additionally, each component had a different weight. It considered the possible actions available and calculated the corresponding score for the move. 

This is not meant to be a perfect agent but an introduction into the project.

##### Files Edited

```
multiAgents.py:76
    - ReflexAgent:evaluationFunction()
```

##### Corresponding StartUp Item
```
| 1.1 multiagent reflex agent		            | python pacman.py --frameTime 0 -p ReflexAgent -k 1                                                |  
```

#### Q2 MiniMax Agent

##### Description 

MiniMax decision making algorithms work well for zero-sum games. The algorithm assumes it is playing agaisnt an optimal player.
It works by assigning pacman to aim for the maximum possible score and the ghosts aiming for the minimum possible score. This works because an increase in the pacmans score means a decrease in the ghosts score (zero-sum game). To keep a maximum score if the pacman knows there is no option but to die it walks into a ghost to end the game with the max points possible.

Note that this agent will not win every game (as expected) both because the ghost may not make the optimal move and because of the depth limitation.

The minimax algorithm has limitions. One must limit the depth searched because it would not be fast enough to play through an entire possibility of game outcomes every move. Limiting the depth works but the algorithm is no longer returning the most optimal move for the full game but just of that depth search.

![mini max algo](imgs/MiniMaxAlgo.JPG)

##### Files Edited

```
multiAgents.py:147
    - MinimaxAgent
```

##### Corresponding StartUp Item
```
| 1.2 multiagent minimax agent		            | python pacman.py --p MinimaxAgent -l minimaxClassic -a depth=4                                    |  
```

#### Q3 Alpha-Beta Pruning

##### Description 

This algorithm builds on the MiniMax search by removing the nodes that are certainily a worse move than a previously examined move option - meaning those moves will result in a lower score. This elimates going down the tree of a move that is not useful in maximizing the score.

![alpha beta algo](imgs/AlphaBetaTree.JPG)

The algorithm pseudocode is:
![alpha beta algo](imgs/AlphaBeta.JPG)

##### Files Edited

```
multiAgents.py:217
    - AlphaBetaAgent
```

##### Corresponding StartUp Item
```
| 1.3 multiagent alpha-beta agent	            | python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic                                     |  
```

#### Q4 Expectimax

##### Description 

Expectimax improves on the previous algorithms as it incorporates a probabilistic model for the oponent move rather than assuming the optimal move. The probability is determined by the amount of move options the agent has at a given time e.i. `1/len(possibleMoves)`. Different methods can be used to calculate the probability such as using an evaluation function for score, random probability, or uniform distribution.
 
![Expectimax algo](imgs/Expectimax.JPG)

The change can be seen as in this varient of the algorithm when the pacman is trapped it still takes the chance to move towards the food hoping that the ghost makes a suboptimal move. This leads to the pacman dying with less points in this case. But overall it performs better as there is the case that the ghost makes a suboptimal move then the pacman is correct in taking a chance to go for more food. This can be seen in running the trapped version of the map for both alpha beta and expectimax:

```
python pacman.py -p AlphaBetaAgent -l trappedClassic -a depth=3 -q -n 10

python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10
```

AlphaBetaAgent will always lose and ExpectiMaxAgent wins around 1/2 the time.

##### Files Edited

```
multiAgents.py:286
    - ExpectimaxAgent
```

##### Corresponding StartUp Item
```
| 1.4 multiagent expecti-max agent              | python pacman.py -p ExpectimaxAgent -l smallClassic -a depth=3                                    |  
```

#### Q5 Even Better Evaluation Function

##### Description 

As opposed to the evaluation from Q1 this function considers the game state rather than actions available to score the best move. I used a linear combination of features to determine the score. The features considered are: 

      Food is the most important -> go to food first
        if a ghost is near us consider
            can we eat a pellet to make it killable?
                if yes -> eat pellet kill ghost
                if no -> run away (hopefully towards more food)
        if no ghost -> eat food!

Each consideration adds or deducts from the score at different rates. For example food is more important the the bonus pellet that turns the ghosts white. Another example is if a ghost is near the pacman this takes priority to run away from the ghost to safety as staying alive is more important than points.

##### Files Edited

```
multiAgents.py:385
    - betterEvaluationFunction()
```

##### Corresponding StartUp Item
```
| 1.5 multiagent autograder q5			        | python autograder.py  -q q5                                                                       |  
```

#### General Discussion of Part 1

After completing this homework the difference in optimisic and pessimistic assumptions in AI was made more apparent. 
Assuming that the enemy makes the best move can lead to an early death or an elongated game where the pacman runs away from the ghost rather than moving towards a food item. Contrastingly, using a probablitic model can improve on the simple assumption but can still lead to deaths when chances are taking while assuming non-optimal moves for the enemy. Overall, the ExpectiMax algorthim would be the most fun to play agaisn't because it isn't predictable.

### Part 2 GhostBusters

In this version of pacman, pacman sadly cannot see the ghosts but he can hear them! The following explores different algorithms for locating the ghosts.
The pacman hears via noisy readings of the manhattan distance to the ghost.

For these implementations each has a playable version and a auto play version by a greedy pacman. In the auto play the ghosts have been displayed (`-s`) so that the process can be easily visualized. In the playable version no ghosts are shown to be true to pacmans perspective.

Play `2 Tracking Buster Player` for a crude tracking algorithm. This can be compared to the improvements made below for tracking.

Note: The brighter the tile the more certain pacman is that there is a ghost located there
 
#### Q1 - Q2 Exact Interface

##### Description 

Here the update of pacmans belief distribution based on the sensor information was implemented. The distrubition starts out uniform and is updated to the information gathered at each turn. When a ghost is captured its distrubition is removed.

Q2 builds on this initial implementation and includes filtering the noisy data. Because the pacman tracks time it can filter out data that says the pacman went from 2 squares away to 10 because a ghost can only move one square per turn.

The progression of the distribution can be seen:
![particles](imgs/Exact2.JPG)
![particles](imgs/Exact1.JPG)


##### Files Edited

```
interface.py:111
    - ExactInference::observe()
    - ExactInference::elapseTime()
```

##### Corresponding StartUp Item
```
| 2.1-.2 ExactInference Play			        | python busters.py  -l bigHunt -a inference=ExactInference                                         |  
| 2.1-.2 ExactInference Greedy Buster Auto		| python busters.py -l bigHunt -s -a inference=ExactInference -p GreedyBustersAgent                 |  
```

#### Q3 Greedy Agent

##### Description 

The greedy pacman agent assumes that the ghost is located in the most likely square based on its observations. It will move towards the most likely closest ghost (so the closets square with the highest probability).

##### Files Edited

```
bustersAgents.py:125
    - GreedyBustersAgent::chooseAction()
```

##### Corresponding StartUp Item
```
| 2.3 GreedyBustersAgent Auto			        | python busters.py -p GreedyBustersAgent -s -a inference=ExactInference                            |  
```

#### Q4 - Q5 Particle Filter

##### Description 

Q4 - Q5 focused on implementing a particle filtering algorithm for locating the ghost. The algorithm follows this flow (as shown in the picture below): initial distribution -> sampling -> weighting -> resampling. This repeats on every turn.

Particles are used to mirror the probability distribution as shown:
![particles](imgs/particleTimeLine.JPG)

Q5 extends this algorithm by filtering out noisy data as explained in Q1. Although it filters out noisy data there is still noise as seen below. This is because this is a probabilitic model versus using the exact position information in Q1/2. 

![particles](imgs/particleFilter.JPG)

##### Files Edited

```
interface.py:241
    - ParticleFilter::observe()
    - ParticleFilter::elapseTime()
    - ParticleFilter::initializeUniformly()
    - ParticleFilter::getBeliefDistribution()
```

##### Corresponding StartUp Item
```
| 2.4-.5 ParticleFilter Play			        | python busters.py  -k 1 -a inference=ParticleFilter                                               |  
| 2.4-.5 ParticleFilter Greedy Buster Auto		| python busters.py  -k 1 -s -a inference=ParticleFilter -p GreedyBustersAgent                      |  
```

#### Q6 - Q7 Joint Particle Filter

##### Description 

This algorithm improves on the Q4-Q5 by now considering multiple ghosts simiulationasly versus tracking each on independently. This is done using a dynamic Bayes net and particles. Each particle is now a tuple of ghost positions rather than just a single position. The algorithm follows the same structure above: initial distribution -> sampling -> weighting -> resampling.

Q7 extends this algorithm by filtering out noisy data as explained in Q1.

The Progression can be seen:
![particles](imgs/JointFilter1.JPG)
![particles](imgs/JointFilter2.JPG)

Tracking ghosts simiulationasly is more accurate as more data is being taken into consideration. Knowing that the ghosts will move onto each other helps distinguish the probability of their next move.

##### Files Edited

```
interface.py:410
    - JointParticleFilter::observeState()
    - JointParticleFilter::elapseTime()
    - JointParticleFilter::initializeParticles()
    - JointParticleFilter::getBeliefDistribution()
    - JointParticleFilter::jailGhosts()
```

##### Corresponding StartUp Item
```
|2.6-.7 JointParticleFilter Play			    | python busters.py  -k 3 -a inference=MarginalInference -g DispersingGhost                         |  
|2.6-.7 JointParticleFilter Greedy Buster Auto	| python busters.py -s -k 3 -a inference=MarginalInference -g DispersingGhost -p GreedyBustersAgent |  
```

#### General Discussion of Part 2

The most diffucult part of this part was the particle filtering. Originally I mistakenly tripled the particle count causing the algorithm to run incredible slowly. Particle filtering is an expensive computation that can be speed up with parallezation. It would be intresting to extend this assigment by paralizing the filtering to see what the speed up would be.

Although it was intresting to explore particle filters I do not think it would be useful for Game AI. It is most useful in uncontrolled volitale enviorments. Since you can give agents all information needed in a game this algorithm would be over kill. It is computationally expensive and wouldn't improve the game play by using it.

## Refrences

http://ai.berkeley.edu/lecture_slides.html

https://towardsdatascience.com/how-a-chess-playing-computer-thinks-about-its-next-move-8f028bd0e7b1

https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

https://courses.cs.washington.edu/courses/cse473/12au/pacman/tracking/busters.html

https://towardsdatascience.com/optimal-estimation-algorithms-kalman-and-particle-filters-be62dcb5e83

https://towardsdatascience.com/particle-filter-a-hero-in-the-world-of-non-linearity-and-non-gaussian-6d8947f4a3dc
