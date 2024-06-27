import logging
from vpp_papi import VPPApiClient  # Ensure VPPApiClient is imported correctly

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientIPSec:
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

    # VPP VNET/IPSec Commands
    def ikev2_profile_add_del(self, name, op):
        params = {
            'name': name,
            'op': op
        }
        return self.execute_command('ikev2_profile_add_del', **params)

    def ikev2_set_local_key(self, name, key_type, file):
        params = {
            'name': name,
            'key_type': key_type,
            'file': file
        }
        return self.execute_command('ikev2_set_local_key', **params)

    def ikev2_profile_dump(self):
        return self.execute_command('ikev2_profile_dump')

    def ikev2_sa_dump(self):
        return self.execute_command('ikev2_sa_dump')

    def ipsec_spd_add_del(self, spd_id, is_add=True):
        params = {
            'spd_id': spd_id,
            'is_add': is_add
        }
        return self.execute_command('ipsec_spd_add_del', **params)

    def ipsec_sad_add_del_entry(self, is_add=True, entry=None):
        params = {
            'is_add': is_add,
            'entry': entry
        }
        return self.execute_command('ipsec_sad_add_del_entry', **params)

    def ipsec_spd_entry_add_del(self, spd_id, is_add=True, entry=None):
        params = {
            'spd_id': spd_id,
            'is_add': is_add,
            'entry': entry
        }
        return self.execute_command('ipsec_spd_entry_add_del', **params)

    def ipsec_interface_add_del_spd(self, sw_if_index, spd_id, is_add=True):
        params = {
            'sw_if_index': sw_if_index,
            'spd_id': spd_id,
            'is_add': is_add
        }
        return self.execute_command('ipsec_interface_add_del_spd', **params)

    def ipsec_sa_dump(self):
        return self.execute_command('ipsec_sa_dump')

    def ipsec_spd_dump(self):
        return self.execute_command('ipsec_spd_dump')

    def show_ipsec(self):
        return self.execute_command('ipsec_spd_dump')  # Example command to show IPsec policies

# Example usage
if __name__ == "__main__":
    vpp_client_ipsec = VPPClientIPSec()

    # Example: Create IKEv2 Profile
    response, error = vpp_client_ipsec.ikev2_profile_add_del(name='my_profile', op=1)
    if error:
        print("Create IKEv2 Profile Error:", error)
    else:
        print("Create IKEv2 Profile Output:", response)

    # Example: Set IKEv2 Local Key
    response, error = vpp_client_ipsec.ikev2_set_local_key(name='my_profile', key_type=1, file='/path/to/key/file')
    if error:
        print("Set IKEv2 Local Key Error:", error)
    else:
        print("Set IKEv2 Local Key Output:", response)

    # Example: Show IKEv2 Profile
    response, error = vpp_client_ipsec.ikev2_profile_dump()
    if error:
        print("Show IKEv2 Profile Error:", error)
    else:
        print("Show IKEv2 Profile Output:", response)

    # Add additional example usages as needed for other commands
