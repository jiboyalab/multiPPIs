import os
import time
import numpy as np
import pandas as pd
import csv
import math
import random
import csv
import math
import random
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from scipy import interp
from itertools import cycle
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:  
        SaveList.append(row)
    return

def ReadMyCsv2(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:
        counter = 0
        while counter < len(row):
            row[counter] = int(row[counter])     
            counter = counter + 1
        SaveList.append(row)
    return

def ReadMyCsv3(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:
        counter = 0
        while counter < len(row):
            row[counter] = float(row[counter])    
            counter = counter + 1
        SaveList.append(row)
    return

def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return

def GenerateLabel(Sample):
    Label = []
    counter = 0
    while counter < len(Sample) / 2:
        Label.append(1)
        counter = counter + 1
    counter = 0
    while counter < len(Sample) / 2:
        Label.append(0)
        counter = counter + 1
    return Label

def MyConfuse(SampleFeature, SampleLabel):
   
    counter = 0
    R = []
    while counter < len(SampleFeature):
        R.append(counter)
        counter = counter + 1
    random.shuffle(R)

    RSampleFeature = []
    RSampleLabel = []
    counter = 0
    while counter < len(SampleFeature):
        RSampleFeature.append(SampleFeature[R[counter]])
        RSampleLabel.append(SampleLabel[R[counter]])
        counter = counter + 1
    print('len(RSampleFeature)', len(RSampleFeature))
    print('len(RSampleLabel)', len(RSampleLabel))
    return RSampleFeature, RSampleLabel

def MyEnlarge(x0, y0, width, height, x1, y1, times, mean_fpr, mean_tpr, thickness=1, color = 'blue'):
    def MyFrame(x0, y0, width, height):
        import matplotlib.pyplot as plt
        import numpy as np

        x1 = np.linspace(x0, x0, num=20) 
        y1 = np.linspace(y0, y0, num=20)
        xk = np.linspace(x0, x0 + width, num=20)
        yk = np.linspace(y0, y0 + height, num=20)

        xkn = []
        ykn = []
        counter = 0
        while counter < 20:
            xkn.append(x1[counter] + width)
            ykn.append(y1[counter] + height)
            counter = counter + 1

        plt.plot(x1, yk, color='k', linestyle=':', lw=1, alpha=1)  # 左
        plt.plot(xk, y1, color='k', linestyle=':', lw=1, alpha=1)  # 下
        plt.plot(xkn, yk, color='k', linestyle=':', lw=1, alpha=1)  # 右
        plt.plot(xk, ykn, color='k', linestyle=':', lw=1, alpha=1)  # 上

        return

    width2 = times * width
    height2 = times * height
    MyFrame(x0, y0, width, height)
    MyFrame(x1, y1, width2, height2)


    xp = np.linspace(x0 + width, x1, num=20)
    yp = np.linspace(y0, y1 + height2, num=20)
    plt.plot(xp, yp, color='k', linestyle=':', lw=1, alpha=1)


    XDottedLine = []
    YDottedLine = []
    counter = 0
    while counter < len(mean_fpr):
        if mean_fpr[counter] > x0 and mean_fpr[counter] < (x0 + width) and mean_tpr[counter] > y0 and mean_tpr[counter] < (y0 + height):
            XDottedLine.append(mean_fpr[counter])
            YDottedLine.append(mean_tpr[counter])
        counter = counter + 1


    counter = 0
    while counter < len(XDottedLine):
        XDottedLine[counter] = (XDottedLine[counter] - x0) * times + x1
        YDottedLine[counter] = (YDottedLine[counter] - y0) * times + y1
        counter = counter + 1


    plt.plot(XDottedLine, YDottedLine, color=color, lw=thickness, alpha=1)
    return

def MyConfusionMatrix(y_real,y_predict):
    from sklearn.metrics import confusion_matrix
    CM = confusion_matrix(y_real, y_predict)
    print(CM)
    CM = CM.tolist()
    TN = CM[0][0]
    FP = CM[0][1]
    FN = CM[1][0]
    TP = CM[1][1]
    print('TN:%d, FP:%d, FN:%d, TP:%d' % (TN, FP, FN, TP))
    Acc = (TN + TP) / (TN + TP + FN + FP)
    Sen = TP / (TP + FN)
    Spec = TN / (TN + FP)
    Prec = TP / (TP + FP)
    MCC = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
    # 分母可能出现0，需要讨论待续
    print('Acc:', round(Acc, 4))
    print('Sen:', round(Sen, 4))
    print('Spec:', round(Spec, 4))
    print('Prec:', round(Prec, 4))
    print('MCC:', round(MCC, 4))
    Result = []
    Result.append(round(Acc, 4))
    Result.append(round(Sen, 4))
    Result.append(round(Spec, 4))
    Result.append(round(Prec, 4))
    Result.append(round(MCC, 4))
    return Result

def MyAverage(matrix):
    SumAcc = 0
    SumSen = 0
    SumSpec = 0
    SumPrec = 0
    SumMcc = 0
    counter = 0
    while counter < len(matrix):
        SumAcc = SumAcc + matrix[counter][0]
        SumSen = SumSen + matrix[counter][1]
        SumSpec = SumSpec + matrix[counter][2]
        SumPrec = SumPrec + matrix[counter][3]
        SumMcc = SumMcc + matrix[counter][4]
        counter = counter + 1
    print('AverageAcc:',SumAcc / len(matrix))
    print('AverageSen:', SumSen / len(matrix))
    print('AverageSpec:', SumSpec / len(matrix))
    print('AveragePrec:', SumPrec / len(matrix))
    print('AverageMcc:', SumMcc / len(matrix))
    return

def MyRealAndPredictionProb(Real,prediction):
    RealAndPredictionProb = []
    counter = 0
    while counter < len(prediction):
        pair = []
        pair.append(Real[counter])
        pair.append(prediction[counter][1])
        RealAndPredictionProb.append(pair)
        counter = counter + 1
    return RealAndPredictionProb

def MyRealAndPrediction(Real,prediction):
    RealAndPrediction = []
    counter = 0
    while counter < len(prediction):
        pair = []
        pair.append(Real[counter])
        pair.append(prediction[counter])
        RealAndPrediction.append(pair)
        counter = counter + 1
    return RealAndPrediction

def MyStd(result):
    import numpy as np
    NewMatrix = []
    counter = 0
    while counter < len(result[0]):
        row = []
        NewMatrix.append(row)
        counter = counter + 1
    counter = 0
    while counter < len(result):
        counter1 = 0
        while counter1 < len(result[counter]):
            NewMatrix[counter1].append(result[counter][counter1])
            counter1 = counter1 + 1
        counter = counter + 1
    StdList = []
    MeanList = []
    counter = 0
    while counter < len(NewMatrix):
        # std
        arr_std = np.std(NewMatrix[counter], ddof=1)
        StdList.append(arr_std)
        # mean
        arr_mean = np.mean(NewMatrix[counter])
        MeanList.append(arr_mean)
        counter = counter + 1
    result.append(MeanList)
    result.append(StdList)
    # 换算成百分比制
    counter = 0
    while counter < len(result):
        counter1 = 0
        while counter1 < len(result[counter]):
            result[counter][counter1] = round(result[counter][counter1] * 100, 2)
            counter1 = counter1 + 1
        counter = counter + 1
    return result

PositiveSample = []     
ReadMyCsv2(PositiveSample, 'PositiveSample.csv')
print('PositiveSample[0]', PositiveSample[0])

NegativeSample = []     
ReadMyCsv2(NegativeSample, 'NegativeSample.csv')
print('NegativeSample[0]', NegativeSample[0])

NewRandomList = []      
ReadMyCsv2(NewRandomList, 'NewRandomList.csv')
# print('NewRandomList[0]', NewRandomList[0])


tprs = []
aucs = []
mean_fpr = np.linspace(0, 1, 1000)
i = 0
colorlist = ['red', 'gold', 'purple', 'green', 'blue', 'black']
RealAndPrediction = []
AllResult = []

counter = 0
while counter < 5:
    AllNodeFeatureNum = []
    AllNodeFeatureNumName = 'AllNodeAttributeMannerNum' + str(counter) + '.csv'
    # print('AllNodeFeatureNumName', AllNodeFeatureNumName)
    ReadMyCsv3(AllNodeFeatureNum, AllNodeFeatureNumName)


    PositiveSampleFeature = []
    counter1 = 0
    while counter1 < len(PositiveSample):
        FeaturePair = []
        FeaturePair.extend(AllNodeFeatureNum[PositiveSample[counter1][0]])
        FeaturePair.extend(AllNodeFeatureNum[PositiveSample[counter1][1]])
        PositiveSampleFeature.append(FeaturePair)
        counter1 = counter1 + 1
    # print('np.array(PositiveSampleFeature).shape', np.array(PositiveSampleFeature).shape)
    # print('PositiveSampleFeature[0]', PositiveSampleFeature[0])
    # StorFile(PositiveSampleFeature, 'PositiveSampleFeature.csv')
    NegativeSampleFeature = []
    counter1 = 0
    while counter1 < len(NegativeSample):
        FeaturePair = []
        FeaturePair.extend(AllNodeFeatureNum[NegativeSample[counter1][0]])
        FeaturePair.extend(AllNodeFeatureNum[NegativeSample[counter1][1]])
        NegativeSampleFeature.append(FeaturePair)
        counter1 = counter1 + 1
    # print('np.array(NegativeSampleFeature).shape', np.array(NegativeSampleFeature).shape)

    Num = 0
    NewPositiveSampleFeature = []
    NewNegativeSampleFeature = []
    counter2 = 0
    while counter2 < len(NewRandomList):
        PairP = []
        PairN = []  #
        PairP.extend(PositiveSampleFeature[Num:Num + len(NewRandomList[counter2])])
        PairN.extend(NegativeSampleFeature[Num:Num + len(NewRandomList[counter2])])
        NewPositiveSampleFeature.append(PairP)
        NewNegativeSampleFeature.append(PairN)
        Num = Num + len(NewRandomList[counter2])
        counter2 = counter2 + 1
    # print('!!!NewPositiveSampleFeature[0][0]', NewPositiveSampleFeature[0][0])
    # print('!!!NewPositiveSampleFeature[1][0]', NewPositiveSampleFeature[1][0])
    # print('len(NewPositiveSampleFeature)', len(NewPositiveSampleFeature))
    # print('len(NewPositiveSampleFeature[0])', len(NewPositiveSampleFeature[0]))
    # print('len(NewPositiveSampleFeature[0][0])', len(NewPositiveSampleFeature[0][0]))
    #
    # print('np.array(NegativeSampleFeature).shape', np.array(NegativeSampleFeature).shape)

    TrainPositiveFeature = []
    TrainNegativeFeature = []
    TestPositiveFeature = []
    TestNegativeFeature = []

    NumTest = 0
    NumTrain = 0
    counter4 = 0
    while counter4 < len(NewRandomList):         
        if counter4 == counter:
            TestPositiveFeature.extend(NewPositiveSampleFeature[counter4])
            TestNegativeFeature.extend(NewNegativeSampleFeature[counter4])
            NumTest = NumTest + 1
        if counter4 != counter:
            TrainPositiveFeature.extend(NewPositiveSampleFeature[counter4])
            TrainNegativeFeature.extend(NewNegativeSampleFeature[counter4])
            NumTrain = NumTrain + 1
        counter4 = counter4 + 1
    # print('NumTest, NumTrain', NumTest, NumTrain)
    # print('TestPositiveFeature[0]', TestPositiveFeature[0])
    # print('TrainPositiveFeature[0]', TrainPositiveFeature[0])
    #
    # print('np.array(TestPositiveFeature).shape', np.array(TestPositiveFeature).shape)
    # print('np.array(TestNegativeFeature).shape', np.array(TestNegativeFeature).shape)
    # print('np.array(TrainPositiveFeature).shape', np.array(TrainPositiveFeature).shape)
    # print('np.array(TrainNegativeFeature).shape', np.array(TrainNegativeFeature).shape)

    TrainFeature = []
    TrainFeature = TrainPositiveFeature
    TrainFeature.extend(TrainNegativeFeature)
    TrainLabel = GenerateLabel(TrainFeature)
    TrainFeature, TrainLabel = MyConfuse(TrainFeature, TrainLabel)


    TestFeature = []
    TestFeature = TestPositiveFeature
    TestFeature.extend(TestNegativeFeature)
    TestLabel = GenerateLabel(TestFeature)
    TestFeature, TestLabel = MyConfuse(TestFeature, TestLabel)

    # print('np.array(TrainFeature).shape', np.array(TrainFeature).shape)
    # print('np.array(TestFeature).shape', np.array(TestFeature).shape)
    print('start train')

    from sklearn.ensemble import RandomForestClassifier
    model1 = RandomForestClassifier(n_estimators=300)
    model1.fit(TrainFeature, TrainLabel)
    y_score0 = model1.predict(TestFeature)
    y_score1 = model1.predict_proba(TestFeature)
    # 保存Real,PredictionProb.csv
    RealAndPrediction = MyRealAndPrediction(TestLabel, y_score0)
    Name = str(i) + '.csv'
    StorFile(RealAndPrediction, Name)

    RealAndPredictionProb = MyRealAndPredictionProb(TestLabel,y_score1)
    NameProb = str(i) + 'Prob.csv'
    StorFile(RealAndPredictionProb, NameProb)


    Result = MyConfusionMatrix(TestLabel, y_score0)  #
    AllResult.append(Result)
    AllResult[i].append(roc_auc)
    i += 1


    # break
    counter = counter + 1

