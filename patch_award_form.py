import sys
import re

with open('Construz/MBTApp/forms.py', 'r') as f:
    content = f.read()

old_award = """class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = '__all__'
        widgets = {
            'image': UploadImageWidget,
        }"""

new_award = """class AwardForm(forms.ModelForm):
    image = UploadUrlField(label='Logotyp / Grafika')
    _multipart = forms.FileField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        _clear_upload_cache()
        super().__init__(*args, **kwargs)

    class Meta:
        model = Award
        fields = '__all__'
        widgets = {'_multipart': forms.HiddenInput()}"""

content = content.replace(old_award, new_award)

with open('Construz/MBTApp/forms.py', 'w') as f:
    f.write(content)
