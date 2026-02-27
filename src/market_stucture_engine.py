import pandas as pd

def ComputeHHI(df):
    #Calculate the HHI for each industry
    HHI=(
        df.groupby(["date", "industry"])["market_share"]
        .apply(lambda x: (x**2).sum()*10000)
        .reset_index(name="HHI")
    )
    return HHI

def compute_CR4(df):
    #Calculate thhe concentration ratio for the top 4 firms in each industry
    CR4=(df.groupby(["date", "industry"])["market_share"]
         .apply(lambda x: x.nlargest(4).sum()*100)
    .reset_index(name="CR4")
    )
    return CR4