import numpy as np

TDMA_delay = 8 # set TDMA delay
DRL_delay = 5 # set DRL delay
delay_tag = TDMA_delay - DRL_delay
DRL_action_length = 30
TDMA_counter = 0

class ENVIRONMENT(object):
    """docstring for ENVIRONMENT"""

    def __init__(self, state_size=10):
        self.state_size = state_size
        self.action_space = ['w', 't']  # wait transmit
        self.n_actions = len(self.action_space)
        self.n_nodes = 2
        self.TDMA_delay = TDMA_delay
        self.DRL_delay = DRL_delay
        self.delay_tag = delay_tag
        self.agent_reward_list = []
        self.tdma_reward_list = []
        self.reward_list = []
        self.DRL_observation_list = []
        self.observation_reward_counter = 0

        self.action_list = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # case 1

    # reset state
    def reset(self):
        init_state = np.zeros(self.state_size, int)
        return init_state

    def step(self, action):
        global TDMA_counter
        tdma_reward = 0
        agent_reward = 0
        reward = 0
        observation_ = 0

        if self.delay_tag > 0: # When TDMA node is farther from AP than DRL node
            if self.action_list[TDMA_counter - self.delay_tag] == 1:
                TDMA_action = 1
            else:
                TDMA_action = 0
        else:
            if self.action_list[TDMA_counter - self.delay_tag-10] == 1:
                TDMA_action = 1
            else:
                TDMA_action = 0

        if action == 1: # DRL node chooses to transmit
            if TDMA_action == 1:
                # print('collision')
                observation_ = -1 # tx, no success
            else:
                # print('agent success')
                reward = 1
                agent_reward = 1
                observation_ = 1  # tx, success
        else:
            if TDMA_action == 1:
                # print('tdma success')
                reward = 1
                tdma_reward = 1
                observation_ = 2  # no tx, success
            else:
                # print('idle')
                observation_ = -2  # no tx, no success

        TDMA_counter += 1
        if TDMA_counter == len(self.action_list):
            TDMA_counter = 0

        self.agent_reward_list.append(agent_reward)
        self.tdma_reward_list.append(tdma_reward)
        self.reward_list.append(reward) # store total reward
        self.DRL_observation_list.append(observation_) # store DRL node observation
        self.observation_reward_counter += 1
        if self.observation_reward_counter >= 2 * self.DRL_delay:
            counter11 = self.observation_reward_counter - (2 * self.DRL_delay)
            return self.DRL_observation_list[counter11], self.reward_list[counter11], self.agent_reward_list[counter11], self.tdma_reward_list[counter11]
        else:
            return 0, 0, 0, 0