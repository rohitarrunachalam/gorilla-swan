import logging
from vpp_papi import VPPApiClient  # Ensure VPPApiClient is imported correctly

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VirtioClient:
    def __init__(self):
        self.vpp = VPPApiClient()
        self.vpp.connect('vpp_api_client')
        self.logger = logging.getLogger(__name__)

    def execute_command(self, api_method, **params):
        self.logger.debug(f"Running API method: {api_method} with parameters {params}")
        try:
            response = getattr(self.vpp.api, api_method)(**params)
            return response, None
        except AttributeError:
            error_msg = f"API method '{api_method}' not available in VPP API"
            self.logger.error(error_msg)
            return None, error_msg
        except Exception as e:
            self.logger.error(f"Error executing API method {api_method}: {e}")
            return None, str(e)

    def create_vhost_user(self, socket_path, *options):
        return self.execute_command("vhost_user_create",
                                    sock_filename=socket_path,
                                    **dict(option.split('=') for option in options))

    def delete_vhost_user(self, socket_path):
        return self.execute_command("vhost_user_delete", sock_filename=socket_path)

    def show_vhost_user(self, socket_path=None):
        if socket_path:
            return self.execute_command("vhost_user_dump", sock_filename=socket_path)
        else:
            return self.execute_command("vhost_user_dump")

# Example usage
if __name__ == "__main__":
    virtio_client = VirtioClient()

    # Example: Show Vhost User
    stdout, stderr = virtio_client.show_vhost_user()
    print("Show Vhost User Output:", stdout)
    print("Show Vhost User Error:", stderr)

    # Add additional example usages as needed for other commands
