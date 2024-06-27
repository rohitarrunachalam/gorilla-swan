import logging
from vpp_papi import VPPApiClient  # Ensure VPPApiClient is imported correctly

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientSR:
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

    # VPP VNET/SR Commands
    def set_ip6_sr_rewrite(self):
        return self.execute_command("sr_ip6_rewrite")

    def show_sr_hmac(self):
        return self.execute_command("sr_show_hmac")

    def show_sr_multicast_map(self):
        return self.execute_command("sr_show_multicast_map")

    def show_sr_policy(self):
        return self.execute_command("sr_show_policy")

    def show_sr_tunnel(self):
        return self.execute_command("sr_show_tunnel")

    def sr_hmac(self):
        return self.execute_command("sr_hmac")

    def sr_multicast_map(self):
        return self.execute_command("sr_multicast_map")

    def sr_policy(self):
        return self.execute_command("sr_policy")

    def sr_tunnel(self):
        return self.execute_command("sr_tunnel")

    def test_sr_debug(self):
        return self.execute_command("sr_test_debug")

    def test_sr_hmac(self):
        return self.execute_command("sr_test_hmac")

# Example usage
if __name__ == "__main__":
    vpp_client_sr = VPPClientSR()

    # Example: Show SR HMAC
    response, error = vpp_client_sr.show_sr_hmac()
    if error:
        print("Show SR HMAC Error:", error)
    else:
        print("Show SR HMAC Output:", response)

    # Add additional example usages as needed for other commands
