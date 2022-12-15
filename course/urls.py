from .import views 
from django.urls import path
from .views import Homeview

app_name="course"
urlpatterns = [
   
    path('register/', views.register,name="register"),
    path('login/',views.login,name="login"),
    path('home/',views.home,name="home"),
    path("forget_password/",views.forget_password,name="forget_password"),
    path("send_otp",views.send_otp,name="send_otp"),
    path("reset_password/",views.reset_password,name="reset_password"),
    path("changed/",views.changed,name="changed"),
    path("logout/",views.logoutfunction,name="logout"),
    # path('store/',views.store,name="store"),
    # path('cart/',views.cart,name="cart"),
    # path('checkout/',views.checkout,name="checkout"),
    path('hi/',Homeview.as_view(),name="homed"),
]
