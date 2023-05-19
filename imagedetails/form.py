from django import forms
from .models import Image
from django.core.exceptions import ValidationError
import tomllib
config_filepath = 'config.toml'

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','description','category','image')

    def clean_image(self):  
        image_file=self.cleaned_data.get('image')
        with open(config_filepath, 'rb') as f:            
            data = tomllib.load(f)
            image_size = data.get('image_validation')['image_size']
            image_format = data.get('image_validation')['image_format']
            image_size_error = data.get('image_validation')['image_size_error']
            image_format_error = data.get('image_validation')['image_format_error']
            image_empty_error = data.get('image_validation')['image_empty_error']
      
        if not image_file:
              raise ValidationError(image_empty_error)
        else:
             extension = image_file.name.split(".")[-1]
        if extension not in image_format:
               raise ValidationError(image_format_error)
        if image_file:
            if image_file.size > image_size:
                raise ValidationError(image_size_error)
            return image_file
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].error_messages['invalid_image'] = 'Please upload a JPG or PNG image.'

