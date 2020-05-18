# A introduction to DR-DLMA
We put forth a new deep reinforcement learning algorithm, referred to as delayed-reward deep Q-network (DR-DQN). 
Then we use this algorithm to design a new medium access control (MAC) protocol for underwater acousitc networks (UWANs) with large propagation latency, called DR-DLMA. 
# About 1.pdf
This is a supplementary document to pur paper: Deep Reinforcement Learning Based MAC Protocol for Underwater Acoustic Networks. In this document, we give the optimal network throughput when the DR-DLMA node coexists with nodes using other protocols, then we use the optimal network throughput as the benchmark in our paper.
# How to use the codes
There are three main files in each folder, simulating the interactions of DR-DLMA node with other nodes.   
## Run.py
This is the main framework, and you can run this file to start the simulation.   
## Env.py
It simulates the environment in which the DR-DLMA nodes interact with the nodes using other protocols.   
## Brain.py
This is the main framework of the DR-DLMA node, which contains the DR-DQN algorithm.
# Partly open-sourced
Currently, only the simulation codes of the coexistence of one DR-DLMA node and one TDMA node in UWANs with no-negligible long propagation delay are provided. 
In addition, the simulation codes we give does not contain our proposed adaptive deep neural network (DNN) training mechanism.
More simulation codes will be available after our paper gets accepted.
