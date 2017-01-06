import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
import math
from collections import namedtuple

import pprint

import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
import math
from collections import namedtuple
import pprint
from scipy import constants as sc

class QLearningAgent(Agent):
    """An learning agent that learns to drive  using Q learning"""

    def __init__(self, env):
        super(QLearningAgent, self).__init__(env)  
        self.color = 'red'  
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        ##initialize q table here
        
        self.alpha    = 0.7
        self.gamma    = 0.1      
        self.previousState = None
        self.state = None
        self.previousAction = None  
        self.previous_reward = None
        self.cumulativeRewards = 0        
        self.qTable = dict()       
        self.discount = self.gamma       
        self.deadline = self.env.get_deadline(self)       
 
    def reset(self, destination=None):        
        #resets the current values of the agent        
        self.planner.route_to(destination)
        self.previousState = None
        self.state = None
        self.previousAction = None
        self.cumulativeRewards = 0
        

    def getLegalActions(self, state):       
        return ['forward', 'left', 'right', None]

    
    def getQValue(self, state, action):
        #if not  (state, action) in qZable return 20.0
        return self.qTable.get((state, action), 30.0)  
    
    
    def getPolicyAndValue(self, state):
        """
        Compute the best action to take in a state.
        input: state
        output: best possible action and qvalue(policy maps states to action)       
        Evaluate all legal actions and return the one with the best Q value.
        """
        legalActions = self.getLegalActions(state)  
        bestAction = None       
        bestQValue=-1000000000
        for action in legalActions:
            if(self.getQValue(state, action) >= bestQValue):
                bestQValue = self.getQValue(state, action)
                bestAction = action          
        return bestQValue,bestAction        
    
    def getValue(self, state):
        value,action=self.getPolicyAndValue(state)
        return value
    
    def getPolicy(self, state):
        value,action=self.getPolicyAndValue(state)
        return action    
    
    def getAction(self, state):
          
       # Pick Action
        legalActions = self.getLegalActions(state)  
        action = None  
        action = self.getPolicy(state)
        return action

    def updateQTable(self, state, action, nextState, reward):
          
        if((state, action) not in self.qTable): 
            self.qTable[(state, action)] = 30.0
        else:           
            self.qTable[(state, action)] = self.qTable[(state, action)] + self.alpha*(reward + self.discount*self.getValue(nextState) - self.qTable[(state, action)])
    

    def createState(self, state):
       
        #This function creates a state and returns 
     
        State = namedtuple("State", ["light","next_waypoint"])
        return State(light = state['light'], next_waypoint = self.planner.next_waypoint())
 

    def update(self, t):         
        self.next_waypoint = self.planner.next_waypoint()  
        ## this is my current state
        self.state = self.createState(self.env.sense(self))
        ##get the current best action based on q table
        action = self.getAction(self.state)
        ##perform the action and now get the reward
        reward = self.env.act(self, action)
        ## in case of initial configuration don't update the q table, else update q table
        if self.previous_reward!= None:
            self.updateQTable(self.previousState,self.previousAction,self.state,self.previous_reward)
        # store the previous action and state so that we can update the q table on the next iteration
        self.previousAction = action
        self.previousState = self.state
        self.previous_reward = reward
        self.cumulativeRewards += reward
      #  if reward==12:
            #destination reached
      #      print "Cumulative Rewards ",self.cumulativeRewards


   
class LearningAgent(Agent):
    
    # This is the naive agent
    """An agent that learns to drive in the smartcab world."""
    
    

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        # TODO: Initialize any additional variables here
       

    def reset(self, destination=None):
        self.planner.route_to(destination)
       
        # TODO: Prepare for a new trip; reset any variables here, if required
      
        
    def update(self, t):
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
    #    print "LearningAgent.update(): next waypoint", self.next_waypoint
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)
        
        current_env_state = self.env.sense(self)
        # TODO: Update state
        #Environment State  is a set of possible states:   # 'location': 'heading','destination', 'deadline'        
                   
        action = None        
        # Set of possible actions Environment.valid_actions[1:]
        possible_actions = []
        if(current_env_state['light'] == 'red'):
            if(current_env_state['oncoming'] != 'left'):
                possible_actions = ['right', None]
        else:
            # traffic ligh is green and now check for oncoming
            #if no oncoming 
            if(current_env_state['oncoming'] == 'forward'):
                possible_actions = [ 'forward','right']
            else:
                possible_actions = ['right','forward', 'left']
        
        # TODO: Select action according to your policy
        if possible_actions != [] :
            action_int =  random.randint(0,len(possible_actions)-1)
            action = possible_actions[action_int]
             
        # Execute action and get reward
        reward = self.env.act(self, action)
        # TODO: Learn policy based on state, action, reward
        # No learning strategy!
      #  print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]
        


def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    
    a = e.create_agent(QLearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # set agent to track

    # Now simulate it
    sim = Simulator(e, update_delay=0.001)  # reduce update_delay to speed up simulation
    sim.run(n_trials=100)  # press Esc or close pygame window to quit


if __name__ == '__main__':
    run()
