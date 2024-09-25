from django import forms

# 입력받을 애들만 적으면 됨 created_at은 입력 안받으니까 안적어
# TextField는 없음 
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
