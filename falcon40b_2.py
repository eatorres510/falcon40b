import falcon

# Define resource classes
class GreetingResource:
    def on_get(self, req, resp):
        resp.media = {'message': 'Hello, Falcon 4.0b!'}

class NameResource:
    def on_post(self, req, resp):
        data = req.media  # Get the request body
        name = data.get('name')
        resp.media = {'message': f'Hello, {name}!'} if name else {'message': 'Hello!'}
        resp.status = falcon.HTTP_201

class EchoResource:
    def on_post(self, req, resp):
        data = req.media  # Get the request body
        resp.media = data
        resp.status = falcon.HTTP_200

# Create an instance of the Falcon API
api = falcon.API()

# Instantiate resource classes
greeting_resource = GreetingResource()
name_resource = NameResource()
echo_resource = EchoResource()

# Add routes to the API and associate them with resources
api.add_route('/', greeting_resource)
api.add_route('/name', name_resource)
api.add_route('/echo', echo_resource)

# Run the Falcon API
if __name__ == '__main__':
    from wsgiref import simple_server

    # Create a WSGI server using the Falcon API
    server = simple_server.make_server('localhost', 8000, api)

    print('Starting Falcon server on localhost:8000')
    # Start the server
    server.serve_forever()