import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

	payload = data
	headers = {
    					"accept": "application/json",
    					"content-type": "application/json",
    					"authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI2MjRjYTk1OS1jZDFkLTQ2NzEtOTY3My01MTEzODQ4ZTI2NTQiLCJlbWFpbCI6InZpbmhjaXRAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siaWQiOiJGUkExIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9LHsiaWQiOiJOWUMxIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6IjY4NWVhOGIxNTc5MTg2MWU2YzM2Iiwic2NvcGVkS2V5U2VjcmV0IjoiNDRmMzE4YWI2ZDA3YWIyMmFjMWVjMDU2MTNiYjZiNDU3YjllOWY1ZmQ5MGQ0NWViMzIzY2Q2Y2IzMjlmZjYyMSIsImlhdCI6MTcwNTg5ODA1MX0.DEvs3wXWcQfzw3dpQxuidgup82IqyhAurLU3XntpfOk"
						}
	response = requests.post(url, json=payload, headers=headers)
	return response['IpfsHash']

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	data = requests.get('https://gateway.pinata.cloud/ipfs/'+cid)
	data = json.loads(data.text)
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
