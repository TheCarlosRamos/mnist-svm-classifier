#!/usr/bin/env python

import numpy as np
from scipy.io import loadmat, savemat
from os.path import exists
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

def leitura_mnist(filename):
    fid = open(filename, 'r')
    finished = False
    empty_lines = 0
    M = []
    t = []
    
    fid.readline()
    
    while not(finished):
        line = fid.readline()
        
        if len(line) < 10:
            empty_lines += 1
        else:
            empty_lines = 0
            
        if empty_lines >= 10:
            finished = True
        else:
            line = line.strip().split(',')
            if len(line) < 2:
                continue
                
            img = line[:-1]
            try:
                img = [int(float(x)) for x in img]
                target = int(line[-1])
                M.append(img)
                t.append(target)
                
                if np.mod(len(t), 1000) == 0:
                    print(f"Processadas {len(t)} amostras")
            except ValueError as e:
                print(f"Ignorando linha com erro: {e}")
    
    fid.close()
    return np.array(M), np.array(t)

def mainsvm(M, t):
    print('Iniciando o treinamento do SVM.')
    s = svm.SVC(kernel='rbf')
    s.fit(M, t)
    print('Treinamento do SVM concluído.')
    return s

def plot_confusion_matrix(cm, classes):
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=classes, yticklabels=classes)
    plt.title('Matriz de Confusão')
    plt.ylabel('Rótulo Verdadeiro')
    plt.xlabel('Rótulo Predito')
    plt.show()

if __name__ == '__main__':
    if exists('mnist_784.mat'):
        D = loadmat('mnist_784.mat')
        M = D['M']
        t = D['t']
        t = t[0]
    else:
        M, t = leitura_mnist('mnist_784.csv')
        D = {}
        D['M'] = M
        D['t'] = t
        savemat('mnist_784.mat', D)
    
    Mtreino = M[:30000, :]
    ttreino = t[:30000]
    Mtest = M[5000:6000, :]
    ttest = t[5000:6000]
    
    s = mainsvm(Mtreino, ttreino)
    
    print("\nAvaliando o modelo em todo o conjunto de teste...")
    predictions = s.predict(Mtest)
    
    accuracy = np.mean(predictions == ttest)
    print(f"\nAcurácia: {accuracy:.4f} ({accuracy*100:.2f}%)")
    
    cm = confusion_matrix(ttest, predictions)
    print("\nMatriz de Confusão:")
    print(cm)
    
    plot_confusion_matrix(cm, classes=[str(i) for i in range(10)])
    
    n = np.random.permutation(len(Mtest))[0]
    img = np.reshape(Mtest[n], (28, 28))
    
    plt.imshow(img, cmap='gray')
    plt.title(f'Rótulo: {ttest[n]}; Predição: {predictions[n]}')
    plt.show()
