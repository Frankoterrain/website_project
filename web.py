import streamlit as st
import pandas

st.title("The Best Company")

content = """This company belongs to Mr. Franklin Okoma Chukwuma, formal student of Delta State 
university Abraka, he is now a fully grown man with dreams and motivations that needs to be acheived
he has currently given his life to christ and ensures that he will do greater thigs for the kingdom 
of God to excel more and more """

st.write(content)

st.header("Our Team")

col1, empty_col1, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("imagess/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("imagess/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("imagess/" + row["image"])





#with col1:
    #st.image("images/photo.png")

#with col2:
    #st.title("Okoma Franklin")
    #content = """ My name is Okoma Franklin Chukwuma i am a student of Delta State University
    #Abraka, i am 23 years of age and i want to be a great pythom programmer and also impact much
    #of this knowledge on people around my vasinity
    #"""
    #st.info(content)

#st.write("Below you can find some of the apps i have built on python")

#col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

#df = pandas.read_csv("data.csv", sep = ";")
#with col3:
    #for index, row in df[:10].iterrows():
        #st.header(row["title"])
        #st.write(row["description"])
        #st.image("images/" + row["image"])
        #st.write(f"[source code]({row['url']})")

#with col4:
    #for index, row in df[10:].iterrows():
        #st.header(row["title"])
        #st.write(row["description"])
        #st.image("images/" + row["image"])
        #st.write(f"[source code]({row['url']})")







