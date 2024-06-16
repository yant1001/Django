from django import forms
from .models import Product

class ProductRegisterForm(forms.Form):
    product_name = forms.CharField(
        error_messages={'required': '상품명을 입력해주세요'}, label="상품명")

    product_price = forms.IntegerField(
        error_messages={'required': '상품가격을 입력해주세요'}, label="상품가격")

    product_desc = forms.CharField(
        error_messages={'required': '상품설명을 입력해주세요'}, label="상품설명")

    product_stock = forms.IntegerField(
        error_messages={'required': '상품재고을 입력해주세요'}, label="상품재고")

    # 유효성 검증
    def clean(self):
        cleaned_data = super().clean()

        product_name = cleaned_data.get("product_name")
        product_price = cleaned_data.get("product_price")
        product_desc = cleaned_data.get("product_desc")
        product_stock = cleaned_data.get("product_stock")

        if product_name and product_price and product_desc and product_stock:
            product = Product(
                product_name = product_name,
                product_price = product_price,
                product_desc = product_desc,
                product_stock = product_stock
            )

            product.save()