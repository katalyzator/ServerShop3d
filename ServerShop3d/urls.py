from django.conf.urls import include, url
from django.contrib import admin
from tastypie.api import Api

from ServerShop3d import settings
from ShopServer.api import CategoryResource, ProductResource

v1 = Api(api_name='v1')
v1.register(ProductResource())
v1.register(CategoryResource())

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(v1.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
]
