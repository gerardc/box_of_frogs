class CategoryResource:
    def __init__(self, web):
        self.web = web
        pass

    async def fetch_one(self, request):
        return self.web.Response(text="Hello, world")

    async def fetch_all(self, request):
        id = request.match_info.get('id', "Anonymous")
        txt = "Hello, {}".format(id)
        return self.web.Response(text=txt)
    
    async def create(self, request):
        return self.web.Response(text="Hello, post")

    async def update(self, request):
        id = request.match_info.get('id', "Anonymous")
        txt = "Hello, {}".format(id)
        return self.web.Response(text=txt)

    async def delete(self, request):
        id = request.match_info.get('id', "Anonymous")
        txt = "Hello, {}".format(id)
        return self.web.Response(text=txt)