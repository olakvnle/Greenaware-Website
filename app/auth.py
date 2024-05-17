from django.http import Http404
from django.contrib.auth.mixins import AccessMixin


class IsNotObserverMixin(AccessMixin):
    """
    Mixin to prevent observers from accessing the view.
    """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_observer:
            raise Http404("Observers are not allowed to access this page.")
        return super().dispatch(request, *args, **kwargs)


class IsNotSubscriberMixin(AccessMixin):
    """
    Mixin to prevent subscribers from accessing the view.
    """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and  request.user.is_observer:
            raise Http404("Subscribers are not allowed to access this page.")
        return super().dispatch(request, *args, **kwargs)













    # Retrieve the JWT token and refresh token from session
    # jwt_token = request.session.get('jwt_access_token')
    # refresh_token = request.session.get('jwt_refresh_token')
    # print(jwt_token, refresh_token)
    # if jwt_token:
    #     # Include the JWT token in API requests as needed
    #     headers = {'Authorization': f'Bearer {jwt_token}'}
    #     # Make API requests with the JWT token included in the headers
    #
    #     # Example: Verify JWT token against API endpoint
    #     api_verify_url = 'http://127.0.0.1:3000/api/v1/jwt/verify/'
    #     verify_response = requests.post(api_verify_url,
    #                                     json={'token': jwt_token},
    #                                     headers=headers,
    #                                     verify=False,
    #
    #                                     )
    #
    #     if verify_response.status_code == 201:
    #         # Token is valid,
    #         return True
    #     elif refresh_token:
    #         # Token is invalid, attempt to refresh it using the refresh token
    #         api_refresh_url = 'http://127.0.0.1:3000/api/v1/jwt/refresh/'
    #         refresh_response = requests.post(api_refresh_url,
    #                                          data={'refresh_token': refresh_token},
    #                                          headers=headers,
    #                                          verify=False,
    #
    #                                          )
    #
    #         if refresh_response.status_code == 201:
    #             # Refresh successful, obtain new tokens from the response
    #             new_tokens = refresh_response.json()
    #
    #             # Update session with new tokens
    #             request.session['jwt_token'] = new_tokens['access']
    #             # Note: Refresh token may remain unchanged or be updated by the API
    #
    #             # Retry API request with the new JWT token
    #             headers['Authorization'] = f'Bearer {new_tokens["access_token"]}'
    #             verify_response = requests.post(api_verify_url, headers=headers,
    #                                             data={'token': refresh_token},
    #                                             verify=False,
    #                                             )
    #
    #             if verify_response.status_code == 201:
    #                 # Token is now valid,
    #                 return True
    #
    # # If no valid token
    # return False
