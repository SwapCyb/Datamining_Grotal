import csv
import pandas as pd
df1 = pd.read_csv("indiacom.csv")                                       # Reading csv file
indiacom = df1.sample(30)
df2 = pd.read_csv("target_study.csv")
targetstudy = df2.sample(30)
df3 = pd.read_csv("justdial.csv")
justdial = df3.sample(30)
result = [0 for i in range(len(df1))]
random = zip(justdial['n12'].values.tolist(), justdial['n21'].values.tolist(), justdial['p12'].values.tolist(), justdial['p21'].values.tolist(), justdial['a12'].values.tolist(), justdial['a21'].values.tolist(), result)
# with open("training_set.txt", "a") as f:
#     writer = csv.writer(f, delimiter=',')
#     # writer.writerow(['n12', 'n21', 'p12', 'p21', 'a12', 'a21', 'result'])
#     for list in random:
#         writer.writerow(list)

with open("training_set.txt", "a+") as f:
    writer = csv.writer(f, delimiter=',')
    indiacom1 = 0
    targetstudy1 = 0
    justdial1 = 0
    for i in range(len(df1)):
        if df1['n12'][i] > 40.0 and df1['n21'][i] > 40.0:       # Checking the name for match
            n = df1.iloc[i].values.tolist()
            n.append(1)
            writer.writerow(n)
            indiacom1 += 1
    for i in range(len(df2)):
        if df2['n12'][i] > 40.0 and df2['n21'][i] > 40.0:
            n = df2.iloc[i].values.tolist()
            n.append(1)
            writer.writerow(n)
            targetstudy1 += 1
    for i in range(len(df3)):
        if df3['n12'][i] > 40.0 and df3['n21'][i] > 40.0:
            n = df3.iloc[i].values.tolist()
            n.append(1)
            writer.writerow(n)
            justdial1 += 1
    print(indiacom1, targetstudy1, justdial1)
    print("\n")

    indiacom2 = 0
    targetstudy2 = 0
    justdial2 = 0
    for i in range(len(df1)):
        if df1['p12'][i] > 0.0 and df1['p21'][i] > 0.0:                # Checking the Phone no. Match
            p = df1.iloc[i].values.tolist()
            p.append(1)
            writer.writerow(p)
            indiacom2 += 1
    for i in range(len(df2)):
        if df2['p12'][i] > 0.0 and df2['p21'][i] > 0.0:
            p = df2.iloc[i].values.tolist()
            p.append(1)
            writer.writerow(p)
            targetstudy2 += 1
    for i in range(len(df3)):
        if df3['p12'][i] > 0.0 and df3['p21'][i] > 0.0:
            p = df3.iloc[i].values.tolist()
            p.append(1)
            writer.writerow(p)
            justdial2 += 1
    print(indiacom2, targetstudy2, justdial2)
    print("\n")

    indiacom3 = 0
    targetstudy3 = 0
    justdial3 = 0
    for i in range(len(df1)):
        if df1['a12'][i] > 40.0 and df1['a21'][i] > 40.0:                   # Checking the Address match
            a = df1.iloc[i].values.tolist()
            a.append(1)
            print(a)
            writer.writerow(a)
            indiacom3 += 1
    for i in range(len(df2)):
        if df2['a12'][i] > 40.0 and df2['a21'][i] > 40.0:
            a = df2.iloc[i].values.tolist()
            a.append(1)
            writer.writerow(a)
            targetstudy3 += 1
    for i in range(len(df3)):
        if df3['a12'][i] > 40.0 and df3['a21'][i] > 40.0:
            a = df3.iloc[i].values.tolist()
            a.append(1)
            writer.writerow(a)
            justdial3 += 1
    print(indiacom3, targetstudy3, justdial3)



