from aiohttp import web
import server

async def test_hello(aiohttp_client, loop):
    client = await aiohttp_client(server.build_application())
    resp = await client.get('/categories')
    assert resp.status == 200
    text = await resp.text()
    assert 'Hello, Anonymous' in text