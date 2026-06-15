def api_Call():
	try:
		import requests
		import config as apiurlFunc
		apiaddr=apiurlFunc.apiUrl()
		response=requests.get(apiaddr)
		response.raise_for_status()
		data=response.json()
		return data
	except Exception as e:
		print("Error received from api call-",e)