import streamlit  as sg
import pandas

sg.set_page_config(layout="wide")
sg.header("The Best Company")

description="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip 
ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum.
"""

sg.text(description)
sg.title("Our Team")
df = pandas.read_csv("data.csv",sep=",")

col1,col2,col3=sg.columns([1,1,1])

with col1:
    for index,row in df[:4].iterrows():
        firstName = row["first name"]
        lastName = row["last name"]
        roleName = row["role"]
        imagePath="images/"+row["image"]
        sg.subheader(f"{firstName} {lastName}".title())
        sg.text(roleName)
        sg.image(imagePath)

with col2:
    for index,row in df[4:8].iterrows():
        firstName = row["first name"]
        lastName = row["last name"]
        roleName = row["role"]
        imagePath = "images/" + row["image"]
        sg.subheader(f"{firstName} {lastName}".title())
        sg.text(roleName)
        sg.image(imagePath)


with col3:
    for index,row in df[8:].iterrows():
        firstName = row["first name"]
        lastName = row["last name"]
        roleName = row["role"]
        imagePath = "images/" + row["image"]
        sg.subheader(f"{firstName} {lastName}".title())
        sg.text(roleName)
        sg.image(imagePath)

