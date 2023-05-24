from django import forms
from .models import Image
from django.core.exceptions import ValidationError
from configurations.configsettings import Validationdetails

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','description','category','image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # call the validation_setting function
        self.config = Validationdetails().validation_setting()
        image = self.cleaned_data.get('binaryimage')

        if not image:
            raise ValidationError(self.config.image_empty_error)
        else:
            if image:
                extension = image.name.split(".")[-1]
            if extension not in self.config.image_format:
                raise ValidationError(self.config.image_format_error)
            if image.size > self.config.image_size:
                raise ValidationError(self.config.image_size_error)
            return image

