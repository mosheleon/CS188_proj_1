# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    fringe = util.Stack()
    expandedSet = set()

    fringe.push( ( (problem.getStartState(),'',''),() ) )
    #print ( (problem.getStartState(),'',''),('',) )

    while (fringe.isEmpty()==False):  # not fringe.isEmpty()
        current = fringe.pop()
        #print 'current was popped is: {}'.format(current)
        #print 'current[0][0] is: {}'.format(current[0][0])
        if problem.isGoalState(current[0][0]):
            print 'reached goal- returning it {}'.format('CHANGED')
            return list(current[1])
        else:
            #print 'not goal, push children if not in set'
            expandedSet.add(current[0][0])
            children = problem.getSuccessors(current[0][0])
            #print 'children = {}'.format(children)
            for child in children:
                #print 'child is: {}'.format(child)
                if child[0] not in expandedSet:
                    #print 'current = {}'.format(current)
                    #print 'current1 = {}'.format(current[1])
                    #print 'child = {}'.format(child[1])
                    
                    tempB = child , (current[1]+(child[1],) )
                    #print 'tempB is: {}'.format(tempB)
                    fringe.push(tempB)

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """                  
    fringe = util.Queue()
    expandedSet = set()

    fringe.push( (problem.getStartState(),'','',() ) )
    
    while (fringe.isEmpty()==False):  
        current = fringe.pop()        
        #print 'this is current: {}'.format(current)        
        if problem.isGoalState(current[0]):                
            return list(current[3])
        else:            
            if current[0] not in expandedSet:
                #print 'CURRENT IS:',current
                expandedSet.add(current[0])
                #print 'expanded set is: {}'.format(expandedSet)
                children = problem.getSuccessors(current[0])
                #print 'children = {}'.format(children)
                for child in children:                        
                    makeTuple = (child[1],)                
                    temp = current[3]+makeTuple                                       
                    newChild = (child[0],child[1],child[2],temp)
                    #print 'newChild:',newChild                    
                    fringe.push(newChild)
    return []

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
        
    fringe = util.PriorityQueue()
    expandedSet = set()
    
    #print 'this is the first push: {}'.format(((problem.getStartState(),'',0),()))
    fringe.push( ((problem.getStartState(),'',0),()), 0)  
   
    while (fringe.isEmpty()==False):
        current = fringe.pop()
        costSoFar = current[0][2]    
        #print 'THIS IS CURRENT: {}'.format(current)    
        if problem.isGoalState(current[0][0]):           
            return list(current[1])
        else:            
            if current[0][0] not in expandedSet:
                expandedSet.add(current[0][0])                
                children = problem.getSuccessors(current[0][0])                
                for child in children:     
                    childCost = child[2]+costSoFar   
                    newChild = child[0],child[1],childCost           
                    tempB = newChild , (current[1]+(child[1],) )                   
                    fringe.push(tempB,childCost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    expandedSet = set()
    #print 'this is the initial heuristic: {}'.format(heuristic(problem.getStartState(),problem))    
    fringe.push((problem.getStartState(),'',0,()), heuristic(problem.getStartState(),problem))  
    #print 'this is the initial push'
    while (fringe.isEmpty()==False):
        current = fringe.pop()
        costSoFar = current[2]            
        if problem.isGoalState(current[0]):            
            return list(current[3])
        else:            
            if current[0] not in expandedSet:
                expandedSet.add(current[0])                
                children = problem.getSuccessors(current[0])                
                for child in children:     
                    childCost = child[2]+costSoFar 
                    path = current[3]+(child[1],) 
                    childToPush = child[0],child[1],childCost,path                        
                    pushCost = childCost+heuristic(child[0],problem)
                    fringe.push(childToPush,pushCost)
    return []
    
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
