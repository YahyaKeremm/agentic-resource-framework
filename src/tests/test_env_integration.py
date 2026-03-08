import numpy as np
import matplotlib.pyplot as plt
from time import time
from ..environment.environment import Environment
from ..traffic.generator import burst, periodic

env = Environment(N=3)

allocation = np.array([0.33, 0.33, 0.34])
allocation2 = np.array([0.37, 0.32, 0.31])
allocation3 = np.array([0.39, 0.34, 0.27])
allocation4 = np.array([0.41, 0.36, 0.23])
# allocs = [allocation, allocation2]
allocs = [allocation, allocation2, allocation3, allocation4]

# seed = int(time())
seed = 0

bases = [0.35, 0.25, 0.1]
# traffic = burst(50, bases, seed) # slice0 : 0.35 -> 0.40, slice2 : 0.1 -> 0.15
traffic = periodic(50, bases, seed)

fns = []
for x in range(4):

    delays = []
    throughputs = []
    losses = []
    utils = []
    fairnesses = []
    for t in range(50):
        demand = traffic[t]

        # metrics = env.step(allocation, demand)
        metrics = env.step(allocs[x], demand)

        # print("t:", t)
        # print("demand:", demand[t])
        # print("delay:", metrics["delay"])
        # print("loss:", metrics["loss"])
        # print("throughput:", metrics["throughput"])
        # print()
        # print()
        
        # metrics.append(metric)
        delays.append(metrics["delay"])
        throughputs.append(metrics["throughput"])
        losses.append(metrics["loss"])
        utils.append(metrics["utilization"])
        fairnesses.append(metrics["fairness"])

    delays = np.array(delays)
    throughputs = np.array(throughputs)
    losses = np.array(losses)
    utils = np.array(utils)
    fairnesses = np.array(fairnesses)
    fns.append(fairnesses)

    plt.figure()
    plt.plot(delays[:,0], label="slice0")
    plt.plot(delays[:,1], label="slice1")
    plt.plot(delays[:,2], label="slice2")
    plt.title("Delay")
    plt.legend()

    # plt.figure()
    # plt.plot(traffic[:,0], label="lambda0")
    # plt.axhline(allocation[0], linestyle="--", label="capacity0")
    # plt.legend()
    # plt.title("Demand vs Capacity")

    plt.figure()
    plt.plot(utils[:,0], label="slice0")
    plt.plot(utils[:,1], label="slice1")
    plt.plot(utils[:,2], label="slice2")
    plt.axhline(1, linestyle="--")
    plt.title("Utilization")
    plt.legend()

    plt.figure()
    plt.plot(fairnesses, label="slice0")
    plt.title("Fairness")
    plt.ylim(0,1.05)

# plt.figure()
# plt.subplot(3, 1, 1)
# plt.plot(fns[0], label="1st Iteration")
# plt.plot(fns[1], label="2nd Iteration")
# plt.title("Fairness Over Iterations")
# plt.legend()
# plt.subplot(3, 1, 2)
# plt.plot(fns[1], label="2nd Iteration")
# plt.plot(fns[2], label="3rd Iteration")
# plt.title("Fairness Over Iterations")
# plt.legend()
# plt.subplot(3, 1, 3)
# plt.plot(fns[2], label="3rd Iteration")
# plt.plot(fns[3], label="4th Iteration")
# plt.title("Fairness Over Iterations")
# plt.legend()

plt.show()