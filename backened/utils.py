from account.serializers import UserSerializer

# obtain_jwt_token only returns token, add userdata to it by overloading JWT_RESPONSE_PAYLOAD_HANDLER setting
def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }