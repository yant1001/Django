from django import forms
from .models import Order
from product.models import Product
from user.models import User

class OrderForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    order_qty = forms.CharField(
        error_messages={'required': '수량을 입력해 주세요.'},
        label='주문 수량'
        )
    
    product = forms.IntegerField(
        error_messages={'required': '수량을 입력해 주세요'}, 
        label='상품', 
        widget=forms.HiddenInput
        )
    
    def clean(self):
        cleaned_data = super().clean()

        order_qty = cleaned_data.get('order_qty')
        product_id = cleaned_data.get('product')

        # 로그인한 사용자의 정보는 session에 있음
        user_id = self.request.session.get('user')

        if order_qty and product_id and user_id:
            order = Order(
                order_qty=order_qty,
                product=Product.objects.get(pk=product_id),
                user = User.objects.get(pk=user_id)
            )

            order.save()
        else:
            if not product_id:
                self.add_error('product', '값이 없습니다.')
            if not order_qty:
                self.add_error('order_qty', "값이 없습니다.")