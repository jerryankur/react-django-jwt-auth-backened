from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
	path('user-auth/', obtain_jwt_token)
]