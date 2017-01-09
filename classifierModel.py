from pywt import wavedec
import numpy as np
import itertools
import math


class classifierModel:
    def __init__(self, eegData):
        self.data = eegData
        """self.d1 = np.array()
        self.d2 = np.array()
        self.d3 = np.array()
        self.d4 = np.array()
        self.a4 = np.array()"""

    def discreteWavelete(self):
        coeffs = wavedec(self.data, 'db3', level=4)
        cA4, cD4, cD3, cD2, cD1 = coeffs

        return cA4, cD4, cD3, cD2, cD1

    def permutation_entropy(self, time_series, m, delay):
        n = len(time_series)
        permutations = np.array(list(itertools.permutations(range(m))))
        c = [0] * len(permutations)

        for i in xrange(n - delay * (m - 1)):
            # sorted_time_series =    np.sort(time_series[i:i+delay*m:delay], kind='quicksort')
            sorted_index_array = np.array(np.argsort(time_series[i:i + delay * m:delay], kind='quicksort'))
            for j in xrange(len(permutations)):
                if abs(permutations[j] - sorted_index_array).any() == 0:
                    c[j] += 1
        # print "sorted: ", sorted_index_array.array()
        c = [element for element in c if element != 0]
        # print "c: ", c

        p = np.divide(np.array(c), float(sum(c)))
        # print "p: ",p

        pe = -sum(p * np.log(p))
        return pe

    def weightedPermutationEntropy(self, timeSeries, m, delay):
        n = len(timeSeries)
        permutations = np.array(list(itertools.permutations(range(m))))
        c = [0] * len(permutations)

        for i in xrange(n - delay * (m - 1)):
            # sorted_time_series =    np.sort(time_series[i:i+delay*m:delay], kind='quicksort')
            sorted_index_array = np.array(np.argsort(timeSeries[i:i + delay * m:delay], kind='quicksort'))
            for j in xrange(len(permutations)):
                if abs(permutations[j] - sorted_index_array).any() == 0:
                    c[j] += 1
        # print "sorted: ", sorted_index_array.array()
        c = [element for element in c if element != 0]
        # print "c: ", c

        """sumX = 0
        for k in range(1, m):
            subscript = (k + 1) * delay
            sumX = sumX + timeSeries[subscript - 1]
        xBar = float(sumX / m)"""
        xBar = sum(c)/m

        subscript = 0
        wbefore = 0
        """for i in xrange(1, m):
            subscript = (k + 1) * delay
            wbefore = wbefore + (self.data[subscript - 1] - xBar) ** 2
        wReal = float(wbefore / m)"""
        xj = np.array(c)
        variance = xj - xBar
        wbefore = sum(variance**2)
        """
        for i in range(1,m):
            wbefore = wbefore + (c-xBar)**2"""
        wReal = float(wbefore/m)
        fw = np.array(c) * wReal
        print "fw: ", fw
        sumfw = float(sum(fw))
        print "sumfw: ", sumfw
        pw = np.divide(fw, sumfw)
        print "pw: ", pw
        hw = -sum(pw*np.log(pw))
        print "hw: ", hw
        wpe = hw/np.log(math.factorial(m))
        print "wpe: ", wpe
        # print "coba: ", coba
        """p = np.divide(np.array(c), float(sum(c)))
        # print "p: ",p

        h = -sum(p * np.log(p))
        pe = h/np.log(math.factorial(m))
        return pe"""
        return wpe

    def setPermutationEntropy(self, d1,d2,d3,d4,a4):
        self.d1 = np.array(d1)
        self.d2 = np.array(d2)
        self.d3 = np.array(d3)
        self.d4 = np.array(d4)
        self.a4 = np.array(a4)

        cD1 = self.weightedPermutationEntropy(self.d1,3,1)
        cD2 = self.weightedPermutationEntropy(self.d2, 3, 1)
        cD3 = self.weightedPermutationEntropy(self.d3, 3, 1)
        cD4 = self.weightedPermutationEntropy(self.d4, 3, 1)
        cA4 = self.weightedPermutationEntropy(self.a4, 3, 1)

        return cD1, cD2, cD3, cD4, cA4





