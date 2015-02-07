__author__ = 'gabriel'

import numpy as np
import tracks
from sklearn.grid_search import GridSearchCV
from sklearn.neighbors import KernelDensity

class Prior(object):

    def prior_function(self, x):
        raise NotImplementedError()

    def __call__(self, x, *args, **kwargs):
        return self.prior_function(x)


class KdePrior(Prior):

    def __init__(self, data):
        self.data = np.array(data)


if __name__ == '__main__':

    data = np.random.randn(100)
    grid = GridSearchCV(KernelDensity(),
                        {'bandwidth': np.linspace(0.1, 1.0, 30)},
                        cv=20
    ) # 20-fold cross-validation
    grid.fit(data[:, None])
    print grid.best_params_