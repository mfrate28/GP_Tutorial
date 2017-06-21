import george
import numpy as np

#mean function. You can write your own mean function and change the input parameters accordingly
from george.modeling import ModelingMixin
class Mean(ModelingMixin):
    def __init__(self, params):
        self.p0=params[0]
        self.p1=params[1]
        self.p2=params[2]
    def get_value(self, t):
        sqrts = 13000.
        return (self.p0 * (1.-t/sqrts)**self.p1 * (t/sqrts)**(self.p2))*np.append(np.diff(t), np.diff(t)[-1])
    
#kernel function. ExpSquaredKernel is a standard programmed kernel in george. You can choose a programmed kernel in george or write your own and import it here
from george.kernels import ExpSquaredKernel
def Kernel(hyperparams):
    return hyperparams[0]*ExpSquaredKernel(hyperparams[1])
