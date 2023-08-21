class Authentication:
    def authenticate(self, request):
        # Add your implementation here
        # Example implementation: return request.headers.get('Authorization') == 'Bearer TOKEN'
        return request.headers.get('Authorization') == 'Bearer TOKEN'

    def require_authentication(self, route):
        # Add your implementation here
        # Example implementation: return route.startswith('/admin')
        return route.startswith('/admin')