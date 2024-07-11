from django.forms import ModelForm
from .models import Profile

class ProfileCreationForm(ModelForm):
    class Meta:
        #상속받을 model 클래스명
        model = Profile
        #상속받을 model 클래스의 필드 즉, 입력받을 속성
        fields = ["image", "nickname", "message"]
