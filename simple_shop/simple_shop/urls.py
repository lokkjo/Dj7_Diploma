from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  re_path(r'^accounts/',
                          include('django.contrib.auth.urls')),
                  path('shop/', include('goods.urls')),
                  path('', include('index_page.urls'))
              ] + static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)
