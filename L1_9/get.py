import urllib.request as urllib 

response = urllib.urlopen('https://tiffanypoon.com')
text = response.read().decode('utf-8')
print(text)
