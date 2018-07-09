import stopwords
import string
import pandas as pd
import ast
import csv
count = 0
print(stopwords.Stopwords)
array_final = []


def string_match(str1, str2):                                                           # String Matching Function
    try:
        str_1 = [k for k in (''.join(k for k in str1.lower() if k not in string.punctuation).split(' ')) if k not in stopwords.Stopwords]
        str_2 = [k for k in (''.join(k for k in str2.lower() if k not in string.punctuation).split(' ')) if k not in stopwords.Stopwords]
    except AttributeError:
        str_1 = str1
        str_2 = str2
    str_list1 = [x for x in str_1 if x != '']
    str_list2 = [x for x in str_2 if x != '']
    gin_12 = 0
    gin_21 = 0
    for i in str_list1:
        if i in str_list2:
            gin_12 += 1
    for j in str_list2:
        if j in str_list1:
            gin_21 += 1
    try:
        pct_12 = ((gin_12/len(str_list1))*100)
        pct_21 = ((gin_21/len(str_list2))*100)
    except ZeroDivisionError:
        pct_12 = 0.0
        pct_21 = 0.0
    return round(pct_12, 2), round(pct_21, 2)


def main(a, b, c, d, e, f):
    p, q = string_match(a, b)
    r, s = string_match(c, d)
    t, u = string_match(e, f)
    array = [p, q, r, s, t, u]
    return array


df1 = pd.read_csv("grotal_csvfile.txt", sep="\t")
df2 = pd.read_csv("file_name2", sep="\t")
print(df2)
for i in range(1, len(df1["name"])):
    for j in range(1, len(df2)):
        Phone1 = ast.literal_eval(df1["phones"][i])["phone"]
        Phone1_1 = Phone1.split()
        Address1 = str(ast.literal_eval(df1["address"][i])["address line1"]) + ',' + str(ast.literal_eval(df1["address"][i])["address line2"])
        for k in ast.literal_eval(df2["phone"][i]):
            Phone2 = k['phone']
            print(Phone2)
        Address2 = str(ast.literal_eval(df2["address"][j])["address line 1"]) + ',' + str(ast.literal_eval(df2["address"][j])["address line 2"])
        array_final.append(main((df1["name"][i]), (df2["name"][j]), Phone1_1, Phone2, Address1, Address2))


print(array_final)
with open('.csv', "w") as f:                                                  # Creating a file to store the result
    writer = csv.writer(f, delimiter=',')
    writer.writerow(('n12', 'n21', 'p12', 'p21', 'a12', 'a21'))
    for i in array_final:
        writer.writerow(i)

