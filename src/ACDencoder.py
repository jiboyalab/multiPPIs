import csv
import numpy as np
def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:  
        SaveList.append(row)
    return
def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return
seq=[]
ReadMyCsv(seq,"proteinsequence.csv")
length=len(seq)
# 	H VSC P1 P2 SASA NCISC
# A 0.62 27.5 8.1 0.046 1.181 0.007187
# C 0.29 44.6 5.5 0.128 1.461 -0.03661
# D 0.9 40 13 0.105 1.587 0.02382
# E 0.74 62 12.3 0.151 1.862 0.006802
# F 1.19 115.5 5.2 0.29 2.228 0.037552
# G 0.48 0 9 0 0.881 0.179052
# H 0.4 79 10.4 0.23 2.025 0.01069
# I 1.38 93.5 5.2 0.186 1.81 0.021631
# K 1.5 100 11.3 0.219 2.258 0.017708
# L 1.06 93.5 4.9 0.186 1.931 0.051672
# M 0.64 94.1 5.7 0.221 2.034 0.002683
# N 0.78 58.7 11.6 0.134 1.655 0.005392
# P 0.12 41.9 8 0.131 1.468 0.239531
# Q 0.85 80.7 10.5 0.18 1.932 0.049211
# R 2.53 105 10.5 0.291 2.56 0.043587
# S 0.18 29.3 9.2 0.062 1.298 0.004627
# T 0.05 51.3 8.6 0.108 1.525 0.003352
# V 1.08 71.5 5.9 0.14 1.645 0.057004
# W 0.81 145.5 5.4 0.409 2.663 0.037977
# Y 0.26 117.3 6.2 0.298 2.368 0.023599
A= np.array([0.62, 27.5, 8.1, 0.046, 1.181 ,0.007187],dtype=float)
C= np.array([0.29 ,44.6 ,5.5, 0.128, 1.461, -0.03661],dtype=float)
D= np.array([-0.9 ,40 ,13 ,0.105 ,1.587, -0.02382],dtype=float)
E= np.array([-0.74 ,62 ,12.3, 0.151, 1.862, 0.006802],dtype=float)
F= np.array([1.19 ,115.5, 5.2 ,0.29 ,2.228 ,0.037552],dtype=float)
G= np.array([0.48, 0 ,9 ,0 ,0.881 ,0.179052],dtype=float)
H= np.array([-0.4 ,79 ,10.4 ,0.23, 2.025 ,-0.01069],dtype=float)
I= np.array([1.38 ,93.5 ,5.2 ,0.186, 1.81 ,0.021631],dtype=float)
K= np.array([-1.5 ,100, 11.3 ,0.219, 2.258 ,0.017708],dtype=float)
L= np.array([1.06, 93.5, 4.9 ,0.186, 1.931, 0.051672],dtype=float)
M= np.array([0.64,94.1 ,5.7 ,0.221 ,2.034, 0.002683],dtype=float)
N= np.array([-0.78 ,58.7 ,11.6, 0.134, 1.655 ,0.005392],dtype=float)
P= np.array([0.12 ,41.9 ,8, 0.131 ,1.468, 0.239531],dtype=float)
Q= np.array([-0.85 ,80.7, 10.5 ,0.18, 1.932 ,0.049211],dtype=float)
R= np.array([-2.53 ,105, 10.5 ,0.291 ,2.56, 0.043587],dtype=float)
S= np.array([-0.18 ,29.3 ,9.2 ,0.062 ,1.298 ,0.004627],dtype=float)
T= np.array([-0.05, 51.3 ,8.6 ,0.108 ,1.525 ,0.003352],dtype=float)
V= np.array([1.08 ,71.5 ,5.9, 0.14 ,1.645, 0.057004],dtype=float)
W= np.array([0.81, 145.5 ,5.4 ,0.409 ,2.663, 0.037977],dtype=float)
Y= np.array([0.26 ,117.3, 6.2 ,0.298, 2.368 ,0.023599],dtype=float)
#对原始数据做归一化处理

a0=(A[0]+C[0]+D[0]+E[0]+F[0]+G[0]+H[0]+I[0]+K[0]+L[0]+M[0]+N[0]+P[0]+Q[0]+R[0]+S[0]+T[0]+V[0]+W[0]+Y[0])/20
a1=(A[1]+C[1]+D[1]+E[1]+F[1]+G[1]+H[1]+I[1]+K[1]+L[1]+M[1]+N[1]+P[1]+Q[1]+R[1]+S[1]+T[1]+V[1]+W[1]+Y[1])/20
a2=(A[2]+C[2]+D[2]+E[2]+F[2]+G[2]+H[2]+I[2]+K[2]+L[2]+M[2]+N[2]+P[2]+Q[2]+R[2]+S[2]+T[2]+V[2]+W[2]+Y[2])/20
a3=(A[3]+C[3]+D[3]+E[3]+F[3]+G[3]+H[3]+I[3]+K[3]+L[3]+M[3]+N[3]+P[3]+Q[3]+R[3]+S[3]+T[3]+V[3]+W[3]+Y[3])/20
a4=(A[4]+C[4]+D[4]+E[4]+F[4]+G[4]+H[4]+I[4]+K[4]+L[4]+M[4]+N[4]+P[4]+Q[4]+R[4]+S[4]+T[4]+V[4]+W[4]+Y[4])/20
a5=(A[5]+C[5]+D[5]+E[5]+F[5]+G[5]+H[5]+I[5]+K[5]+L[5]+M[5]+N[5]+P[5]+Q[5]+R[5]+S[5]+T[5]+V[5]+W[5]+Y[5])/20
pj_bar=np.array([a0,a1,a2,a3,a4,a5],dtype=float)
b0=((A[0]-pj_bar[0])**2)+((C[0]-pj_bar[0])**2)+((D[0]-pj_bar[0])**2)+((E[0]-pj_bar[0])**2)\
+((F[0]-pj_bar[0])**2)+((G[0]-pj_bar[0])**2)+((H[0]-pj_bar[0])**2)+((I[0]-pj_bar[0])**2)\
+((K[0]-pj_bar[0])**2)+((L[0]-pj_bar[0])**2)+((M[0]-pj_bar[0])**2)+((N[0]-pj_bar[0])**2)\
+((P[0]-pj_bar[0])**2)+((Q[0]-pj_bar[0])**2)+((R[0]-pj_bar[0])**2)+((S[0]-pj_bar[0])**2)\
+((T[0]-pj_bar[0])**2)+((V[0]-pj_bar[0])**2)+((W[0]-pj_bar[0])**2)+((Y[0]-pj_bar[0])**2)
b1=((A[1]-pj_bar[1])**2)+((C[1]-pj_bar[1])**2)+((D[1]-pj_bar[1])**2)+((E[1]-pj_bar[1])**2)\
+((F[1]-pj_bar[1])**2)+((G[1]-pj_bar[1])**2)+((H[1]-pj_bar[1])**2)+((I[1]-pj_bar[1])**2)\
+((K[1]-pj_bar[1])**2)+((L[1]-pj_bar[1])**2)+((M[1]-pj_bar[1])**2)+((N[1]-pj_bar[1])**2)\
+((P[1]-pj_bar[1])**2)+((Q[1]-pj_bar[1])**2)+((R[1]-pj_bar[1])**2)+((S[1]-pj_bar[1])**2)\
+((T[1]-pj_bar[1])**2)+((V[1]-pj_bar[1])**2)+((W[1]-pj_bar[1])**2)+((Y[1]-pj_bar[1])**2)
b2=((A[2]-pj_bar[2])**2)+((C[2]-pj_bar[2])**2)+((D[2]-pj_bar[2])**2)+((E[2]-pj_bar[2])**2)\
+((F[2]-pj_bar[2])**2)+((G[2]-pj_bar[2])**2)+((H[2]-pj_bar[2])**2)+((I[2]-pj_bar[2])**2)\
+((K[2]-pj_bar[2])**2)+((L[2]-pj_bar[2])**2)+((M[2]-pj_bar[2])**2)+((N[2]-pj_bar[2])**2)\
+((P[2]-pj_bar[2])**2)+((Q[2]-pj_bar[2])**2)+((R[2]-pj_bar[2])**2)+((S[2]-pj_bar[2])**2)\
+((T[2]-pj_bar[2])**2)+((V[2]-pj_bar[2])**2)+((W[2]-pj_bar[2])**2)+((Y[2]-pj_bar[2])**2)
b3=((A[3]-pj_bar[3])**2)+((C[3]-pj_bar[3])**2)+((D[3]-pj_bar[3])**2)+((E[3]-pj_bar[3])**2)\
+((F[3]-pj_bar[3])**2)+((G[3]-pj_bar[3])**2)+((H[3]-pj_bar[3])**2)+((I[3]-pj_bar[3])**2)\
+((K[3]-pj_bar[3])**2)+((L[3]-pj_bar[3])**2)+((M[3]-pj_bar[3])**2)+((N[3]-pj_bar[3])**2)\
+((P[3]-pj_bar[3])**2)+((Q[3]-pj_bar[3])**2)+((R[3]-pj_bar[3])**2)+((S[3]-pj_bar[3])**2)\
+((T[3]-pj_bar[3])**2)+((V[3]-pj_bar[3])**2)+((W[3]-pj_bar[3])**2)+((Y[3]-pj_bar[3])**2)
b4=((A[4]-pj_bar[4])**2)+((C[4]-pj_bar[4])**2)+((D[4]-pj_bar[4])**2)+((E[4]-pj_bar[4])**2)\
+((F[4]-pj_bar[4])**2)+((G[4]-pj_bar[4])**2)+((H[4]-pj_bar[4])**2)+((I[4]-pj_bar[4])**2)\
+((K[4]-pj_bar[4])**2)+((L[4]-pj_bar[4])**2)+((M[4]-pj_bar[4])**2)+((N[4]-pj_bar[4])**2)\
+((P[4]-pj_bar[4])**2)+((Q[4]-pj_bar[4])**2)+((R[4]-pj_bar[4])**2)+((S[4]-pj_bar[4])**2)\
+((T[4]-pj_bar[4])**2)+((V[4]-pj_bar[4])**2)+((W[4]-pj_bar[4])**2)+((Y[4]-pj_bar[4])**2)
b5=((A[5]-pj_bar[5])**2)+((C[5]-pj_bar[5])**2)+((D[5]-pj_bar[5])**2)+((E[5]-pj_bar[5])**2)\
+((F[5]-pj_bar[5])**2)+((G[5]-pj_bar[5])**2)+((H[5]-pj_bar[5])**2)+((I[5]-pj_bar[5])**2)\
+((K[5]-pj_bar[5])**2)+((L[5]-pj_bar[5])**2)+((M[5]-pj_bar[5])**2)+((N[5]-pj_bar[5])**2)\
+((P[5]-pj_bar[5])**2)+((Q[5]-pj_bar[5])**2)+((R[5]-pj_bar[5])**2)+((S[5]-pj_bar[5])**2)\
+((T[5]-pj_bar[5])**2)+((V[5]-pj_bar[5])**2)+((W[5]-pj_bar[5])**2)+((Y[5]-pj_bar[5])**2)
sj=np.array([(b0/20)**0.5,(b1/20)**0.5,(b2/20)**0.5,(b3/20)**0.5,(b4/20)**0.5,(b5/20)**0.5],dtype=float)
A[0]=(A[0]-pj_bar[0])/sj[0];A[1]=(A[1]-pj_bar[1])/sj[1];A[2]=(A[2]-pj_bar[2])/sj[2];A[3]=(A[3]-pj_bar[3])/sj[3];A[4]=(A[4]-pj_bar[4])/sj[4];A[5]=(A[5]-pj_bar[5])/sj[5]
C[0]=(C[0]-pj_bar[0])/sj[0];C[1]=(C[1]-pj_bar[1])/sj[1];C[2]=(C[2]-pj_bar[2])/sj[2];C[3]=(C[3]-pj_bar[3])/sj[3];C[4]=(C[4]-pj_bar[4])/sj[4];C[5]=(C[5]-pj_bar[5])/sj[5]
D[0]=(D[0]-pj_bar[0])/sj[0];D[1]=(D[1]-pj_bar[1])/sj[1];D[2]=(D[2]-pj_bar[2])/sj[2];D[3]=(D[3]-pj_bar[3])/sj[3];D[4]=(D[4]-pj_bar[4])/sj[4];D[5]=(D[5]-pj_bar[5])/sj[5]
E[0]=(E[0]-pj_bar[0])/sj[0];E[1]=(E[1]-pj_bar[1])/sj[1];E[2]=(E[2]-pj_bar[2])/sj[2];E[3]=(E[3]-pj_bar[3])/sj[3];E[4]=(E[4]-pj_bar[4])/sj[4];E[5]=(E[5]-pj_bar[5])/sj[5]
F[0]=(F[0]-pj_bar[0])/sj[0];F[1]=(F[1]-pj_bar[1])/sj[1];F[2]=(F[2]-pj_bar[2])/sj[2];F[3]=(F[3]-pj_bar[3])/sj[3];F[4]=(F[4]-pj_bar[4])/sj[4];F[5]=(F[5]-pj_bar[5])/sj[5]
G[0]=(G[0]-pj_bar[0])/sj[0];G[1]=(G[1]-pj_bar[1])/sj[1];G[2]=(G[2]-pj_bar[2])/sj[2];G[3]=(G[3]-pj_bar[3])/sj[3];G[4]=(G[4]-pj_bar[4])/sj[4];G[5]=(G[5]-pj_bar[5])/sj[5]
H[0]=(H[0]-pj_bar[0])/sj[0];H[1]=(H[1]-pj_bar[1])/sj[1];H[2]=(H[2]-pj_bar[2])/sj[2];H[3]=(H[3]-pj_bar[3])/sj[3];H[4]=(H[4]-pj_bar[4])/sj[4];H[5]=(H[5]-pj_bar[5])/sj[5]
I[0]=(I[0]-pj_bar[0])/sj[0];I[1]=(I[1]-pj_bar[1])/sj[1];I[2]=(I[2]-pj_bar[2])/sj[2];I[3]=(I[3]-pj_bar[3])/sj[3];I[4]=(I[4]-pj_bar[4])/sj[4];I[5]=(I[5]-pj_bar[5])/sj[5]
K[0]=(K[0]-pj_bar[0])/sj[0];K[1]=(K[1]-pj_bar[1])/sj[1];K[2]=(K[2]-pj_bar[2])/sj[2];K[3]=(K[3]-pj_bar[3])/sj[3];K[4]=(K[4]-pj_bar[4])/sj[4];K[5]=(K[5]-pj_bar[5])/sj[5]
L[0]=(L[0]-pj_bar[0])/sj[0];L[1]=(L[1]-pj_bar[1])/sj[1];L[2]=(L[2]-pj_bar[2])/sj[2];L[3]=(L[3]-pj_bar[3])/sj[3];L[4]=(L[4]-pj_bar[4])/sj[4];L[5]=(L[5]-pj_bar[5])/sj[5]
M[0]=(M[0]-pj_bar[0])/sj[0];M[1]=(M[1]-pj_bar[1])/sj[1];M[2]=(M[2]-pj_bar[2])/sj[2];M[3]=(M[3]-pj_bar[3])/sj[3];M[4]=(M[4]-pj_bar[4])/sj[4];M[5]=(M[5]-pj_bar[5])/sj[5]
N[0]=(N[0]-pj_bar[0])/sj[0];N[1]=(N[1]-pj_bar[1])/sj[1];N[2]=(N[2]-pj_bar[2])/sj[2];N[3]=(N[3]-pj_bar[3])/sj[3];N[4]=(N[4]-pj_bar[4])/sj[4];N[5]=(N[5]-pj_bar[5])/sj[5]
P[0]=(P[0]-pj_bar[0])/sj[0];P[1]=(P[1]-pj_bar[1])/sj[1];P[2]=(P[2]-pj_bar[2])/sj[2];P[3]=(P[3]-pj_bar[3])/sj[3];P[4]=(P[4]-pj_bar[4])/sj[4];P[5]=(P[5]-pj_bar[5])/sj[5]
Q[0]=(Q[0]-pj_bar[0])/sj[0];Q[1]=(Q[1]-pj_bar[1])/sj[1];Q[2]=(Q[2]-pj_bar[2])/sj[2];Q[3]=(Q[3]-pj_bar[3])/sj[3];Q[4]=(Q[4]-pj_bar[4])/sj[4];Q[5]=(Q[5]-pj_bar[5])/sj[5]
R[0]=(R[0]-pj_bar[0])/sj[0];R[1]=(R[1]-pj_bar[1])/sj[1];R[2]=(R[2]-pj_bar[2])/sj[2];R[3]=(R[3]-pj_bar[3])/sj[3];R[4]=(R[4]-pj_bar[4])/sj[4];R[5]=(R[5]-pj_bar[5])/sj[5]
S[0]=(S[0]-pj_bar[0])/sj[0];S[1]=(S[1]-pj_bar[1])/sj[1];S[2]=(S[2]-pj_bar[2])/sj[2];S[3]=(S[3]-pj_bar[3])/sj[3];S[4]=(S[4]-pj_bar[4])/sj[4];S[5]=(S[5]-pj_bar[5])/sj[5]
T[0]=(T[0]-pj_bar[0])/sj[0];T[1]=(T[1]-pj_bar[1])/sj[1];T[2]=(T[2]-pj_bar[2])/sj[2];T[3]=(T[3]-pj_bar[3])/sj[3];T[4]=(T[4]-pj_bar[4])/sj[4];T[5]=(T[5]-pj_bar[5])/sj[5]
V[0]=(V[0]-pj_bar[0])/sj[0];V[1]=(V[1]-pj_bar[1])/sj[1];V[2]=(V[2]-pj_bar[2])/sj[2];V[3]=(V[3]-pj_bar[3])/sj[3];V[4]=(V[4]-pj_bar[4])/sj[4];V[5]=(V[5]-pj_bar[5])/sj[5]
W[0]=(W[0]-pj_bar[0])/sj[0];W[1]=(W[1]-pj_bar[1])/sj[1];W[2]=(W[2]-pj_bar[2])/sj[2];W[3]=(W[3]-pj_bar[3])/sj[3];W[4]=(W[4]-pj_bar[4])/sj[4];W[5]=(W[5]-pj_bar[5])/sj[5]
Y[0]=(Y[0]-pj_bar[0])/sj[0];Y[1]=(Y[1]-pj_bar[1])/sj[1];Y[2]=(Y[2]-pj_bar[2])/sj[2];Y[3]=(Y[3]-pj_bar[3])/sj[3];Y[4]=(Y[4]-pj_bar[4])/sj[4];Y[5]=(Y[5]-pj_bar[5])/sj[5]
#自协方差编码
def Xij(data, number):
    if data=='A':return A[number]
    if data == 'C': return C[number]
    if data == 'D': return D[number]
    if data == 'E': return E[number]
    if data == 'F': return F[number]
    if data == 'G': return G[number]
    if data == 'H': return H[number]
    if data == 'I': return I[number]
    if data == 'K': return K[number]
    if data == 'L': return L[number]
    if data == 'M': return M[number]
    if data == 'N': return N[number]
    if data == 'P': return P[number]
    if data == 'Q': return Q[number]
    if data == 'R': return R[number]
    if data == 'S': return S[number]
    if data == 'T': return T[number]
    if data == 'V': return V[number]
    if data == 'W': return W[number]
    if data == 'Y': return Y[number]
    else: return 0
FinalACC2=[]

for seqnum in range(length):
    print(seqnum)
    FinalACC=[]
    FinalACC.append(seq[seqnum][0])
    n=len(seq[seqnum][1])
    for log in range(1,31):
        for j in range(6):
            sum=float(0)
            sum2=float(0)
            c0=1/(n-log)
            for i1 in range(1, n + 1):
                sum += Xij(seq[seqnum][1][i1 - 1], j)
            d = (1 / n) * sum
            for i0 in range(1,n-log+1):
                X=Xij(seq[seqnum][1][i0-1],j)
                sum2+=(X-d)*(Xij(seq[seqnum][1][i0+log-1],j)-d)
            ACC=str(c0*sum2)
            FinalACC.append(ACC)
    FinalACC2.append(FinalACC)
    

StorFile(FinalACC2,'FinalProteinACD.csv')

        

    
