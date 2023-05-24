from django import forms
from .models import Image
from django.core.exceptions import ValidationError
from config import MyConfigClass

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','description','category','image')

    def clean_image(self):  
        image_file=self.cleaned_data.get('image')
        setting_config=MyConfigClass().validation_setting()
      
        if not image_file:
              raise ValidationError(setting_config.image_empty_error)
        else:
            if image_file:
                extension = image_file.name.split(".")[-1]
            if extension not in setting_config.image_format:
               raise ValidationError(setting_config.image_format_error)
            if image_file.size > setting_config.image_size:
                raise ValidationError(setting_config.image_size_error)
            return image_file
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].error_messages['invalid_image'] = 'Please upload a JPG or PNG image.'

