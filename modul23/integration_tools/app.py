import streamlit as st
import requests
import pandas as pd

st.title("Project Managment App")

st.header("Add Developer")
dev_name=st.text_input("Developer Name")
dev_experience=st.number_input("Years of Expreience", min_value=0, max_value=50 , value=0)


if st.button("Create Developer"):
    dev_data={"name": dev_name, "experience": dev_experience}
    response=requests.post("http://localhost:8000/developers/",json=dev_data)
    st.json(response.json())    

st.header("Add a Project")
proj_title=st.text_input("Project Title")
proj_desc=st.text_area("Project Description")
proj_languages=st.text_input("Languages Used (Comma-seperated)")
lead_dev_name=st.text_input("Lead Developer Name")
lead_dev_exp=st.number_input("Years of Expreience", min_value=0, max_value=50 , value=0)

if st.button("Add a Project"):
    lead_dev_data={'name': lead_dev_name , "experience":lead_dev_exp}
    proj_data={
        "title":proj_title,
        "description":proj_desc,
        "languages":proj_languages.split(","),
        "lead_developer ":lead_dev_data
    }
    response=requests.post("http://localhost:8000/projects/",json=dev_data)
    projects_data=(response.json())