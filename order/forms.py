from django import forms
from .models import Order


class RegisterForm(forms.Form):
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
