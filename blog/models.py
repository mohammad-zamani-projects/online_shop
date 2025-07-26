from django.db import models


class ProductType(models.Model):
    class Meta:
        verbose_name = "ProductType"
        verbose_name_plural = "ProductTypes"
        # db_table = "blog.PRODUCT_TYPE"

    def __str__(self):
        return self.title

    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=32, blank=True, null=True, verbose_name="TITLE")
    is_active = models.BooleanField(default=False, null=True)


# _________________________________________model separator ____________________________________________


class ProductAttribute(models.Model):
    class Meta:
        verbose_name = "ProductAttribute"
        verbose_name_plural = "ProductAttributes"
        # db_table = "blog.PRODUCT_ATTRIBUTE"

    def __str__(self):
        return self.title

    # INTEGER = 1
    # STRING = 2
    # FLOAT = 3
    # ATTRIBUTE_TYPE_FIELD = (
    #     (INTEGER, "Integer"),
    #     (STRING, "String"),
    #     (FLOAT, "Float"),
    # )

    BLACK = 1
    WHITE = 2
    RED = 3
    BLUE = 4
    GREEN = 5

    ATTRIBUTE_TYPE_FIELD = (
        (BLACK, "Black"),
        (WHITE, "White"),
        (RED, "Red"),
        (BLUE, "Blue"),
        (GREEN, "Green"),
    )

    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=32)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    # attribute_type = models.PositiveSmallIntegerField(default=WHITE, choices=ATTRIBUTE_TYPE_FIELD)
    attribute_type = models.PositiveSmallIntegerField(choices=ATTRIBUTE_TYPE_FIELD)
    is_active = models.BooleanField(default=False, null=True)


# _________________________________________model separator ____________________________________________

