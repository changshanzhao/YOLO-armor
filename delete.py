import os
path1 = r"D:\FileRecv\YOLOarmor-2022final-master\Data\2021-RMUC-0417-0916\2021-RMUC-0417-0916\images\train"
path2 = r"D:\FileRecv\YOLOarmor-2022final-master\Data\2021-RMUC-0417-0916\2021-RMUC-0417-0916\labels\train"
f1 = os.listdir(path1)
f2 = os.listdir(path2)
f1_ = []
f2_ = []
for i in range(0,7602):
    f1_.append(f1[i].split(".",1));
    f1_[i]=f1_[i][0];
for j in range(0,4211):
    f2_.append(f2[j].split(".",1));
    f2_[j]=f2_[j][0];
for i in range(0,7602):
    if f1_[i] not in f2_:
       os.remove(path1 + '/' + f1[i])


