from aiohttp import web
from resources.category import CategoryResource



app = web.Application()
categories = CategoryResource(web)

app.add_routes([web.get('/categories', categories.fetch_all),
                web.post('/categories', categories.create),
                web.get('/categories/{id}', categories.fetch_one),
                web.put('/categories/{id}', categories.update),
                web.delete('/categories{id}', categories.delete)])

if __name__ == '__main__':
    web.run_app(app)