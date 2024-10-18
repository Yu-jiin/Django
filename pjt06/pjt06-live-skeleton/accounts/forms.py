from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    # model 속성 제외하고 나머지는 모두 Meta 클래스를 그대루 
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        