"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
import xadmin
from django.views.static import serve
from MxShop.settings import MEDIA_ROOT

from goods.views import GoodsListViewSet, CategoryViewSet
from users.views import SmsCodeViewset, UserViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from trade.views import ShoppingCartViewset, OrderViewset, AlipayView

from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'goods', GoodsListViewSet)
router.register(r'categorys', CategoryViewSet, basename="categorys")
router.register(r'code', SmsCodeViewset, basename="code")
router.register(r'users', UserViewset, basename="users")
router.register(r'userfavs', UserFavViewset, basename="userfavs")
router.register(r'messages', LeavingMessageViewset, basename="messages")
router.register(r'address',AddressViewset , basename="address")
router.register(r'shopcarts', ShoppingCartViewset, basename="shopcarts")
router.register(r'orders', OrderViewset, basename="orders")

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('ueditor/',include('DjangoUeditor.urls')),
    path('xadmin/', xadmin.site.urls),
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    path('docs', include_docs_urls(title='mxshop')),
    path('api-auth', include('rest_framework.urls')),
    re_path('^', include(router.urls)),
    #path('api-token-auth/', views.obtain_auth_token),
    path('login/', obtain_jwt_token),
    path('alipay/return/', AlipayView.as_view()),
]
