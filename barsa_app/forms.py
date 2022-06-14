from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Имя')
    age = forms.IntegerField(label='Возраст')
    basket = forms.BooleanField(label='Желаете увидеть?', required=False)
    data = forms.DateField(label='Введите дату')
    sity = forms.TypedChoiceField(label='Выберите город', empty_value='Саранск', choices=(('Москва', 'Москва'), ('Самара', 'Самара'), ('Саратов', 'Саратов')))
    commy = forms.CharField(label='Комментарий', widget=forms.Textarea)

class UserForm_2(forms.Form):
    name = forms.CharField(label="Введите имя")
    age = forms.IntegerField(label='Введите возраст', min_value=18)
