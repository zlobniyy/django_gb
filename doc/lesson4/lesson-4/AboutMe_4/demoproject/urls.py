from django.conf.urls import url
from mainapp.views import main, works, learn, hobby
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main, name='main'),
    url(r'^works/$', works, name='works'),
    url(r'^learns/$', learn, name='learns'),
    url(r'^hobby/$', hobby, name='hobby'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
