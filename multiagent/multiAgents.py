# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        scaredTimeList holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        ghostStateList = successorGameState.getGhostStates()
        scaredTimeList = [ghostState.scaredTimer for ghostState in ghostStateList]

        "*** YOUR CODE HERE ***"

        # The closer the food better the score
        foodPos = newFood.asList()
        distanceFoodScore = []
        if len(foodPos) > 0:
            for food in foodPos:
                distanceFoodScore.append(util.manhattanDistance(newPos, food))
            minFoodDist = min(distanceFoodScore)
            minFoodDist = max(minFoodDist, 0.1) # avoid div by 0 error
            foodScore = (1.0/minFoodDist)
        else:
            foodScore = 0

        # The closer a Ghost is the worse the score
        ghostPos= []
        if len(ghostStateList) > 0:
            for ghost in ghostStateList:
               ghostPos.append(util.manhattanDistance(newPos, ghost.getPosition()))
            minGhostPos = min(ghostPos)
            minGhostPos = max(minGhostPos, 0.1) # avoid div by 0 error
            ghostScore = (1.0/minGhostPos)
        else:
            ghostScore = -1

        # if the ghost is closer amplify the score
        if minGhostPos < 3:
            ghostScore = 15

        # ghost is eatable!
        scaredScore = 0
        for scared in scaredTimeList:
            if scared > minGhostPos:
                scaredScore += scared
                ghostScore = 0

        # make sure we arn't in the start bc then its negative
        if successorGameState.getScore() > 10:
            return (successorGameState.getScore() - ghostScore + foodScore + scaredScore)
        return successorGameState.getScore() 

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        # function returns pair of (action, cost) thourgh mini max tree parsing
        return self.miniMax(gameState, 0, 0)[0]

    # refrence from the http://ai.berkeley.edu/lecture_slides.html slides for algorithm
    def miniMax(self, gameState, index, depth):
        # index incremented to max start back at 0 and incr depth
        if index >= gameState.getNumAgents():
            index = 0
            depth += 1

        # if state is terminal return state's utility
        if  gameState.isWin()  or  gameState.isLose() or depth >= self.depth:
            return (Directions.STOP, self.evaluationFunction(gameState))
        # if next agent is max -> maxValue
        if index == 0:
            return self.maxValue(gameState, index, depth)
        # if next agent is min -> minValue
        else:
            return  self.minValue(gameState, index, depth)

    def minValue(self, gameState, index, depth):
        # v = +inf
        p_inf = float('inf')
        returnValue = (Directions.STOP, p_inf)

        #for successor in state -> v = min(v, miniMax(successor))
        legalMoves = gameState.getLegalActions(index)
        for action in legalMoves:
            successor = gameState.generateSuccessor(index, action)
            compValue = (action, self.miniMax(successor, index+1,  depth)[1])
            returnValue = min(returnValue, compValue, key = lambda t:t[1]) # https://stackoverflow.com/questions/14802128/tuple-pairs-finding-minimum-using-python
        return returnValue

    def maxValue(self, gameState, index, depth):
        # v = -inf
        p_inf = float('-inf')
        returnValue = (Directions.STOP, p_inf)

        #for successor in state -> v = max(v, miniMax(successor))
        legalMoves = gameState.getLegalActions(index)
        for action in legalMoves:
            successor = gameState.generateSuccessor(index, action)
            compValue = (action, self.miniMax(successor, index+1,  depth)[1])
            returnValue = max(returnValue, compValue, key = lambda t:t[1])  # https://stackoverflow.com/questions/14802128/tuple-pairs-finding-minimum-using-python
        return returnValue

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        # alpha : MAX's best option on path to root
        # beta : MIN's best option on path to root
        # function returns pair of (action, cost) thourgh alpha beta mini max tree parsing
        return self.alphaBeta(gameState, 0, 0, float('-inf'), float('inf'))[0]

    def alphaBeta(self, gameState, index, depth, alpha, beta):
        # index incremented to max start back at 0 and incr depth
        if index >= gameState.getNumAgents():
            index = 0
            depth += 1

        # if state is terminal return state's utility
        if  gameState.isWin()  or  gameState.isLose() or depth >= self.depth:
            return (Directions.STOP, self.evaluationFunction(gameState))
        # if next agent is max -> maxValue
        if index == 0:
            return self.maxValue(gameState, index, depth, alpha, beta)
        # else next agent is min -> minValue
        else:
            return self.minValue(gameState, index, depth, alpha, beta)

    def minValue(self, gameState, index, depth, alpha, beta):
        # v = +inf
        p_inf = float('inf')
        returnValue = (Directions.STOP, p_inf)

        #for successor in state -> v = min(v, alphaBeta(successor, alpha, beta))
        legalMoves = gameState.getLegalActions(index)
        for action in legalMoves:
            successor = gameState.generateSuccessor(index, action)
            compValue = (action, self.alphaBeta(successor, index+1,  depth, alpha, beta)[1])
            returnValue = min(returnValue, compValue, key = lambda t:t[1]) 

            # pruning
            if returnValue[1] < alpha: 
                return returnValue
            beta = min(beta, returnValue[1])
        return returnValue

    def maxValue(self, gameState, index, depth, alpha, beta):
        # v = -inf
        p_inf = float('-inf')
        returnValue = (Directions.STOP, p_inf)

        #for successor in state -> v = max(v, alphaBeta(successor, alpha, beta))
        legalMoves = gameState.getLegalActions(index)
        for action in legalMoves:
            successor = gameState.generateSuccessor(index, action)
            compValue = (action, self.alphaBeta(successor, index+1,  depth, alpha, beta)[1])
            returnValue = max(returnValue, compValue, key = lambda t:t[1])  
            
            # pruning
            if returnValue[1] > beta: 
                return returnValue
            alpha = max(alpha, returnValue[1])
        return returnValue


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        return self.expectiMax(gameState, 0, 0)[0]

    def expectiMax(self, gameState, index, depth):
        # index incremented to max start back at 0 and incr depth
        if index >= gameState.getNumAgents():
            index = 0
            depth += 1

        #if state is terminal -> return state utility
        if  gameState.isWin()  or  gameState.isLose() or depth >= self.depth:
            return (Directions.STOP, self.evaluationFunction(gameState))
        #if the next agent is MAX: return max-value(state)
        if index == 0:
            return self.maxValue(gameState, index, depth)
        #if the next agent is EXP: return exp-value(state)
        else:
            return  self.expValue(gameState, index, depth)

    def maxValue(self, gameState, index, depth):
        # v = -inf
        p_inf = float('-inf')

        returnValue = (Directions.STOP, p_inf)

        #for each successor of state -> max(v, value(successor))
        legalMoves = gameState.getLegalActions(index)
        for action in legalMoves:
            successor = gameState.generateSuccessor(index, action)
            compValue = (action, self.expectiMax(successor, index+1,  depth)[1])
            returnValue = max(returnValue, compValue, key = lambda t:t[1])  

        return returnValue

    def expValue(self, gameState, index, depth):
        cost = 0

        #for each successor of state -> v += p * value(successor)
        legalMoves = gameState.getLegalActions(index)
        for action in legalMoves:
            # prob is every outcome not pacman -> ghost moves
            prob = 1.0 / len(legalMoves)
            successor = gameState.generateSuccessor(index, action)
            cost += prob*self.expectiMax(successor, index+1,  depth)[1]
            returnValue= (action, cost) 
        return returnValue

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: 
      Food is the most important -> go to food first
        if a ghost is near us consider
            can we eat a pellet to make it killable?
                if yes -> eat pellet kill ghost
                if no -> run away (hopefully towards more food)
        if no ghost -> eat food!
    """
    "*** YOUR CODE HERE ***"
    foodList = currentGameState.getFood().asList()
    pacPos = currentGameState.getPacmanPosition()
    ghostStateList = currentGameState.getGhostStates()
    scaredTimeList = [ghostState.scaredTimer for ghostState in ghostStateList]
    ghostKillers = currentGameState.getCapsules()

     # The closer the food better the score
    foodScore = 0
    distanceFoodScore = []
    if len(foodList) > 0:
        for food in foodList:
            distanceFoodScore.append(util.manhattanDistance(pacPos, food))
        minFoodDist = min(distanceFoodScore)
        foodScore = (1.0 / minFoodDist) * 10.0  

    # The closer a Ghost is the worse the score
    ghostPos= []
    if len(ghostStateList) > 0:
        for ghost in ghostStateList:
            ghostPos.append(util.manhattanDistance(pacPos, ghost.getPosition()))
        minGhostPos = min(ghostPos)

    # if the ghost is closer amplify the score
    if minGhostPos < 1:
        ghostScore =  15.0
    elif minGhostPos < 4:
        ghostScore = (1.0 / minGhostPos) * 15.0
    else:
        ghostScore = (1.0 / minGhostPos) * 5.0

    # can make ghosts killable if he is near us
    killerScore = 0
    if minGhostPos < 3 and len(ghostKillers) > 0:
        killerPos = []
        for killer in ghostKillers:
            killerPos.append(util.manhattanDistance(pacPos, killer))
            minKiller = min(killerPos)
            killerScore = 1.0 / minKiller
        if minKiller < 1:
            killerScore = 20.0

    # ghost is eatable!
    scaredScore = 0
    for scared in scaredTimeList:
        if scared > minGhostPos:
            scaredScore += scared
            ghostScore = 0

    return  foodScore + currentGameState.getScore() - ghostScore + killerScore + scaredScore

# Abbreviation
better = betterEvaluationFunction