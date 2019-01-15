import numpy as np




class Agent():
    '''
    An Agent that learns by tabular Q - learning
    As input it only need the number of possible actions to play
    
    New states while be dynamically added to the matrix and will make use of a translation dictionary.
    This dictriony goed from state to matrix index (This proves faster than using the loc function and a DataFrame)
    
    Learning method:
    Updating rule is a temporal difference approach
    Q(s,a) = Q(s,a) + lr * ( rew + discount * [max_{a'} Q(s',a')]- Q(s,a))
    
    Policy:
    A epsilon greedy policy, for a specific state add noise to the state_action values, then pick the biggest one.
    This noise introduces a from of exploration
    This noise can be changed using the explore_decay attribute (0 a lot of noise to 'bignumber' little noise)
    '''

    def __init__(self, num_actions,  learn_rate = 0.8, gamma = .95):
        self.num_actions = num_actions
        self.lr = learn_rate
        self.gamma = gamma
        self.explore_decay = 0

        self.action = 0
        self.state = 0
        self.num_states = 0
    
        self.state_dict = {}

        # Define the Q-table
        self.val_table = np.zeros((1,num_actions))
    
    def next_action(self, state):
        # Get the index of the state
        s = self.get_state_index(state)

        # Retrieve the new action    
        a = np.argmax(self.val_table[s] + np.random.randn(self.num_actions)*(1./(self.explore_decay+1)))  
    
        # Remember the state we saw and the action we have taken
        # We need this for the update rule
        self.state = s
        self.action = a
        return a
      
    def get_state_index(self, state):
        # From the state get the matrix row index. 
        # If it does not exists append a new row to the matrix

        try:
            s = self.state_dict[state]
      
        except KeyError:
            self.state_dict[state] = self.num_states
            self.val_table = np.append(self.val_table, [[0]*self.num_actions], axis = 0)
            self.num_states += 1
      
            s = self.state_dict[state]
        return s
    
  
    def update(self, reward, new_state):
        # This coincides with the Q-learning Algorithm 9 from the slides
        
        # Previous state and action
        a = self.action
        s = self.state
        
        # Index of new state
        s_prime = self.get_state_index(new_state)

        prev_val = self.val_table[s,a]
        
        update_val = reward + self.gamma*np.max(self.val_table[s_prime])- prev_val
    
        # Update the value in the table
        self.val_table[s,a] = prev_val+self.lr*update_val