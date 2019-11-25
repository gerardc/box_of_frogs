from aiohttp import web

class CategoryResource:
    def __init__(self):
        pass

    async def fetch_one(self, request):
        return web.Response(text="Hello, world")

    async def fetch_all(self, request):
        id = request.match_info.get('id', "Anonymous")
        txt = "Hello, {}".format(id)
        return web.Response(text=txt)
    
    async def create(self, request):
        return web.Response(text="Hello, post")

    async def update(self, request):
        id = request.match_info.get('id', "Anonymous")
        txt = "Hello, {}".format(id)
        return web.Response(text=txt)

    async def delete(self, request):
        id = request.match_info.get('id', "Anonymous")
        txt = "Hello, {}".format(id)
        return web.Response(text=txt)

categories = CategoryResource()

app = web.Application()
app.add_routes([web.get('/categories', categories.fetch_all),
                web.post('/categories', categories.create),
                web.get('/categories/{id}', categories.fetch_one),
                web.put('/categories/{id}', categories.update),
                web.delete('/categories{id}', categories.delete)])

if __name__ == '__main__':
    web.run_app(app)