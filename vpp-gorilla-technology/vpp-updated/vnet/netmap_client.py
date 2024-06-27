import logging
from vpp_papi import VPPApiClient  # Ensure VPPApiClient is imported correctly

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class NetmapClient:
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

    def create_netmap(self, interface, *options):
        params = {
            'interface': interface,
            'options': " ".join(options) if options else ""
        }
        return self.execute_command('netmap_create', **params)

    def delete_netmap(self, interface):
        params = {
            'interface': interface
        }
        return self.execute_command('netmap_delete', **params)

# Example usage
if __name__ == "__main__":
    netmap_client = NetmapClient()

    # Example: Create Netmap
    response, error = netmap_client.create_netmap('eth0', '-option1', '-option2')
    if error:
        print("Create Netmap Error:", error)
    else:
        print("Create Netmap Output:", response)

    # Example: Delete Netmap
    response, error = netmap_client.delete_netmap('eth0')
    if error:
        print("Delete Netmap Error:", error)
    else:
        print("Delete Netmap Output:", response)

    # Add additional example usages as needed for other commands
