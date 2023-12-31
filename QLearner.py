""""""  		  	   		   	 			  		 			 	 	 		 		 	
"""  		  	   		   	 			  		 			 	 	 		 		 	
Template for implementing QLearner  (c) 2015 Tucker Balch  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		   	 			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		   	 			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
Template code for CS 4646/7646  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		   	 			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		   	 			  		 			 	 	 		 		 	
and other users of this template code are advised not to share it with others  		  	   		   	 			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		   	 			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		   	 			  		 			 	 	 		 		 	
or edited.  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		   	 			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		   	 			  		 			 	 	 		 		 	
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		   	 			  		 			 	 	 		 		 	
GT honor code violation.  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
-----do not edit anything above this line---  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
Student Name: Stella Soh  		  	   		   	 			  		 			 	 	 		 		 	
GT User ID: lsoh3 	  	   		   	 			  		 			 	 	 		 		 	
GT ID: 903641298 	  	   		   	 			  		 			 	 	 		 		 	
"""  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
import random as rand
import numpy as np


class QLearner(object):  		  	   		   	 			  		 			 	 	 		 		 	
    """  		  	   		   	 			  		 			 	 	 		 		 	
    This is a Q learner object.  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
    :param num_states: The number of states to consider.  		  	   		   	 			  		 			 	 	 		 		 	
    :type num_states: int  		  	   		   	 			  		 			 	 	 		 		 	
    :param num_actions: The number of actions available..  		  	   		   	 			  		 			 	 	 		 		 	
    :type num_actions: int  		  	   		   	 			  		 			 	 	 		 		 	
    :param alpha: The learning rate used in the update rule. Should range between 0.0 and 1.0 with 0.2 as a typical value.  		  	   		   	 			  		 			 	 	 		 		 	
    :type alpha: float  		  	   		   	 			  		 			 	 	 		 		 	
    :param gamma: The discount rate used in the update rule. Should range between 0.0 and 1.0 with 0.9 as a typical value.  		  	   		   	 			  		 			 	 	 		 		 	
    :type gamma: float  		  	   		   	 			  		 			 	 	 		 		 	
    :param rar: Random action rate: the probability of selecting a random action at each step. Should range between 0.0 (no random actions) to 1.0 (always random action) with 0.5 as a typical value.  		  	   		   	 			  		 			 	 	 		 		 	
    :type rar: float  		  	   		   	 			  		 			 	 	 		 		 	
    :param radr: Random action decay rate, after each update, rar = rar * radr. Ranges between 0.0 (immediate decay to 0) and 1.0 (no decay). Typically 0.99.  		  	   		   	 			  		 			 	 	 		 		 	
    :type radr: float  		  	   		   	 			  		 			 	 	 		 		 	
    :param dyna: The number of dyna updates for each regular update. When Dyna is used, 200 is a typical value.  		  	   		   	 			  		 			 	 	 		 		 	
    :type dyna: int  		  	   		   	 			  		 			 	 	 		 		 	
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		   	 			  		 			 	 	 		 		 	
    :type verbose: bool  		  	   		   	 			  		 			 	 	 		 		 	
    """  		  	   		   	 			  		 			 	 	 		 		 	
    def __init__(  		  	   		   	 			  		 			 	 	 		 		 	
        self,  		  	   		   	 			  		 			 	 	 		 		 	
        num_states=100,  		  	   		   	 			  		 			 	 	 		 		 	
        num_actions=4,  		  	   		   	 			  		 			 	 	 		 		 	
        alpha=0.2,  		  	   		   	 			  		 			 	 	 		 		 	
        gamma=0.9,  		  	   		   	 			  		 			 	 	 		 		 	
        rar=0.5,  		  	   		   	 			  		 			 	 	 		 		 	
        radr=0.99,  		  	   		   	 			  		 			 	 	 		 		 	
        dyna=0,  		  	   		   	 			  		 			 	 	 		 		 	
        verbose=False,  		  	   		   	 			  		 			 	 	 		 		 	
    ):  		  	   		   	 			  		 			 	 	 		 		 	
        """  		  	   		   	 			  		 			 	 	 		 		 	
        Constructor method  		  	   		   	 			  		 			 	 	 		 		 	
        """  		  	   		   	 			  		 			 	 	 		 		 	
        self.verbose = verbose  		  	   		   	 			  		 			 	 	 		 		 	
        self.num_actions = num_actions
        self.num_states = num_states
        self.alpha = alpha
        self.gamma = gamma
        self.rar = rar
        self.radr = radr
        self.dyna = dyna

        self.s = 0  		  	   		   	 			  		 			 	 	 		 		 	
        self.a = 0

        # Initialize Q table, a 2-d array with all zeros
        self.Q = np.zeros(shape=(num_states, num_actions))

        # Initialize transition count table from (s, a) to s_prime for Dyna-Q
        self.T = np.zeros(shape=(num_states, num_actions, num_states))

        # Initialize reward table for (s, a) for Dyna-Q
        self.R = np.zeros(shape=(num_states, num_actions))


    def Q_update(self, s, a, s_prime, r):
        '''
        Updating the Q-table with the experience tuple <s, a, s_prime, r>
        :param s: The current state
        :type  s: int
        :param a: The action taken to get to the next state
        :type a: int
        :param s_prime: The next state
        :type s_primte: int
        :param r: The immediate reward
        :type r: float
        :return: An updated Q-table of num_states rows and num_actions columns
        :rtype: A 2-d, num_states x num_actions array
        '''
        self.Q[s, a] = (1 - self.alpha) * self.Q[s, a] + \
                  self.alpha * (r + self.gamma * self.Q[s_prime, np.argmax(self.Q[s_prime])])
        return self.Q

  		  	   		   	 			  		 			 	 	 		 		 	
    def querysetstate(self, s):
        """  		  	   		   	 			  		 			 	 	 		 		 	
        Update the state without updating the Q-table  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
        :param s: The current state
        :type s: int  		  	   		   	 			  		 			 	 	 		 		 	
        :return: The selected action (whether a random action or np.argmax(self.Q[s,:])
        :rtype: int  		  	   		   	 			  		 			 	 	 		 		 	
        """  		  	   		   	 			  		 			 	 	 		 		 	
        self.s = s

        # Generate a random floating number between 0.0 and 1.0
        prob = rand.uniform(0.0, 1.0)

        # If the probability is less than rar, choose a random action from the column indices[i.e. from 0 to (num_actions)-1]
        if prob <= self.rar:
            self.a = rand.randint(0, self.num_actions -1)
        else:
            # indices of the maximum elements in the Q-table
            self.a = np.argmax(self.Q[s])

        if self.verbose:  		  	   		   	 			  		 			 	 	 		 		 	
            print(f"s = {self.s}, a = {self.a}")
        return self.a


    def query(self, s_prime, r):  		  	   		   	 			  		 			 	 	 		 		 	
        """  		  	   		   	 			  		 			 	 	 		 		 	
        Update the Q table and return an action
        
        Formula to calculate the new values of Q is as follows: 
        Q′[s,a]=(1−α)Q[s,a]+α(r+γQ[s′,argmaxa′(Q[s′,a′])])		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
        :param s_prime: The new state  		  	   		   	 			  		 			 	 	 		 		 	
        :type s_prime: int  		  	   		   	 			  		 			 	 	 		 		 	
        :param r: The immediate reward  		  	   		   	 			  		 			 	 	 		 		 	
        :type r: float  		  	   		   	 			  		 			 	 	 		 		 	
        :return a: The selected action 		   	 			  		 			 	 	 		 		 	
        :rtype: int 	   		   	 			  		 			 	 	 		 		 	
        """
        # Update the Q-table using the experience tuple
        self.Q_update(self.s, self.a, s_prime, r)

        # Per the lecture, if dyna is specified, dyna is greater than 0.
        if self.dyna > 0:
            # Update the transition T and reward R tables
            self.T[self.s, self.a, s_prime] += 1
            self.R[self.s, self.a] = (1 - self.alpha) * self.R[self.s, self.a] + self.alpha * r

            for i in range(self.dyna):
                self.run_hallucination()

        self.s = s_prime
        # Roll the dice to see if you draw an action from the transition model or random action with
        # probability
        p = rand.uniform(0.0, 1.0)
        if p <= self.rar:
            self.a = rand.randint(0, self.num_actions - 1)
        else:
            self.a = np.argmax(self.Q[s_prime])
        self.rar *= self.radr

        return self.a


    def run_hallucination(self):
        '''
             Hallucinate the experience tuple after learning about model T and R

             :return: The updated Q-table using the experience tuple
        '''
        # Randomly select a state and an action
        h_s = rand.randint(0, self.num_states - 1)
        h_a = rand.randint(0, self.num_actions - 1)

        # Infer s_prime from T by drawing from the one with the highest probability
        h_s_prime = np.argmax(self.T[h_s, h_a])

        # Compute r from simulated actions of s and a via R[s, a]
        r  = self.R[h_s, h_a]

        # Update the Q-table using the experience tuple
        self.Q_update(h_s, h_a, h_s_prime, r)


    def author(self):
        return 'lsoh3'


if __name__ == "__main__":  		  	   		   	 			  		 			 	 	 		 		 	
    print("Remember Q from Star Trek? Well, this isn't him")  		  	   		   	 			  		 			 	 	 		 		 	
