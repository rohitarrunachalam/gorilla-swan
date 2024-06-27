import logging
from vpp_papi import VPPApiClient  # Ensure VPPApiClient is imported correctly

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientPolicer:
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

    # VPP VNET/Policer Commands
    def test_policer(self):
        return self.execute_command("policer_test")

    def configure_policer(self, policer_index, policer_params):
        params = {
            'policer_index': policer_index,
            'policer_params': policer_params
        }
        return self.execute_command("policer_configure", **params)

    def show_policer(self):
        return self.execute_command("policer_show")

# Example usage
if __name__ == "__main__":
    vpp_client_policer = VPPClientPolicer()

    # Example: Show Policier
    response, error = vpp_client_policer.show_policer()
    if error:
        print("Show Policier Error:", error)
    else:
        print("Show Policier Output:", response)

    # Add additional example usages as needed for other commands
