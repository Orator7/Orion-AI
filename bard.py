# import bard
#
# # Replace "YOUR_API_KEY" with the actual API Key obtained earlier
# API_KEY = "AIzaSyDL92liLM22YOT8K_5Ygm3MoMHiGb_rAbA"
#
# def main():
# 	query = "What is the meaning of life?"
# 	response = google_bard.generate_text(query, api_key=AIzaSyDL92liLM22YOT8K_5Ygm3MoMHiGb_rAbA)
# 	print("Google Bard Response (Using google_bard Module):")
# 	print(response)
import bardapi
import os

# set your __Secure-1PSID value to key
# token = 'AIzaSyA4uNwaZALnni4sHWAaP77xw7_d8-AP2LM.'

# def main():
# 	# set your input text
# 	input_text = "who is narendra modi"
#
# 	# Send an API request and get a response.
# 	response = bardapi.core.Bard(token).get_answer(input_text)
# 	print(response)
from bardapi import Bard
import os
os.environ['_BARD_API_KEY']="dQhi6ChMT3DIBWaIxStlgoHR_hYpylhC0UXoVcFmBWvDYNK0QIZaOQ13OacORsKTYJzg-A."

response = Bard().get_answer("who is modi")['content']
print(response)


# if __name__ == "__main__":
#
# 	main()
