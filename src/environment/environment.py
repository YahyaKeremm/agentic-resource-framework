import numpy as np

class Environment:
    def __init__(self, N=3):
        self.N = N # numSlices
        self.C_total = 1 # total capacity
        self.eps = 1e-5

    def compute_service_rates(self, allocation):
        return [self.C_total * a for a in allocation]
    
    def compute_metrics(self, lam, mu):
        metrics = {}

        utilization = []
        throughput = []
        delay = []
        loss = []

        for i in range(self.N):

            u = lam[i] / (mu[i] + self.eps)
            utilization.append(u)

            th = min(lam[i], mu[i])
            throughput.append(th)

            delay_ = 1/ np.maximum(mu[i]-lam[i], self.eps)
            delay.append(delay_)

            loss.append(max(0, u - 1))

        fairness = (sum(throughput)**2) / ( self.N * sum(x**2 for x in throughput) + self.eps )

        metrics["delay"] = delay
        metrics["throughput"] = throughput
        metrics["loss"] = loss
        metrics["utilization"] = utilization
        metrics["fairness"] = fairness

        return metrics
    
    def step(self, allocation, demand):
        lam = demand
        mu = self.compute_service_rates(allocation)
        metrics = self.compute_metrics(lam, mu)
        return metrics