import os
import json
from tkinter import Image
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

from pinata import pin_file_to_ipfs, pin_json_to_ipfs, convert_data_to_json

load_dotenv()

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

################################################################################
# Helper functions to pin files and json to Pinata
################################################################################

st.title("Buy Rental Tokens")
st.write("Choose an account to get started")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")


if st.button ("Buy Tokens"): 
    #w3.eth.balanceOf(address)

    tx_hash = contract.functions.weiRaised()
    #receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write(dict(tx_hash))

from PIL import Image

image_1 = Image.open("car1.jpeg")
image_2 = Image.open("car2.jpeg")
image_3 = Image.open("car3.jpeg")

st.image(image_1, width=400)
st.image(image_2, width=400)
st.image(image_3, width=400)

