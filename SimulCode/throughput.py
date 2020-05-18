import numpy as np
import matplotlib.pyplot as plt


def my_plot(file1, file2):
	max_iter = 50000
	N = 2000

	# load reward
	agent_reward = np.loadtxt(file1)
	tdma_reward = np.loadtxt(file2)

	throughput_agent = np.zeros((1, max_iter))
	throughput_tdma = np.zeros((1, max_iter))
	total_optimal = np.ones(max_iter)* 1

	agent_temp_sum = 0
	tdma_temp_sum = 0
	for i in range(0, max_iter):
		if i < N:
			agent_temp_sum += agent_reward[i]
			tdma_temp_sum  += tdma_reward[i]
			throughput_agent[0][i] = agent_temp_sum / (i+1)
			throughput_tdma[0][i]  = tdma_temp_sum / (i+1)
		else:
			agent_temp_sum += agent_reward[i] - agent_reward[i-N]
			tdma_temp_sum  += tdma_reward[i] - tdma_reward[i-N]
			throughput_agent[0][i] = agent_temp_sum / N
			throughput_tdma[0][i]  = tdma_temp_sum / N

	total_line, = plt.plot(throughput_agent[0]+throughput_tdma[0], color='green', lw=1.2, label='total')

	total_optimal_line,  = plt.plot(total_optimal, color='green', lw=2, label='total optimal')

	plt.xlim((0, max_iter))
	plt.ylim((-0.05, 1.05))
	plt.grid()
	plt.legend(handles=[total_line, total_optimal_line], loc='best')


for i in range(1, 2):
	plt.figure(i)
	my_plot('rewards/agent_len5e4_M40.txt',
		    'rewards/TDMA_len5e4_M40.txt')
plt.show()


