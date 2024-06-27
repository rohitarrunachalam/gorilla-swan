import logging
from vpp_papi import VPPApiClient

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class APPacketClient:
    def __init__(self):
        self.vpp = VPPApiClient()
        self.vpp.connect('vpp_api_client')
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command, **kwargs):
        self.logger.debug(f"Running command: {command} with arguments {kwargs}")
        try:
            response = getattr(self.vpp.api, command)(**kwargs)
            return response, None
        except AttributeError:
            error_msg = f"Command '{command}' not available in VPP API"
            self.logger.error(error_msg)
            return None, error_msg
        except Exception as e:
            self.logger.error(f"Error executing command {command}: {e}")
            return None, str(e)

    def create_host_interface(self, name):
        command = 'create_host_interface'
        kwargs = {'name': name}
        return self.run_vpp_command(command, **kwargs)

    def delete_host_interface(self, name):
        command = 'delete_host_interface'
        kwargs = {'name': name}
        return self.run_vpp_command(command, **kwargs)

# Example usage
if __name__ == "__main__":
    vpp_client = APPacketClient()

    # Example: Create Host Interface
    response, error = vpp_client.create_host_interface('eth0')
    if error:
        print(f"Error: {error}")
    else:
        print(f"Response: {response}")

    # Example: Delete Host Interface
    response, error = vpp_client.delete_host_interface('eth0')
    if error:
        print(f"Error: {error}")
    else:
        print(f"Response: {response}")
