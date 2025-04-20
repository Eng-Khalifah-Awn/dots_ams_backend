from rest_framework import serializers

from api.models import *


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblCategories
        fields = "__all__"


class BrandCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblBrandCategories
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TblCompany
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblDepartment
        fields = "__all__"


class AssetsManagementSerializer(serializers.ModelSerializer):
    name_brand_category = BrandCategoriesSerializer(read_only=True)
    name_brand_category_id = serializers.PrimaryKeyRelatedField(
        source='name_brand_category', queryset=TblBrandCategories.objects.all(), write_only=True
    )

    name_category = CategoriesSerializer(read_only=True)
    name_category_id = serializers.PrimaryKeyRelatedField(
        source='name_category', queryset=TblCategories.objects.all(), write_only=True
    )

    class Meta:
        model = TblAssetsManagement
        fields = "__all__"


class CustomUserSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        source="company", queryset=TblCompany.objects.all(), write_only=True
    )

    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        source="department", queryset=TblDepartment.objects.all(), write_only=True
    )

    class Meta:
        model = TblCustomUser
        fields = "__all__"


class AssetsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblAssetsImages
        fields = "__all__"
