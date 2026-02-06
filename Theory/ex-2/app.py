import numpy as np
stored_sapid = "500122856"
user_sapid = input("Enter your SAP ID: ")
if user_sapid == stored_sapid:
    print("Access granted.")
else:
    print("Access denied. Invalid SAP ID.")