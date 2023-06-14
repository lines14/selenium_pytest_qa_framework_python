import os
from requests_toolbelt import sessions
from requests.exceptions import HTTPError

session = sessions.BaseUrlSession(base_url='https://jsonplaceholder.typicode.com')
# headers = Request(method='get', headers={'Authorization': f'Bearer {os.environ.get("ACCESS_TOKEN") or ""}'})
# print(headers)
# prepared_request = session.prepare_request(headers)

try:
    response = session.get('posts/1')
    response.raise_for_status()
    print('success:', response.text)
except HTTPError:
    print('failed:', response.status_code)
except:
    print('fucked up')

# response = session.post('posts', json={
#     "title": "foo",
#     "body": "bar",
#     "userId": 777,
# })

# response = session.put('posts/1', headers={"Content-type": "application/json; charset=UTF-8"}, json={
#     "userId": 1,
#     "id": 1,
#     "title": "foo",
#     "body": "bar",
# })

# response = session.patch('posts/1', headers={"Content-type": "application/json; charset=UTF-8"}, json={
#     "title": "foo",
# })

# response = session.delete('posts/1')

print(response.text)

# super(options.baseURL || configManager.getApiConfigData().apiBaseUrl, 
# options.log || '[info] ▶ set base api url', 
# configManager.getConfigData().waitTime, 
# { Authorization: `Bearer ${process.env.ACCESS_TOKEN || ''}` });