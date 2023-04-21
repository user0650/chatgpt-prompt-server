import requests

# data = {
#     'op': 'add',
#     'nums': [1, 2, 3, 4, 5]
# }
# url = 'http://localhost:3001/calc'
# response = requests.post(url, json=data)
# result = response.json()['result']
# print(result)


data2 = {
    'url': 'https://item.jd.com/6039832.html'
}
server2 = 'http://localhost:3001/page'
response2 = requests.post(server2, json=data2)
result2 = response2.json()['result']
print(result2)
