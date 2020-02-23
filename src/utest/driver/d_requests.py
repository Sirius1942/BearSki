import requests


def get(url, params=None, **kwargs):
  return requests.get(url,params,**kwargs)

def post(url, data=None, json=None, **kwargs):
  return requests.post(url, data, json, **kwargs)

def delete(url, **kwargs):
  return requests.delete(url, **kwargs)

def put(url, data=None, **kwargs):
  return requests.put(url, data=None, **kwargs)

def patch(url, data=None, **kwargs):
  return requests.patch(url, data=None, **kwargs)

def head(url, **kwargs):
  return requests.head(url, **kwargs)

def options(url, **kwargs):
  return requests.options(url,**kwargs)
