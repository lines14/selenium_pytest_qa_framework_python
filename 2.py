from main.utils.API.base_API import BaseAPI

api = BaseAPI('https://jsonplaceholder.typicode.com', 'connect to API')

print((api.get('posts/1')).text)