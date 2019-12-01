import requests

def get(url, params=None, **kwargs):
  return requests.get(url,params,**kwargs)

def post(url, data=None, json=None, **kwargs):
  return requests.post(url, data, json, **kwargs)


