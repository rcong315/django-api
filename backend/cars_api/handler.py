import os
import sys
from django.core.wsgi import get_wsgi_application
from django.core.handlers.wsgi import WSGIRequest
from django.urls import resolve
from io import BytesIO


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'cars_api')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cars_api.settings')

application = get_wsgi_application()

def lambda_handler(event, context):

    print(event)

    # Extract required information from the event object
    http_method = event['requestContext']['httpMethod']
    path = event.get('path', '/')
    headers = event.get('headers', {})
    body = event.get('body', '')
    if body is None:
        body = '{}'
    body = BytesIO(body.encode())

    # Create Django request object
    request = WSGIRequest({
        'REQUEST_METHOD': http_method,
        'PATH_INFO': path,
        'HTTP_HOST': headers.get('Host', ''),
        'CONTENT_TYPE': headers.get('Content-Type', ''),
        'CONTENT_LENGTH': headers.get('Content-Length', ''),
        'wsgi.input': body,
        'wsgi.errors': sys.stderr,
        'wsgi.multiprocess': False,
        'wsgi.multithread': False,
        'wsgi.run_once': False,
        'wsgi.url_scheme': 'http',
        'wsgi.version': (1, 0),
    })

    # Resolve the URL and call the view function
    match = resolve(request.path_info)
    response = match.func(request, *match.args, **match.kwargs)

    # Ensure the response is rendered before accessing its content
    if hasattr(response, 'render') and callable(response.render):
        response = response.render()

    # Convert Django response to Lambda-compatible response
    return {
        'statusCode': response.status_code,
        'headers': dict(response.items()),
        'body': response.content.decode('utf-8'),
    }
