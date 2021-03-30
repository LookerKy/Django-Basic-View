from django import forms
from .models import Product


class RegisterForm(forms.Form):
    name = forms.CharField(error_messages={
        'required': '상품명을 입력해주세요'
    }, max_length=64, label="상품명")

    price = forms.IntegerField(error_messages={
        'required': '상품 가격을 입력해주세요'
    }, label="상품 가격")

    description = forms.CharField(error_messages={
        'required': '상품 설명을 입력해주세요'
    }, label='상품 설명')

    stuck = forms.IntegerField(error_messages={
        'required': '상품 재고를 입력해주세요'
    }, label='상품 재고')

    def clean(self):
        clean_data = super().clean()
        name = clean_data.get('name')
        price = clean_data.get('price')
        description = clean_data.get('description')
        stuck = clean_data.get('stuck')

        if not(name and price and description and stuck):
            self.add_error('name', 'empty')
            self.add_error('pri  ce', 'empty')
            self.add_error('description', 'empty')
            self.add_error('stuck', 'empty')

