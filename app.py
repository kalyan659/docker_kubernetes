# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:55:12 2025

@author: kalya
"""

# app.py
import streamlit as st

st.title("My Simple Streamlit App")
st.write("Hello from Kubernetes!")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")