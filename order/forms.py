from django import forms


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
        product = clean_data.get('product')

        if not (quantity and product):
            self.add_error('quantity', "값이 없습니다.")
            self.add_error('product', "값이 없습니다.")
            self.add_error('user', "값이 없습니다.")
