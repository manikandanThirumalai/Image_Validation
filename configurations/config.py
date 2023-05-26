config_filepath = 'configurations\\config.toml'
import toml

class ConfigClass:
    with open(config_filepath, 'r') as f:
     config = toml.load(f)

    DATABASE_CONFIG = config['database']
    
    def __init__(self):
        pass


    def load_app_config_settings(self):
        with open(config_filepath, 'r') as f:
            config = toml.load(f)
            self.sender_email_id = config['email_service']['sender_email_id']
            self.receiver_email_id = config['email_service']['receiver_email_id']
            self.email_auth = config['email_service']['email_auth']
            self.sender_email_msg = config['email_service']['sender_email_msg']
            return self
        
