import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))

parent_dir = os.path.dirname(current_dir)

sys.path.append(parent_dir)
import simu.main as main
import pandas as pd
import openpyxl



def dictToDataFrame(dic):

    df = pd.DataFrame.from_dict({(level1, level2): value 
							for level1, inner_dict in dic.items() 
							for level2, value in inner_dict.items()}, orient='index')
    df.index=pd.MultiIndex.from_tuples(df.index) 
    print(df)
    df.to_excel('tst.xlsx', index = True)
    return df

dictToDataFrame(a)




