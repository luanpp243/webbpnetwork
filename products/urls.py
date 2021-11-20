from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from products import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.home_view, name='home'),
   path('intro/', views.intro_view, name='intro'),
   path('product/', views.product_nav_view, name='product_nav'),
   path('service/', views.service_nav_view, name='service_nav'),
   path('solution/', views.solution_nav_view, name='solution_nav'),
   path('news/', views.news_nav_view, name='news_nav'),
   path('promotional/', views.promotional_nav_view, name='promotional_nav'),
   path('contact/', views.contact_nav_view, name='contact_nav'),

   #url brand sản phẩm
   path('mikrotik/', views.mikrotik_view, name='mikrotik'),
   path('draytek/', views.draytek_view, name='draytek'),
   path('tplink/', views.tplink_view, name='tplink'),
   path('hpe/', views.hpe_view, name='hpe'),
   path('unifi/', views.unifi_view, name='unifi'),
   path('camera/', views.camera_view, name='camera'),
   path('linksys/', views.linksys_view, name='linksys'),
   path('other/', views.other_view, name='other'),
   # url classify
   path('router/', views.router_view, name='router'),
   path('switch/', views.switch_view, name='switch'),
   path('wifi/', views.wifi_view, name='wifi'),
   path('camera/', views.camera_classify_view, name='camera'),

   #url chi tiết sản phẩm
   path('mikrotik202101/',views.mikrotik202101_view),
   path('mikrotik202102/',views.mikrotik202102_view),
   path('draytek202101/', views.draytek202101_view),
   path('draytek202102/', views.draytek202102_view),
   path('tplink202101/', views.tplink202101_view),
   path('tplink202102/', views.tplink202102_view),
   path('hpe202101/', views.hpe202101_view),
   path('hpe202102/', views.hpe202102_view),
   path('unifi202101/', views.unifi202101_view),
   path('unifi202102/', views.unifi202102_view),
   path('linksys202101/', views.linksys202101_view),
   path('linksys202102/', views.linksys202102_view),
   path('camera202101/', views.camera202101_view),
   path('camera202102/', views.camera202102_view),
   path('other202101/', views.other202101_view),
   path('other202102/', views.other202102_view),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)