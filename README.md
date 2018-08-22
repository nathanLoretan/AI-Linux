# AI-Linux - University of Glasgow, MSc Project

AI-Linux is a research project that tries to implement an Artificial Intelligence within the kernel of an operating system, In this case, the Linux kernel. 

The objective of this project is to design artificial agents that would change their behaviour regarding the utilization of the kernel. The design is focus on three parts of the kernel (process scheduler, load balance and page frame reclaiming algorithm). 

All the agents use reinforcement learning (action, state, rewards) to learn the best way to complete their tasks during the execution of the kernel. For this project, the environment is considered to be dynamic. Hence, the number of processes running, their priority, the pages used are unknown and the state space and action space are constantly changing. Therefore, the design is focus on developing value function approximation to determine the Q-Value function of a state and an action based on different features to select the best move to do. 

The results show that the agents can adapt its behaviour differently regarding the type of environment, resources used and processes running on the Operating Systems by giving different weights to the features selected. However, the measurements where performed in a controlled environment with a well-defined number of processes and action to execute. Further work has now to be done to test the design in a more real-world environment and to finally measure the actual performances of the design to fully evaluate it.
