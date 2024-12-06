from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import streamlit as st

#  Step 1 : Launching IMDB URL to get movie details

driver_path = r'geckodriver.exe'
service1 = Service(driver_path)
driver = webdriver.Firefox(service=service1)

movie_rating_appurl = "https://www.imdb.com/chart/top/"
driver.get(movie_rating_appurl) 
driver.implicitly_wait(5)

# Step 2: Get the Options from Streamlit

st.title("Movie Fetcher Application Menu")

option = st.selectbox(
    "Select your Options",
    ("Get the Movie Details and Display","Quit"),
)

st.write("You Selected",option)

# Step 3: Get the Movie Name from streamlit dropdown
users_Movie_Selection = st.text_input("Enter the movie name: ")
st.write("Users Movie Selection : ",users_Movie_Selection)

try:
    if(option == "Get the Movie Details and Display"):
        movie_name = driver.find_element(By.XPATH,"//h3[contains(text(),'"+users_Movie_Selection+"')]")
        st.text(movie_name.text)   
        rating_class = "ipc-rating-star--rating"
        movie_rating = driver.find_element(By.XPATH,"//span[@class='"+rating_class+"']")
        st.text(movie_rating.text)
        other_details_class ="sc-300a8231-7 eaXxft cli-title-metadata-item"
        movies_otherdetails = driver.find_element(By.XPATH,"//span[@class='"+other_details_class+"']")               
        st.text(movies_otherdetails.text)
        
    if(option=="Quit"):
        st.text("User wish to close the session!")
        driver.quit()
except Exception as e:
    st.text("Exception:",e)



                                                           