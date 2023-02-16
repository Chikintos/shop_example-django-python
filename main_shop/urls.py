
from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name="main"),
    path('about-us',views.aboutUs,name="aboutus"),
    path('user/register',views.registrPanel,name="register"),
    path('user/login',views.LoginPanel,name="login"),
    path('logout/',views.UserLogout,name='logout'),
    path('user/settings',views.Settings,name='settings'),
    path('password/',views.changepassword,name='passwordchange'),
    path('saveorder',views.saveorder,name='saveorder'),
    path('product/<int:id>',views.ProductPage),
    path('product/makeorder/<int:id>/<int:num>',views.OrderPage),
    path('product/makeorder',views.OrderPage,name='makeorder'),
    path('product/addToBasket/<int:id>/<int:num>/<str:user>',views.addtobasket),
    path('basket',views.basket,name="basket"),
    path('category/<int:id>',views.category),
    path('user/clearBasket',views.clearBasket)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
    
    