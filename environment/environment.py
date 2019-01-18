'''
Make an environment class that uses the system class

To be similar as Open AI gym me make functions

env.make('env_string'):
    - This initialises the environment and returns the environment object
    (so this deviates a bit from the gym idea where the make in not a function of the environment)

env.reset():
    - This should reset the environment to the initial state
    and outputs the initial state

env.step(a)
    - Perform action a
    - Return new_state, reward, whether we are done, some dictionairy we never actually seem to use

'''
from environment.system import System



class environment():
    def __init__(self, ):
        env = System(brick_ip='ev3dev.local', get_state_mode='dict')
        env.get_state()
        env.get_action_space()

    def reset(self):
        # stop current action

        # Go to initial state

        # return state
        return None

    def step(self, action):
        # give the action to the motors

        # run for 1 sec
        # while 1 sec
        # - measure color 5/10 times
        # - check saying whether in the field (using classifier)
        # - if not in field do somehting
        


        # set the speeds to zero or not
        return None

    