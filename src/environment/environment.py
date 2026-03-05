class Metrics:
    def __init__(self, N):
        self.delay = [0]*N
        self.throughput = [0]*N
        self.loss = [0]*N
        self.utilization = [0]*N
        self.fairness = 0.0

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

            if (lam[i] < mu[i]):
                delay.append(1 / (mu[i] - lam[i] + self.eps))
            else:
                delay.append(float("inf"))

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

    # def step(self, allocation, demand):
    #     metrics = Metrics(self.N)

    #     mu = [0]*self.N
    #     lam = [0]*self.N
    #     for i in range(self.N):
    #         mu[i] = self.C_total * allocation[i]
    #         lam[i] = demand[i]

    #         metrics.utilization[i] = lam[i] / (mu[i] + self.eps)
    #         metrics.throughput[i] = min(lam[i], mu[i])
    #         if (lam[i] < mu[i]):
    #             metrics.delay[i] = 1 / (mu[i] - lam[i] + self.eps)
    #         else:
    #             metrics.delay[i] = "OVERLOAD"
    #         metrics.loss[i] = max(0, metrics.utilization[i] - 1)
    #     metrics.fairness = (sum(metrics.throughput)**2) / (self.N * sum(x**2 for x in metrics.throughput) + self.eps)