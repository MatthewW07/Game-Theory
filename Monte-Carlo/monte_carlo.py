
import numpy as np
import matplotlib.pyplot as plt

# General Monte Carlo Class
class MonteCarlo:
    def __init__(self, trial_function: callable, n: int=100, trials: int=100, label: str=None):
        # Number of samples per trial
        self.n = n

        # Number of trials
        self.trials = trials

        # The user must create and pass in a function to represent a single trial
        self.trial_function = trial_function

        # To store the results of all the trials
        self.estimates = None

        # The user can specify what the estimated value represents
        self.label = label


    # Simulate all the trials
    def simulate_trials(self):
        estimates = np.array([self.trial_function(n=self.n) for _ in range(self.trials)])

        # Store the result of the first trial
        if self.estimates == None:
            self.estimates = estimates

        return estimates


    # Plot the results with a line plot and a histogram
    def plot_results(self):
        estimates = self.estimates if self.estimates is not None else self.simulate_trials()

        print(f"Average: {estimates.mean()}")
        print(f"Standard Dev: {estimates.std(ddof=1)}")

        plt.figure(figsize=(10, 5))
        """Line Plot"""
        # plt.plot(range(1, self.trials+1), estimates, marker="o", linestyle="-", label="Estimate")

        """Histogram"""
        plt.hist(estimates, bins=40, edgecolor="black")

        plt.xlabel("Trial")
        plt.ylabel(f"Value {''.join(["of ", self.label]) if self.label is not None else ''}")
        plt.title(f"Monte Carlo Estimation - n={self.n}, trials={self.trials}")
        plt.legend()
        plt.show()
