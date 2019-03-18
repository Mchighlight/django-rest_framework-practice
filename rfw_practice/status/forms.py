from django import forms

from .models import Status

class StatusForm(forms.ModelForm):
    class Meta:
        models = Status
        # Form頁面顯示格式
        fields = [
            'user',
            'content',
            'image'
        ]

    # 用來決定form是否符合規範
    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) > 240:
            raise forms.ValidationError("Content is too long")
        return content

    # 用來決定form是否符合規範
    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get("image",None)
        print(content)
        if content is None and image is None :
            raise forms.ValidationError('Content or image is require')
        return super().clean(*args, **kwargs)