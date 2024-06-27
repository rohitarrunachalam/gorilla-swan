import logging
from vpp_papi import VPPApiClient

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class COPClient:
    def __init__(self):
        self.vpp = VPPApiClient()
        self.vpp.connect('vpp_api_client')
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command, **params):
        self.logger.debug(f"Running command: {command} with parameters {params}")
        try:
            response = getattr(self.vpp.api, command)(**params)
            return response, None
        except AttributeError:
            error_msg = f"Command '{command}' not available in VPP API"
            self.logger.error(error_msg)
            return None, error_msg
        except Exception as e:
            self.logger.error(f"Error executing command {command}: {e}")
            return None, str(e)

    def cop_interface(self, sw_if_index, enable=True):
        params = {
            'sw_if_index': sw_if_index,
            'enable_disable': 1 if enable else 0
        }
        return self.run_vpp_command('cop_interface_enable_disable', **params)

    def cop_whitelist(self, ip4_address=None, ip6_address=None, sw_if_index=None):
        params = {
            'ip4_address': ip4_address,
            'ip6_address': ip6_address,
            'sw_if_index': sw_if_index,
            'is_add': 1 if ip4_address or ip6_address else 0
        }
        return self.run_vpp_command('cop_whitelist_enable_disable', **params)


# Example usage
if __name__ == "__main__":
    cop_client = COPClient()

    # Example: Enable COP Interface
    response, error = cop_client.cop_interface(sw_if_index=1, enable=True)
    if error:
        print(f"Error enabling COP Interface: {error}")
    else:
        print(f"COP Interface enabled successfully: {response}")

    # Example: Add IP4 address to COP whitelist
    response, error = cop_client.cop_whitelist(ip4_address='192.168.1.1', sw_if_index=1)
    if error:
        print(f"Error adding IP4 address to COP whitelist: {error}")
    else:
        print(f"IP4 address added to COP whitelist successfully: {response}")

    # Add additional example usages as needed
