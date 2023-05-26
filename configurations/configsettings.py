import tomllib
config_filepath = 'configurations\config.toml'


class Validationdetails:
    def validation_setting(self):
        with open(config_filepath, 'rb') as f:    
            config = tomllib.load(f)
            self.image_size = config.get('image_validation')['image_size']
            self.image_format = config.get('image_validation')['image_format']
            self.image_size_error = config.get('image_validation')['image_size_error']
            self.image_format_error = config.get('image_validation')['image_format_error']
            self.image_empty_error = config.get('image_validation')['image_empty_error']
            return self