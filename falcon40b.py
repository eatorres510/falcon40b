import falcon

# Define a resource class that handles GET requests
class HelloWorldResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # Set the response status code
        resp.media = {'message': 'Hello, Falcon 4.0b!'}  # Set the response body as a JSON object

# Create an instance of the Falcon API
api = falcon.App()

# Instantiate the resource class
hello_world_resource = HelloWorldResource()

# Add a route to the API and associate it with the resource
api.add_route('/', hello_world_resource)

# Run the Falcon API
if __name__ == '__main__':
    from wsgiref import simple_server

    # Create a WSGI server using the Falcon API
    server = simple_server.make_server('localhost', 8000, api)

    print('Starting Falcon server on localhost:8000')
    # Start the server
    server.serve_forever()