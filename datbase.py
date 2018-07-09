from pymongo import MongoClient
import pandas as pd
Client = MongoClient()
coaching_info = Client.mydatabase
grotal_coaching = coaching_info.grotal_coaching
df1 = pd.DataFrame(list(grotal_coaching.find()))
df1.to_csv('grotal_csvfile.txt', sep='\t', encoding='utf-8')