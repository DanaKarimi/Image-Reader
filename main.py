import requests
import json

image_url = input("Enter URL of the image: ")
url = f"https://api.apilayer.com/image_to_text/url?url={image_url}"

payload = {}
headers= {
  "apikey": "Nmik5E7q3pxG7gMWv6D5itqyFpkf9sqJ"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
result_html = result.encode('utf-8')
result_main = json.loads(result_html)


print(result_main["all_text"])