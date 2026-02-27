import streamlit as st
import pandas as pd
from src.market_stucture_engine import ComputeHHI,compute_CR4
from src.Markup_calculator import Mark_Up
from src.risk_Classifier import classification_Competition_Risk