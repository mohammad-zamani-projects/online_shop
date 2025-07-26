from django.contrib import admin
from django.contrib.admin import register
from blog.models import ProductType, ProductAttribute


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute


# class ProductAttributeInline(admin.StackedInline):
#     model = ProductAttribute


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modified_time', 'is_active']
    list_display_links = ['title']
    list_filter = ['is_active']
    list_editable = ['is_active']
    search_fields = ['title', 'create_time', 'modified_time', 'is_active']
    inlines = [ProductAttributeInline]


@register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_type', 'attribute_type', 'create_time', 'modified_time', 'is_active']
    list_display_links = ['title', 'product_type']
    list_filter = ['product_type', 'is_active']
    list_editable = ['is_active']
    search_fields = ['title', 'product_type', 'attribute_type', 'create_time', 'modified_time', 'is_active']


admin.site.register(ProductType, ProductTypeAdmin)
# admin.site.register(ProductAttribute)
