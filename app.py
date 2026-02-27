import streamlit as st
import pandas as pd
from src.market_stucture_engine import ComputeHHI,compute_CR4
from src.Markup_calculator import Mark_Up
from src.risk_Classifier import Classification_Competition_Risk


st.set_page_config(page_title="Pricing Power Market Analyser", layout="wide")
st.title("Pricing Power Market Analyser")

@st.cache_data
def load_data():
    return pd.read_csv("data/raw/firm_financials.csv", parse_dates=["Date"])
df=load_data()

df=Mark_Up(df)
hhi=ComputeHHI(df)
cr4=compute_CR4(df)
df["Risk_Category"]=df["HHI"].apply(Classification_Competition_Risk)

tab1, tab2, tab3=st.tabs(["Market Structure Analysis", "Markup Analysis", "Risk Classification"])

with tab1:
    st.header("Average markups by industry")
    Avg_Markup=df.groupby("Industry")["Markup"].mean().reset_index()
    st.bar_chart(Avg_Markup.set_index("Industry")["Markup"])
    
with tab2:
    st.header("HHI trends")
    industry=st.selectbox("Select Industry", df["Industry"].unique())
    HHI_Filtered=df[df["Industry"]==industry]
    st.line_chart(HHI_Filtered.set_index("Date")["HHI"])
    
with tab3:
    Latest_HHI=hhi.sort_values("date", ascending=False).groupby("Industry").tail(1)
    Latest_HHI["Risk_Category"]=Latest_HHI["HHI"].apply(Classification_Competition_Risk)
    st.dataframe(Latest_HHI[["industry", "HHI", "Risk_Category"]])