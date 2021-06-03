from django.conf.urls import url, include
from django.contrib import admin

import developers

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r'^developers/', include('developers.urls')),
]
