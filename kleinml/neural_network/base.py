"""
Author: Kexuan Zou
Date: June 22, 2018
Reference: https://github.com/eriklindernoren/ML-From-Scratch/blob/master/mlfromscratch/deep_learning/activation_functions.py
"""

import numpy as np

class Loss(object):
    def loss(self, y_true, y_pred):
        raise NotImplementedError

    def gradient(self, y_true, y_pred):
        raise NotImplementedError


class SquareLoss(Loss):
    def __init__(self):
        pass

    def loss(self, y_true, y_pred):
        return 0.5*np.square(y_true - y_pred)

    def gradient(self, y_true, y_pred):
        return y_pred - y_true


class CrossEntropy(Loss):
    def __init__(self):
        pass

    def loss(self, y_true, y_pred):
        y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)
        return -y_true*np.log(y_pred) - (1 - y_true)*np.log(1 - y_pred)

    def gradient(self, y_true, y_pred):
        y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)
        return (y_true - y_pred)/((y_pred - 1.)*y_pred)


class Sigmoid(object):
    def __call__(self, x):
        return 1./(1. + np.exp(-x))

    def gradient(self, x):
        return self.__call__(x)*(1 - self.__call__(x))


class Softmax(object):
    def __call__(self, x):
        e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
        return e_x/np.sum(e_x, axis=-1, keepdims=True)

    def gradient(self, x):
        return self.__call__(x)*(1 - self.__call__(x))


class ReLU(object):
    def __call__(self, x):
        return np.where(x >= 0, x, 0)

    def gradient(self, x):
        return np.where(x >= 0, 1, 0)


class TanH(object):
    def __call__(self, x):
        return 2./(1. + np.exp(-2*x)) - 1.

    def gradient(self, x):
        return 1. - np.square(self.__call__(x))
