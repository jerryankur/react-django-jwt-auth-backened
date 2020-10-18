from account.views import current_user
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import current_user

urlpatterns = [
	path('user-auth/', obtain_jwt_token),
	path('current-user/', current_user),
]