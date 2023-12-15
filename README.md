# ER-Force Framework Reinforcement Learning Interface 

This repo contains a Python based interface for reinforcement learning with the [ER-Force Framework](https://github.com/robotics-erlangen/framework) for SSL robot soccer simulation.

## Getting started
First set up an instance of the ER-Force Framework. Then the Python script will be able to connect to the team/world control sockets. Make sure the websocket ports are set to the same values for both programs.

To install the requirements for the RL interface run the following command in this directory:
```Shell
python -m pip install -e .
```

Then you will be able to use the command line interface as follows:
```Shell
rtt-rl <command>
```

For example to initialize the field with five robots on each team:
```Shell
rtt-rl init --robots 5
```
This will move any necessary players off the field and reset the ball to the center.