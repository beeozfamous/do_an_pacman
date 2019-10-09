# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    ss = Directions.STOP
    return [w, w, ss]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState(-))
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    def dfsLUV(graph, node, visited, mazeMap):
        visited.append(node)
        if graph.isGoalState(node):
            return mazeMap, True
        else:
            isTwice = False
            for n in graph.getSuccessors(node):
                if n[0] not in visited:
                    mazeMap.append(n[1])
                    once, isTwice = dfsLUV(graph, n[0], visited, mazeMap)
                    if not isTwice:
                        mazeMap.pop()
                    else:
                        return once, isTwice
            return mazeMap, isTwice

    mazeBegin = problem.getStartState()
    TheWay, isCompleted = dfsLUV(problem, mazeBegin, [], [])
    print(TheWay)
    return TheWay


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    mazeQueue = util.Queue()
    mazeQueue.push((problem.getStartState(), []))
    visited = []
    if (problem.isGoalState(problem.getStartState())): return []
    node, way = mazeQueue.pop()
    while not problem.isGoalState(node):
        if node not in visited:
            visited.append(node)
            for nodeX, wayX, costX in problem.getSuccessors(node):
                mazeQueue.push((nodeX, way + [wayX]))
        node, way = mazeQueue.pop()
    return way


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    mazeMap = util.PriorityQueue()
    mazeMap.push((problem.getStartState(), [], 0), 0)
    visited = []
    if (problem.isGoalState(problem.getStartState())): return []
    node, mazeWay, cost = mazeMap.pop()
    while not problem.isGoalState(node):
        if node not in visited:
            visited.append(node)
            for nodeX, wayX, costX in problem.getSuccessors(node):
                mazeMap.push((nodeX, mazeWay + [wayX], cost + costX), cost + costX)
        node, mazeWay, cost = mazeMap.pop()
    return mazeWay


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    mazeMap = util.PriorityQueue()
    mazeMap.push((problem.getStartState(), [], 0),0)
    visited = []
    if (problem.isGoalState(problem.getStartState())): return []
    node, mazeWay, cost = mazeMap.pop()
    while not problem.isGoalState(node):
        if node not in visited:
            visited.append(node)
            for nodeX, wayX, costX in problem.getSuccessors(node):
                mazeMap.push((nodeX, mazeWay + [wayX], cost + costX),heuristic(nodeX, problem) + cost + costX)
        node, mazeWay, cost = mazeMap.pop()
    return mazeWay


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
