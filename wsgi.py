from paste.httpserver import serve
from pyramid.config import Configurator
from pyramid.response import Response

def dump_environ(request):
    return Response(
        body='\n'.join('{0}={1}'.format(k,v) 
                       for (k,v) in request.environ.items()),
        content_type='text/plain')

config = Configurator()
config.add_route('dump_environ', '/')
config.add_view(dump_environ, route_name='dump_environ')
application = config.make_wsgi_app()

if __name__ == '__main__':
    serve(application, host='0.0.0.0')
