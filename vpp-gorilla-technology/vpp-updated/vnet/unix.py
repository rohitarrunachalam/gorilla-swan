import logging
from vpp_papi import VPPApiClient  # Ensure VPPApiClient is imported correctly

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientUnix:
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

    # VPP VNET/Unix Commands
    def show_gdb(self):
        return self.execute_command("unix_show_gdb")

    def tap_connect(self):
        return self.execute_command("unix_tap_connect")

    def tap_delete(self):
        return self.execute_command("unix_tap_delete")

    def tap_modify(self):
        return self.execute_command("unix_tap_modify")

# Example usage
if __name__ == "__main__":
    vpp_client_unix = VPPClientUnix()

    # Example: Show GDB
    response, error = vpp_client_unix.show_gdb()
    if error:
        print("Show GDB Error:", error)
    else:
        print("Show GDB Output:", response)

    # Add additional example usages as needed for other commands
