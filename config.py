import tomllib
config_filepath = 'config.toml'

class MyConfigClass:
    def __init__(self):
        # Initialize any required resources or dependencies here
        pass

    def validation_setting(self):
        with open('config.toml', 'rb') as toml_file:    
            config = tomllib.load(toml_file)
            self.image_size = config.get('image_validation')['image_size']
            self.image_format = config.get('image_validation')['image_format']
            self.image_size_error = config.get('image_validation')['image_size_error']
            self.image_format_error = config.get('image_validation')['image_format_error']
            self.image_empty_error = config.get('image_validation')['image_empty_error']
            return self
        
    def database_setting(self):
        with open('config.toml', 'rb') as toml_file:
            db_setting = tomllib.load(toml_file)
            self.engine = db_setting.get('database')['engine']
            self.database_name = db_setting.get('database')['database_name']
            self.username = db_setting.get('database')['username']
            self.password = db_setting.get('database')['password']
            self.host = db_setting.get('database')['host']
            self.port = db_setting.get('database')['port']
            return self