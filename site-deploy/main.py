from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route


def index(request):
    if (header_count := len(request.headers)) > 5:
        return PlainTextResponse(f'lots of headers: {header_count}')
    else:
        return PlainTextResponse('not many headers')


def startup():
    print('Ready to go')


routes = [
    Route('/', index),
]

app = Starlette(debug=True, routes=routes, on_startup=[startup])
