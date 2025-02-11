
from django.contrib import admin
from django.urls import include, path
from .views import index, charcount, analyzer, capitalfirst, space_remove
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('analyzer', analyzer, name="analyzer")
]
