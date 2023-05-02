import os
path1 = r"D:\FileRecv\YOLOarmor-2022final-master\Data\2021-RMUC-0417-0916\2021-RMUC-0417-0916\images\train"
path2 = r"H:\2021-RMUC-0417-0916\images"
f1 = os.listdir(path1)
f2 = os.listdir(path2)
f1_ = []
f2_ = []
for i in range(0,4211):
    f1_.append(f1[i].split(".",1));
    f1_[i]=f1_[i][0];
for j in range(0,5595):
    f2_.append(f2[j].split(".",1));
    f2_[j]=f2_[j][0];
for i in range(0,5595):
    if f2_[i]  in f1_:
       os.remove(path2 + '/' + f2[i])