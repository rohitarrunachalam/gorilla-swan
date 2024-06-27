import logging
from vpp_papi import VPPApiClient  # Ensure VPPApiClient is imported correctly

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientLawfulIntercept:
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

    # VPP VNET/Lawful Intercept Commands
    def li_set_interface(self, sw_if_index, direction, port):
        params = {
            'sw_if_index': sw_if_index,
            'direction': direction,
            'port': port
        }
        return self.execute_command('li_set_interface', **params)

# Example usage
if __name__ == "__main__":
    vpp_client_li = VPPClientLawfulIntercept()

    # Example: Set Lawful Intercept
    response, error = vpp_client_li.li_set_interface(sw_if_index=1, direction=1, port=1234)
    if error:
        print("Set Lawful Intercept Error:", error)
    else:
        print("Set Lawful Intercept Output:", response)

    # Add additional example usages as needed for other commands
