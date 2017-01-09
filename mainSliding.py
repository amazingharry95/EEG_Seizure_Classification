import matplotlib.pyplot as plt
import os,sys
import csv
import classifierModel as cM

folder = r'C:\Users\amazingharry95\Google Drive\Semester 7\Biomedik\FP\biomedik\dataset\data'
dataset = []
iter = 0
for filename in os.listdir(folder):
    if iter>0:
        namaFile = 'data/'+filename
        fid = open(namaFile,'r')
        tmp = fid.readlines()
        #print "tmp: ", tmp
        data = [float(k) for k in tmp]
        myClassifier = cM.classifierModel(data)

        flag1 = 64
        fitur = []
        for i in xrange(0,4097,64):
            slidingOperator = data[i:flag1]
            wpe = myClassifier.weightedPermutationEntropy(slidingOperator,4,1)
            fitur.append(wpe)
            flag1=flag1+64

        """cA4, cD4, cD3, cD2, cD1 = myClassifier.discreteWavelete()
        d1, d2, d3, d4, a4 = myClassifier.setPermutationEntropy(cD1, cD2, cD3, cD4, cA4)
        d1B = np.array(cD1)
        d2B = np.array(cD2)
        d3B = np.array(cD3)
        d4B = np.array(cD4)
        a4B = np.array(cA4)

        d1 = permutation_entropy(d1B,3,1)
        d2 = permutation_entropy(d2B,3,1)
        d3 = permutation_entropy(d3B,3,1)
        d4 = permutation_entropy(d4B,3,1)
        a4 = permutation_entropy(a4B,3,1)

        eegData = []
        eegData.append(d1)
        eegData.append(d2)
        eegData.append(d3)
        eegData.append(d4)
        eegData.append(a4)"""

        if filename[0] == 'Z':
            fitur.append('non-seizure')
        elif filename[0] == 'O':
            fitur.append('non-seizure')
        else:
            fitur.append('seizure')
        dataset.append(fitur)
    elif iter == 0:
        iter = iter+1
print dataset


wtr = csv.writer(open ('Sliding_WPE_4_Normalize.csv', 'w'), delimiter=',', lineterminator='\n')
for x in dataset : wtr.writerow ([x])