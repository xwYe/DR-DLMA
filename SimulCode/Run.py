from env import ENVIRONMENT
from Brain import DQN
import numpy as np
import time
import random

def main(max_iter):
    start = time.time() # record time
    agent_reward_list = [] # record agent reward
    TDMA_reward_list = []
    reward_list = [] # record total reward
    agent_state_list = []
    agent_action_list = []
    state = env.reset()
    counter2 = 0
    a = 0

    for i in range(max_iter):
        agent_action = dqn_agent.choose_action(state)
        observation_, reward, agent_reward, TDMA_reward = env.step(agent_action)

        if i < env.DRL_delay * 2 - 1:
            next_state = env.reset()
        else:
            next_state = np.concatenate([agent_state_list[counter2][2:], [agent_action_list[counter2], observation_]])
            counter2 += 1

        if i >= env.DRL_delay * 2 - 1:
            dqn_agent.store_transition(state, agent_action, reward, next_state)

        agent_state_list.append(state)
        agent_action_list.append(agent_action)

        agent_reward_list.append(agent_reward) # store agent reward
        TDMA_reward_list.append(TDMA_reward) # store TDMA reward
        reward_list.append(reward) # store total reward

        # --------------------------------------------------------------------------------------------------------------
        # We omit the adaptive training mechanism here.
        # --------------------------------------------------------------------------------------------------------------

        if i > 200 and a == 0:
            dqn_agent.learn()

        state = next_state

        print(i)

    with open('rewards/agent_len5e4_M40.txt', 'w') as my_agent:
        for i in agent_reward_list:
            my_agent.write(str(i) + '   ')
    with open('rewards/TDMA_len5e4_M40.txt', 'w') as my_TDMA:
        for i in TDMA_reward_list:
            my_TDMA.write(str(i) + '   ')

    print('-----------------------------') # Calculate the average of the last 2000 time slots
    print('average agent reward: {}'.format(np.mean(agent_reward_list[-2000:])))
    print('average TDMA reward:  {}'.format(np.mean(TDMA_reward_list[-2000:])))
    print('average total reward: {}'.format(np.mean(agent_reward_list[-2000:]) + np.mean(TDMA_reward_list[-2000:])))
    print('Time elapsed:', time.time() - start) # Print computer run time


if __name__ == "__main__":
    env = ENVIRONMENT(state_size=60)

    dqn_agent = DQN(env.state_size, # the number of DRL state
                    env.n_actions, # the number of DRL action
                    env.n_nodes, #  the number of nodes
                    state_action_memory_size=2*(env.DRL_delay), memory_size=500, replace_target_iter=200, batch_size=32, learning_rate=0.01,
                    gamma=0.95, epsilon=0.1, epsilon_min=0.001, epsilon_decay=0.996,
                    )
    main(max_iter=50000) # run 50000 time slots