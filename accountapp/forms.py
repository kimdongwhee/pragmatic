from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# UserCreationForm 상속 및 재활용
class AccountUpdateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # UserCreationForm 필드 중 username 필드는 수정 못 하도록 잠금
        self.fields["username"].disabled = True

    def clean_username(self):
        # 현재 사용자명은 이미 존재하는 것으로 간주
        return self.instance.username
