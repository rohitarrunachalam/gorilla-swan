import logging
from vpp_papi import VPPApiClient

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class CdpClient:
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

    def show_cdp(self):
        """
        Summary/usage:
        Show cdp command.

        Declaration:
        show_cdp_command (vnet/vnet/cdp/cdp_input.c:448)

        Implementation:
        show_cdp.
        """
        command = 'cdp_dump'  # Assuming the API equivalent is `cdp_dump`
        return self.run_vpp_command(command)

# Example usage
if __name__ == "__main__":
    cdp_client = CdpClient()

    # Example: Show CDP
    response, error = cdp_client.show_cdp()
    if error:
        print(f"Error: {error}")
    else:
        print(f"Response: {response}")
