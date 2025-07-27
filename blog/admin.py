from django.contrib import admin
from django.contrib.admin import register
from blog.models import ProductType, ProductAttribute, Comment, Post


class ProductAttributeInline(admin.TabularInline):  # class ProductAttributeInline(admin.StackedInline):
    model = ProductAttribute


class PostInline(admin.TabularInline):
    model = Post


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


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["comment", "mood", "create_time", "modified_time"]
    list_display_links = ["comment"]
    list_filter = ["mood"]
    search_fields = ["comment", "mood", "create_time", "modified_time"]
    inlines = [PostInline]


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["image_url", "caption", "like", "comment", "create_time", "modified_time"]
    list_display_links = ["image_url"]
    list_filter = ["like"]
    list_editable = ["like"]
    search_fields = ["image_url", "caption", "like", "comment", "create_time", "modified_time"]


admin.site.register(ProductType, ProductTypeAdmin)
# admin.site.register(ProductAttribute)
# admin.site.register(PostAdmin)











