from django.urls import path
from sh import views

urlpatterns=[
    path('',views.show,name="show"),
    path('register',views.register),
    path('collections',views.collections),
    path('collections/<str:name>',views.collections_view,name="collections"),
    path('collections/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('login',views.login_page),
    path('logout',views.logout_page),
    path('cart',views.cart_page,name="cart"),

]




