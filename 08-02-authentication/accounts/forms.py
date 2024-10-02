from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# django는 User 모델 직접 참조를 권장 X 
# from .models import User

# 그래서 django는 User 간접참조 방법 제공 
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email') 