from django.conf.urls import url, include
from django.contrib import admin
from kanban import api_urls

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
    url(r'^api-token-auth/', obtain_jwt_token)
]
