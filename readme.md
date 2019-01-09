What the idea is:
Make an agent that can follow the curve. Ideally train it on a line and test is on a different curve

Input/Output:
- The motors will run constantly using the 'run_direct' command.
- The output/actions will change `the duty_cycle_sp` parameter of the individual motors.
- As input the network will take
  - The angles of the motors (dicretized) so that it can learn the effect of the actions when the arms are in certain positions
  - A sequence of gray values (averaged RGB), so that is has a history of what it has seen. 


The specific architecture is still to be decided.
