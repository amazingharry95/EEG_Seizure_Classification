import matplotlib.pyplot as plt
import os,sys
import csv
import classifierModel as cM
import matplotlib.pyplot as plt

folder = r'C:\Users\amazingharry95\Google Drive\Semester 7\Biomedik\FP\biomedik\dataset\data'
dataset = []os.listdir(folder):
    if iter==1:
iter = 0
for filename in
        namaFile = 'data/'+filename
        fid = open(namaFile,'r')
        tmp = fid.readlines()
        #print "tmp: ", tmp
        data = [float(k) for k in tmp]

        myClassifier = cM.classifierModel(data)
        cA4, cD4, cD3, cD2, cD1 = myClassifier.discreteWavelete()
        plt.plot(cA4)
        plt.title('Delta (0-4 Hz)')
        plt.show()

        plt.plot(cD4)
        plt.title('Theta (4-8 Hz)')
        plt.show()

        plt.plot(cD3)
        plt.title('Alpha (8-13 Hz)')
        plt.show()

        plt.plot(cD2)
        plt.title('Beta (13-30 Hz)')
        plt.show()

        plt.plot(cD1)
        plt.title('Gamma (30-60 Hz)')
        plt.show()

        d1, d2, d3, d4, a4 = myClassifier.setPermutationEntropy(cD1, cD2, cD3, cD4, cA4)
        """d1B = np.array(cD1)
        d2B = np.array(cD2)
        d3B = np.array(cD3)
        d4B = np.array(cD4)
        a4B = np.array(cA4)

        d1 = permutation_entropy(d1B,3,1)
        d2 = permutation_entropy(d2B,3,1)
        d3 = permutation_entropy(d3B,3,1)
        d4 = permutation_entropy(d4B,3,1)
        a4 = permutation_entropy(a4B,3,1)"""

        eegData = []
        eegData.append(d1)
        eegData.append(d2)
        eegData.append(d3)
        eegData.append(d4)
        eegData.append(a4)

        if filename[0] == 'Z':
            eegData.append('non-seizure')
        elif filename[0] == 'O':
            eegData.append('non-seizure')
        else:
            eegData.append('seizure')
        dataset.append(eegData)
    elif iter == 0:
        iter = iter+1
print dataset

"""
wtr = csv.writer(open ('WPE_Normalize.csv', 'w'), delimiter=',', lineterminator='\n')
for x in dataset : wtr.writerow ([x])"""