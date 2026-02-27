import pandas as pd
import numpy as np 

np.random.seed(42)

#Create a sample dataset
Industries=["Banking", "Telecoms", "Retail",
    "Mining", "Utilities", "Food Production",
    "Insurance", "Transport"]

dates=pd.date_range(start="2010-01-01", end="2024-06-30", freq="Q")
records=[]

Firm_Id=1
for industry in Industries:
    N_Firms=np.random.randint(8,15) #Random number of firms per industry
    
    for i in range(N_Firms):
        
        #Uneven market shares
        shares=np.random.dirichlet(np.ones(N_Firms)*0.7)
        
        for date in dates:
            Revenue=np.random.lognormal(mean=16, sigma=0.4)*shares[i] #Revenue influenced by market share
            Cogs=Revenue*(np.random.uniform(0.45,0.75)) #COGS is a percentage of revenue
            Operating=Revenue*(np.random.uniform(0.10,0.25)) #Operating expenses is a percentage of revenue
            
            records.append(
                {
                    "Date": date,
                    "Firm_Id": Firm_Id,
                    "Industry": industry,
                    "Revenue": Revenue,
                    "Cost_Of_Goods_Sold": Cogs,
                    "Operating_Expenses": Operating,
                    "Market_Share": shares[i]
                }
            )
        Firm_Id+=1
        
df=pd.DataFrame(records)
df.to_csv("data/raw/firm_financials.csv", index=False)