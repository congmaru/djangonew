from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#USER 재정의 후 장고의 기존 Form 사용시 default로 사용하던 'auth.Form'이 아니므로 에러가 발생
#새로 정의한 'accounts.User'를 생성할 수 있도록 Form 재정의
#아래 코드 : 기존 'auth.forms'에서 사용하는 UserCreationForm의 기능을 모두 가져온 뒤 model만 우리가 정의한 모델로 바꿈.
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['email', 'first_name']