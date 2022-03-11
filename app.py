import os
import json
from tkinter import Image
from turtle import color
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

from pinata import pin_file_to_ipfs, pin_json_to_ipfs, convert_data_to_json

load_dotenv()

def set_background_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://blusignalsystems.com/wp-content/uploads/2016/12/Savin-NY-Website-Background-Web1.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_background_url()

#Title = '<p style="font-family:Courier; color:Purple; font-size: 20px;">Testing if this works</p>'
#st.markdown(Title, unsafe_allow_html=True)
# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Load_Contract Function
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./ABI.json')) as f:
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract


# Load the contract
contract = load_contract()

#st.markdown('<p style=“color:blue">Enterprise Car Subscription Options</p>', unsafe_allow_html=True )
from PIL import Image

image_4 = Image.open("logo-enterprise.jpeg")
st.image(image_4, width=700)
st.title("Enterprice Car Subscription")
st.write ("Our car subscription service is the solution for those who want more flexibility than you get with car leasing. Instead of investing money in new cars that go down in value, save your money for vacations or other expenses. It’s also hard to know if you will want to drive the same car in 1, 2 or even 5 years, so it’s better to stay flexible. With our tokenized car subscription you can be a worry-free part of your life, just like your streaming service or a gym membership! With an all-inclusive car subscription service, you have mobility with no fuss at a fixed price. Get a car immediately and keep it for as long as you want!")

st.title ("Subscription Benifits")
st.write ("Call and reserve the vehicle you want from a range of sedans, SUVs and pickup trucks. Insurance, maintenance and roadside assistance are covered. Access to diverse, extensive fleet in 90+ countries and territories. Access to Emerald Aisle, Emerald Alerts, and status match. ")

st.title ("How it Works")
st.write ("Step 1. Reserve - Login, select the vehicle you want and how long you'll need it. With our wallet you can reserve vehicles on-the-go. Step 2. Unlock and Go - Hold your wallet token over the windshield sensor to unlock the vehicle, the keys will be waiting for you inside. Step 3. Return - Return the vehicle at the end of your reservation. Hold your wallet token over the reader one last time, the doors will lock and your rental has ended.")
st.markdown("---")


st.title("Input your Etherium Wallet Account")
accounts = w3.eth.accounts
address = st.selectbox("Input Account", options=accounts)

st.markdown("---")

st.title("Economy")
st.title("Price: 300 Eth")
if st.button ("Detials of Package 1"):
        st.markdown("The standard subscription service offered. Access to Compact Cars through Standard SUVs. No upgrades avalaible")  

if st.button ("Purchase Package 1"):
    st.markdown("Congradulations On Your Subscription!") 
    st.balloons() 

from PIL import Image

image_1 = Image.open("car1.jpeg")
st.image(image_1, width=400)

st.markdown("---")  

st.title("Full Size")
st.title("Price: 500 Eth")
if st.button ("Detials of Package 2"):
        st.markdown("The Upgraded from tear 1 subscription offering services of...")  
if st.button ("Purchase Package 2"):
      st.markdown("Congradulations On Your Subscription!")
      st.balloons()  
    
from PIL import Image

image_2 = Image.open("car2.jpeg")
st.image(image_2, width=400)

st.markdown("---")  

st.title("luxury")
st.title("Price: 500 Eth")
if st.button ("Detials of Package 3"):

        st.markdown("ully comprehensive, insurance Re")  
if st.button ("Purchase Package 3"):
    st.markdown("Congradulations On Your Subscription!")  
    st.balloons()

from PIL import Image

image_3 = Image.open("car3.jpeg")
st.image(image_3, width=400)

