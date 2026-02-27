def Mark_Up(df):
    #Calculate the markup for each firm
    df["Markup"]=df["Revenue"]/df["Cost_Of_Goods_Sold"]
    df["Lerner_Index"]=(df["Revenue"]-df["Cost_Of_Goods_Sold"])/df["Revenue"]
    df["Profit_margin"]=(df["Revenue"]-df["Cost_Of_Goods_Sold"] -df["Operating_Expenses"])/df["Revenue"]
    return df                    