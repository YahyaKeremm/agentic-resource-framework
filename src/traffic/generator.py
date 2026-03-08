##################
# VALID PATTERNS
# 0 (DEFAULT): Steady Load
# 1: Burst Traffic
# 2: Periodic Spikes
# 3: Drifting Demand
##################

import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt


def generate(pattern: int = 0, T: int = 1000, bases: list = None, seed: int = 0):
    if (bases is None):
        bases = [0.3, 0.2, 0.1] # default N = 3 and demand load values
    
    match pattern:
        case 0:
            return steady(T, bases, seed)
        case 1:
            return burst(T, bases, seed)
        case 2:
            return periodic(T, bases, seed)
        case 3:
            return drifting(T, bases, seed)

    N = len(bases)
    pass


def steady(T: int, bases: list, seed: int) -> npt.NDArray:
    np.random.seed(seed)
    
    N = len(bases)
    d_t = []
    
    for i in range(T):
        d_s = []
        for j in range(N):
            noise = np.random.normal(0, 0.005)
            d_i = min(1, max(0.01, bases[j]+noise)) # demand is capped as 0.01 < d_i <= 1
            d_s.append(d_i)

        d_t.append(d_s)

    return np.array(d_t)

def burst(T: int, bases: list, seed: int, length: int = 25, period:float = 0.2) -> npt.NDArray: # PARAMETRELER EKLENECEK: SPIKE INTERVAL VE BELKI SPIKE NOKTASI VEYA SPIKE MIKTARI (SPIKE T BOYUNCA RANDOM DAGILACAK ONUN ICIN GUZEL BI FONKSIYON YAZMAK LAZIM)
    np.random.seed(seed)

    N = len(bases)

    count = int((T*period)/length)
    starts = np.random.uniform(0, T-length, (N,count)).astype(int)
    
    d_t = []
    spiker = [0]*N

    for i in range(T):
        d_s = []
        for j in range(N):
            if (i in starts[j]):
                spiker[j] = length

            spike = 0
            if (spiker[j]):
                spike = np.random.normal(bases[j], 0.03)
                spiker[j] -= 1
            
            noise = np.random.normal(0, 0.005)
            d_i = min(1, max(0.01, bases[j]+noise+spike))
            d_s.append(d_i)

        d_t.append(d_s)

    return np.array(d_t)

def periodic(T: int, bases: list, seed: int, amp: list = None, freqs: list = None) -> npt.NDArray: ## will use a sinusoidal
    np.random.seed(seed)

    N = len(bases)
    if (amp is None):
        amp = [i*1.15 for i in bases]
    if (freqs is None):
        freqs = [0.2*i for i in bases]

    phases = np.random.normal(0, 2*np.pi, N)

    d_t = []
    for i in range(T):
        d_s = []
        for j in range(N):
            noise = np.random.normal(0, 0.005)
            d_i = min(1, max(0.01, bases[j]+noise + amp[j]*np.sin(freqs[j]*i + phases[j])))
            d_s.append(d_i)

        d_t.append(d_s)
    
    return np.array(d_t)

def drifting(T: int, bases: list, seed: int) -> npt.NDArray:
    pass

def plot(traffic: npt.NDArray, capInSeperate: bool = False, capInTotal: bool = True):
    plt.figure()
    plt.plot(traffic)
    if (capInSeperate):
        plt.axhline(1)
        plt.text(5, 1.01, "Capacity")
    
    plt.figure()
    plt.plot(np.sum(traffic, axis=1))
    if (capInTotal):
        plt.axhline(1)
        plt.text(5, 1.01, "Capacity")

def draw():
    plt.show()

##############
# TO BE ADDED
# traffic_intensity parameter
# values will be:               "low"   |   "medium"    |   "high"
# mean traffic load would be:    0.5    |     0.75      |    0.90
#
# meaning a function to generate traffic baselines procedurally is necessary in the future for the research.
# e.g. everyday load is "medium" so the function will take the slice amount 4 and generate [0.3, 0.13, 0.22, 0.1]
# total steady baseline is 0.75 in this case
# possible solution:
# 1) 0.75 - rand(max=0.75 - some arbitrary epsilon) -> push to bases
# 2) 0.75 - bases[0] - rand(...) -> push to bases
# 3) 0.75 - bases[1] - bases[0] - rand(...) -> push to bases
# ...) and so on
##############

if __name__ == "__main__":
    bases = [0.15, 0.3, 0.2, 0.1]
    # print(steady(3, bases, 0))
    # print(steady(3, bases, 0))
    plot(steady(1000, bases, 0))
    # plot(burst(1000, bases, 0, 25, 0.2))
    # plot(periodic(1000, bases, 0, [0.2, 0.1, 0.05]))
    plot(periodic(1000, bases, 0))
    draw()