import yaml
import sys
import base64


def load_config():
    try:
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
            if not isinstance(config, dict):
                raise ValueError("Configuration file"
                                 " is not a valid YAML dictionary")
            if 'api_key' in config:
                config['api_key'] = base64.b64decode(
                    config['api_key']).decode('utf-8')
            return config
    except FileNotFoundError:
        print("Configuration file 'config.yaml' not found.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        sys.exit(1)
    except base64.binascii.Error as e:
        print(f"Error decoding base64 API key: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

