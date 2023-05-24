from django import forms
from .models import Image
from django.core.exceptions import ValidationError
from configurations.configsettings import Validationdetails

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','description','category','image')

    def clean_image(self):  
        image_file=self.cleaned_data.get('image')
        self.config = Validationdetails().validation_setting()
        if not image_file:
              raise ValidationError(self.config.image_empty_error)
        else:
             extension = image_file.name.split(".")[-1]
        if extension not in self.config.image_format:
               raise ValidationError(self.config.image_format_error)
        if image_file:
            if image_file.size > self.config.image_size:
                raise ValidationError(self.config.image_size_error)
            return image_file
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].error_messages['invalid_image'] = 'Please upload a JPG or PNG image.'