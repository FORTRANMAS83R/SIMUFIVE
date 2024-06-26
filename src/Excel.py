import main
import pandas as pd
import openpyxl



# Call the build function and retrieve the return value
A={'dureeSimu': '3 ans', 'freqInitFive': 80.0, 'freqInitBeach': 90.0, 'freqInitPadel': 78.0, 'evoFreq': 'lineaire, tauxAugmentation: 1', 'freqBar': 50, 'ticketMoyenBar': 3.0, 'margeBar': 70}  

data = main.buildSimu(A)
def dictToDataFrame(dic):
    #print(dic["Charges"])
    df = pd.DataFrame.from_dict({(level1, level2): value 
							for level1, inner_dict in dic.items() 
							for level2, value in inner_dict.items()}, orient='index')
    df.index=pd.MultiIndex.from_tuples(df.index)
    df =  dictToDataFrame(data)  
    df.to_excel('weekly_results.xlsx', index = True)
    return df


