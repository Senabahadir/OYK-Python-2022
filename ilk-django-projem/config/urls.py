from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.views import home #, ad_soyad_yaz, isim_yaz,python


urlpatterns = [
    path('python2022/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('kullanici/', include('django.contrib.auth.urls')),
    path('wallet/', include('wallet.urls', namespace='wallet')),
    path('vip/', include('vip.urls', namespace='vip')),
    

    path('', home, name='home'),
    # path('python/', python),
    # path('<isim>/', isim_yaz), 
    # path('<ad>/<soyad>/', ad_soyad_yaz),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
