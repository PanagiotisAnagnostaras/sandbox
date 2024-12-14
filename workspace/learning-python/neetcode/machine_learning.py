# https://neetcode.io/practice
## https://neetcode.io/problems/gradient-descent
class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        cur_val = init
        while iterations>0:
            iterations-=1
            cur_val += - learning_rate*(2*cur_val)
        return round(cur_val,5)

## https://neetcode.io/problems/linear-regression-forward
import numpy as np
from numpy.typing import NDArray


# Helpful functions:
# https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
# https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# https://numpy.org/doc/stable/reference/generated/numpy.square.html

class Solution:
    
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is an Nx3 NumPy array
        # weights is a 3x1 NumPy array
        # HINT: np.matmul() will be useful
        # return np.round(your_answer, 5)
        return np.round(np.matmul(X, weights),5)


    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # model_prediction is an Nx1 NumPy array
        # ground_truth is an Nx1 NumPy array
        # HINT: np.mean(), np.square() will be useful
        # return round(your_answer, 5)
        return round(np.mean(np.square(model_prediction-ground_truth)), 5)

## https://neetcode.io/problems/linear-regression-training
import numpy as np
from numpy.typing import NDArray


class Solution:
    def get_derivative(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64], N: int, X: NDArray[np.float64], desired_weight: int) -> float:
        # note that N is just len(X)
        return -2 * np.dot(ground_truth - model_prediction, X[:, desired_weight]) / N

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.squeeze(np.matmul(X, weights))

    learning_rate = 0.01

    def train_model(
        self, 
        X: NDArray[np.float64], 
        Y: NDArray[np.float64], 
        num_iterations: int, 
        initial_weights: NDArray[np.float64]
    ) -> NDArray[np.float64]:

        # you will need to call get_derivative() for each weight
        # and update each one separately based on the learning rate!
        # return np.round(your_answer, 5)
        weights = initial_weights
        for it in range(num_iterations):
            y_pred = self.get_model_prediction(X, weights)
            weights[0] -= self.learning_rate * self.get_derivative(y_pred, Y, len(X), X, 0)
            weights[1] -= self.learning_rate * self.get_derivative(y_pred, Y, len(X), X, 1)
            weights[2] -= self.learning_rate * self.get_derivative(y_pred, Y, len(X), X, 2)
        return np.round(weights, 5)
            