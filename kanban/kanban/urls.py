from django.conf.urls import url
from django.contrib import admin

from profiles.urls import urlpatterns as profiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
] + profiles_urlpatterns
