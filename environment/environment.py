from environment.system import System
import collections
import utils
import numpy as np
import time

from .config import ENVIRONMENT_CONFIG


class Environment():
    '''
    Make the environment object for the lego constuction

    Parameters
    ----------
    field_classifier : str
        The location of the field classifier
    reward_classifier : str
        Location of the line classifier
    get_reward_function : func
        Function that takes a queue of rewards and aggregates them
    get_state_function : func
        Function that has a queue as input (containing angles and color) and outputs the wanted state
    '''

    def __init__(self, field_classifier, reward_classifier, get_reward_function, get_state_function, state_queue_len=10):
        self.system = System(brick_ip='ev3dev.local', get_state_mode='dict')
        self.field_classifier = utils.load_pickle(field_classifier)
        self.reward_classifier = utils.load_pickle(reward_classifier)
        self.opposite_action = {0:3,1:2,2:1,3:0}
        self.opposite_action = {i: self.action_space-i-1 for i in range(self.action_space)}
        
        self.on_field = True
        self.border_count = 0
#         self.color_on = color_on
        
        self.state_queue = collections.deque(maxlen=state_queue_len)
        self.reward_queue = collections.deque(maxlen=state_queue_len)
        
        self.get_reward_function = get_reward_function
        self.get_state_function = get_state_function
        
        for _ in range(state_queue_len):
            self._new_state()
        
    def reset(self):
        # stop current action
        self.system.reset()
        # Go to initial state

        # return state
#         return self.prepro([self.state])
      
    def go_to_init_state(self):
        print('#'*30)
        print('Going to Init')
        print('#'*30)
        self.system.go_to_init_state()
#         time.sleep(3)
    
    @staticmethod
    def _color_from_one_state(s):
        return s[:3]
        
    def _environment_checks(self):
        # access color information from the last measurement 
        # according to self.new_state() ordering
        color = self._color_state_for_classifier
        
        if self.field_classifier.predict(color) == [0]:
            print('I am outside')
            self.border_count += 1

            if ENVIRONMENT_CONFIG['bouncing']:
                if self.on_field:
                    self.system.perform_actions([self.opposite_action[a] for a in self.current_action])
                    print('BOUNCIN!!1')
                    time.sleep(1)

            else:
                self.go_to_unit_state()

            self.on_field = False

        else:
            self.on_field = True
    
        if self.border_count == 3:
            self.go_to_init_state()
            self.border_count = 0
            
    @property
    def _color_state_for_classifier(self):
        return np.array([self._color_from_one_state(s) for s in list(self.state_queue)[-2:]]).reshape(1,-1)
            
    def _new_reward_approx(self):
        def transform_proba_into_reward_approx(proba):
            return np.max([0., 5. * (proba - 0.3)])
            
        # Predict propba
        if not self.on_field:
            return -10
        
        colors = self._color_state_for_classifier
#         r = (np.argmax(self.reward_classifier.predict_proba(x), axis = 1) == 1).sum()
        # sum the probabilities of black class and compute a function of it
        black_proba = self.reward_classifier.predict_proba(colors)[:,1][0]
        
        self.reward_queue.append(transform_proba_into_reward_approx(black_proba))
        
    def _new_state(self):
        s = self.system.get_state()
        color = s['cs'][0]
        top_pos = s['top'][0]
        bot_pos = s['bot'][0]
        self.state_queue.append((*color, top_pos, bot_pos))
        
    def _cycle(self, is_free_cycle):
        if not is_free_cycle:
            print("Performing action", self.current_action)
            self.system.perform_actions(self.current_action)
        
        # gets new states and puts it in the queue
        self._new_state()
        
        # environment specific checks like is it still in the field
        self._environment_checks()
        
        # calculate the reward 
        self._new_reward_approx()
        
    def step(self, action, free_cycles=ENVIRONMENT_CONFIG['free_cycle']):
        self.current_action = action
        self._cycle(False)  
        for _ in range(free_cycles):
            self._cycle(True)
        return self.state, self.reward, False, {}
    
    @property
    def reward(self):
        return self.get_reward_function(self.reward_queue)
        
    @property
    def state(self):
        return self.get_state_function(self.state_queue)
    
    @property
    def action_space(self):
        return len(self.system.get_action_space()[0])

    