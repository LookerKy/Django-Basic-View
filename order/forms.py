from django import forms
from .models import Order
from product.models import Product
from users.models import Users
from django.db import transaction

class RegisterForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(error_messages={
        'required': '수량을 입력해주세요'
    }, label="수량")

    product = forms.IntegerField(error_messages={
        'required': '상품 가격을 입력해주세요'
    }, widget=forms.HiddenInput)

    def clean(self):
        clean_data = super().clean()
        quantity = clean_data.get('quantity')
        product_id = clean_data.get('product')
        user = self.request.session.get('user')

        if quantity and product_id and user:
            with transaction.atomic():
                prod = Product.objects.get(pk=product_id)
                order = Order(
                    quantity=quantity,
                    product=prod,
                    user=Users.objects.get(email=user)
                )
                order.save()
                prod.stuck -= quantity
                prod.save()
        else:
            self.product = product_id
            self.add_error('quantity', "값이 없습니다.")
            self.add_error('product', "값이 없습니다.")
            self.add_error('user', "값이 없습니다.")