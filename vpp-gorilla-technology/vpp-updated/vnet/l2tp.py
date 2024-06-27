import logging
from vpp_papi import VPPApiClient  # Ensure VPPApiClient is imported correctly

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientL2TP:
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

    # VPP VNET/L2TP Commands
    def clear_counters(self):
        return self.execute_command('clear_counters')

    def l2tpv3_create_tunnel(self, local_address, remote_address):
        params = {
            'client_address': local_address,
            'our_address': remote_address
        }
        return self.execute_command('l2tpv3_create_tunnel', **params)

    def set_interface_l2tpv3(self, sw_if_index, vpp_address):
        params = {
            'sw_if_index': sw_if_index,
            'vpp_address': vpp_address
        }
        return self.execute_command('l2tpv3_set_interface', **params)

    def l2tpv3_set_tunnel_cookie(self, sw_if_index, cookie):
        params = {
            'sw_if_index': sw_if_index,
            'cookie': cookie
        }
        return self.execute_command('l2tpv3_set_tunnel_cookie', **params)

    def l2tpv3_tunnel_dump(self):
        return self.execute_command('l2tpv3_tunnel_dump')

    def test_counters(self):
        return self.execute_command('test_counters')

# Example usage
if __name__ == "__main__":
    vpp_client_l2tp = VPPClientL2TP()

    # Example: Clear Counters
    response, error = vpp_client_l2tp.clear_counters()
    if error:
        print("Clear Counters Error:", error)
    else:
        print("Clear Counters Output:", response)

    # Example: Create L2TPv3 Tunnel
    response, error = vpp_client_l2tp.l2tpv3_create_tunnel(local_address='192.168.1.1', remote_address='192.168.2.1')
    if error:
        print("Create L2TPv3 Tunnel Error:", error)
    else:
        print("Create L2TPv3 Tunnel Output:", response)

    # Example: Set Interface L2TPv3
    response, error = vpp_client_l2tp.set_interface_l2tpv3(sw_if_index=1, vpp_address='192.168.1.1')
    if error:
        print("Set Interface L2TPv3 Error:", error)
    else:
        print("Set Interface L2TPv3 Output:", response)

    # Example: Set L2TPv3 Tunnel Cookie
    response, error = vpp_client_l2tp.l2tpv3_set_tunnel_cookie(sw_if_index=1, cookie=12345)
    if error:
        print("Set L2TPv3 Tunnel Cookie Error:", error)
    else:
        print("Set L2TPv3 Tunnel Cookie Output:", response)

    # Example: Show L2TPv3 Tunnel
    response, error = vpp_client_l2tp.l2tpv3_tunnel_dump()
    if error:
        print("Show L2TPv3 Tunnel Error:", error)
    else:
        print("Show L2TPv3 Tunnel Output:", response)

    # Example: Test Counters
    response, error = vpp_client_l2tp.test_counters()
    if error:
        print("Test Counters Error:", error)
    else:
        print("Test Counters Output:", response)

    # Add additional example usages as needed for other commands
