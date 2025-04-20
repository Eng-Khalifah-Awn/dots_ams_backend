from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt import views as jwt_views

from api import views
from api.views import *

app_name = "api_v1"

router_v1 = DefaultRouter()
router_v1.register(r'category', CategoriesViewSet, basename="specialization")
router_v1.register(r'brand', BrandCategoriesViewSet, basename="branch")
router_v1.register(r'company', CompanyViewSet, basename="day")
router_v1.register(r'department', DepartmentViewSet, basename="illness")
router_v1.register(r'assets', AssetsManagementViewSet, basename="medicine")
router_v1.register(r'user', CustomUserViewSet, basename="user")
router_v1.register(r'assets_images', AssetsImagesViewSet, basename="profile")

urlpatterns = [

    path('v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('v1/', include(router_v1.urls))

]

