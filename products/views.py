from django.shortcuts import render

# Create your views here.
from products.models import Product


def home_view(request):
        object_list=Product.objects.all()
        navhome ='home'
        return render(request,'home.html',{'object_list':object_list, 'navhome':navhome, })

def intro_view(request):
    navintro='intro'
    return render(request,'intro.html',{'navintro':navintro,})
def product_nav_view(request):
    navproduct='product'
    return render(request, 'product_nav.html', {'navproduct':navproduct, })
def service_nav_view(request):
    navservice='service'
    return render(request,'service_nav.html',{'navservice':navservice,})
def solution_nav_view(request):
    navsolution='solution'
    return render(request,'solution_nav.html',{'navsolution':navsolution,})
def news_nav_view(request):
    navnews='news'
    return render(request,'news_nav.html',{'navnews':navnews,})
def promotional_nav_view(request):
    navpromotional='promotional'
    return render(request,'promotional_nav.html',{'navpromotional':navpromotional,})
def contact_nav_view(request):
    navcontact='contact'
    return render(request,'contact_nav.html',{'navcontact':navcontact,})

# gọi hàm cho từng loại sản phẩm
def mikrotik_view(request):
    object_mikrotik=Product.objects.filter(brand='Mikrotik')
    return  render(request,'brand_pages/mikrotik.html',{'object_mikrotik':object_mikrotik, })
def draytek_view(request):
    object_draytek=Product.objects.filter(brand='Draytek')
    return  render(request,'brand_pages/draytek.html',{'object_draytek':object_draytek, })
def tplink_view(request):
    object_tplink=Product.objects.filter(brand='TPLink')
    return  render(request,'brand_pages/tplink.html',{'object_tplink':object_tplink, })
def hpe_view(request):
    object_hpe=Product.objects.filter(brand='HPE')
    return  render(request,'brand_pages/hpe.html',{'object_hpe':object_hpe, })
def unifi_view(request):
    object_unifi=Product.objects.filter(brand='Unifi')
    return  render(request,'brand_pages/unifi.html',{'object_unifi':object_unifi , })
def camera_view(request):
    object_camera=Product.objects.filter(brand='Camera')
    return  render(request,'brand_pages/camera.html',{'object_camera':object_camera, })
def linksys_view(request):
    object_linksys=Product.objects.filter(brand='Linksys')
    return  render(request,'brand_pages/linksys.html',{'object_linksys':object_linksys, })
def other_view(request):
    object_other=Product.objects.filter(brand='Other')
    return  render(request,'brand_pages/other.html',{'object_other':object_other, })


# classify
def router_view(request):
    object_router=Product.objects.filter(classify='Router')
    return render(request,'classify_pages/router.html',{'object_router':object_router,})
def switch_view(request):
    object_switch=Product.objects.filter(classify='Switch/Hub')
    return render(request,'classify_pages/switch.html',{'object_switch':object_switch,})
def wifi_view(request):
    object_wifi=Product.objects.filter(classify='Wifi')
    return render(request,'classify_pages/wifi.html',{'object_wifi':object_wifi,})
def camera_classify_view(request):
    object_camera=Product.objects.filter(classify='Camera')
    return render(request,'classify_pages/camera.html',{'object_camera':object_camera,})

# gọi hàm cho từng sản phẩm
def mikrotik202101_view(request):
    object_mikrotik=Product.objects.filter(brand='Mikrotik')
    return render(request,'product_pages/mikrotik202101.html',{'object_mikrotik':object_mikrotik,})
def mikrotik202102_view(request):
    object_mikrotik=Product.objects.filter(brand='Mikrotik')
    return render(request,'product_pages/mikrotik202102.html',{'object_mikrotik':object_mikrotik,})
def draytek202101_view(request):
    object_draytek=Product.objects.filter(brand='Draytek')
    return render(request,'product_pages/draytek202101.html',{'object_draytek':object_draytek,})
def draytek202102_view(request):
    object_draytek=Product.objects.filter(brand='Draytek')
    return render(request,'product_pages/draytek202102.html',{'object_draytek':object_draytek,})
def tplink202101_view(request):
    object_tplink=Product.objects.filter(brand='TPLink')
    return render(request,'product_pages/tplink202101.html',{'object_tplink':object_tplink,})
def tplink202102_view(request):
    object_tplink=Product.objects.filter(brand='TPLink')
    return render(request,'product_pages/tplink202102.html',{'object_tplink':object_tplink,})
def hpe202101_view(request):
    object_hpe=Product.objects.filter(brand='HPE')
    return render(request,'product_pages/hpe202101.html',{'object_hpe':object_hpe,})
def hpe202102_view(request):
    object_hpe=Product.objects.filter(brand='HPE')
    return render(request,'product_pages/hpe202102.html',{'object_hpe':object_hpe,})
def unifi202101_view(request):
    object_unifi=Product.objects.filter(brand='Unifi')
    return render(request,'product_pages/unifi202101.html',{'object_unifi':object_unifi,})
def unifi202102_view(request):
    object_unifi=Product.objects.filter(brand='Unifi')
    return render(request,'product_pages/unifi202102.html',{'object_unifi':object_unifi,})
def linksys202101_view(request):
    object_linksys=Product.objects.filter(brand='Linksys')
    return render(request,'product_pages/linksys202101.html',{'object_linksys':object_linksys,})
def linksys202102_view(request):
    object_linksys=Product.objects.filter(brand='Linksys')
    return render(request,'product_pages/linksys202102.html',{'object_linksys':object_linksys,})
def camera202101_view(request):
    object_camera=Product.objects.filter(brand='Camera')
    return render(request,'product_pages/camera202101.html',{'object_camera':object_camera,})
def camera202102_view(request):
    object_camera=Product.objects.filter(brand='Camera')
    return render(request,'product_pages/camera202102.html',{'object_camera':object_camera,})
def other202101_view(request):
    object_other=Product.objects.filter(brand='Other')
    return render(request,'product_pages/other202101.html',{'object_other':object_other,})
def other202102_view(request):
    object_other=Product.objects.filter(brand='Other')
    return render(request,'product_pages/other202102.html',{'object_other':object_other,})
