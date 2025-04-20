from django.shortcuts import render
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import *
from api.serializers import *


class CategoriesViewSet(ModelViewSet):
    queryset = TblCategories.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    # filterset_fields = ['id_role__name_role', 'id_specialization__name']
    # search_fields = ['id_user__username', 'id_user__email', 'id_role__name_role', 'id_specialization__name']
    # ordering_fields = ['id_user__username', 'id_role__name_role', 'id_specialization__name', 'age', 'gender']
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, OAuth2Authentication]

    @method_decorator(ratelimit(key='ip', rate='5/m', method='GET', block=True))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(ratelimit(key='ip', rate='5/m', method='POST', block=True))
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @method_decorator(ratelimit(key='ip', rate='5/m', method='PUT', block=True))
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @method_decorator(ratelimit(key='ip', rate='5/m', method='DELETE', block=True))
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class BrandCategoriesViewSet(ModelViewSet):
    queryset = TblBrandCategories.objects.all()
    serializer_class = BrandCategoriesSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    # filterset_fields = ['id_role__name_role', 'id_specialization__name']
    # search_fields = ['id_user__username', 'id_user__email', 'id_role__name_role', 'id_specialization__name']
    # ordering_fields = ['id_user__username', 'id_role__name_role', 'id_specialization__name', 'age', 'gender']
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, OAuth2Authentication]


class CompanyViewSet(ModelViewSet):
    queryset = TblCompany.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    # filterset_fields = ['id_role__name_role', 'id_specialization__name']
    # search_fields = ['id_user__username', 'id_user__email', 'id_role__name_role', 'id_specialization__name']
    # ordering_fields = ['id_user__username', 'id_role__name_role', 'id_specialization__name', 'age', 'gender']
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, OAuth2Authentication]


class DepartmentViewSet(ModelViewSet):
    queryset = TblDepartment.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    # filterset_fields = ['id_role__name_role', 'id_specialization__name']
    # search_fields = ['id_user__username', 'id_user__email', 'id_role__name_role', 'id_specialization__name']
    # ordering_fields = ['id_user__username', 'id_role__name_role', 'id_specialization__name', 'age', 'gender']
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, OAuth2Authentication]


class AssetsManagementViewSet(ModelViewSet):
    queryset = TblAssetsManagement.objects.all()
    serializer_class = AssetsManagementSerializer
    filter_backends = [SearchFilter, OrderingFilter]

    # filterset_fields = ['id_role__name_role', 'id_specialization__name']
    # search_fields = ['id_user__username', 'id_user__email', 'id_role__name_role', 'id_specialization__name']
    # ordering_fields = ['id_user__username', 'id_role__name_role', 'id_specialization__name', 'age', 'gender']
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, OAuth2Authentication]


class CustomUserViewSet(ModelViewSet):
    queryset = TblCustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    # filterset_fields = ['id_role__name_role', 'id_specialization__name']
    # search_fields = ['id_user__username', 'id_user__email', 'id_role__name_role', 'id_specialization__name']
    # ordering_fields = ['id_user__username', 'id_role__name_role', 'id_specialization__name', 'age', 'gender']
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, OAuth2Authentication]


class AssetsImagesViewSet(ModelViewSet):
    queryset = TblAssetsImages.objects.all()
    serializer_class = AssetsImagesSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    # filterset_fields = ['id_role__name_role', 'id_specialization__name']
    # search_fields = ['id_user__username', 'id_user__email', 'id_role__name_role', 'id_specialization__name']
    # ordering_fields = ['id_user__username', 'id_role__name_role', 'id_specialization__name', 'age', 'gender']
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, OAuth2Authentication]
