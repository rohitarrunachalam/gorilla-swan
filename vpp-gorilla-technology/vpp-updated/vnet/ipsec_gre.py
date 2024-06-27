import logging
from vpp_papi import VPPApiClient  # Ensure VPPApiClient is imported correctly

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientIPSecGRE:
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

    # VPP VNET/IPSec-GRE Commands
    def create_ipsec_gre_tunnel(self, local_ip, remote_ip, table_id, tun_sw_if_index, outer_table_id, sa_out, sa_in):
        params = {
            'local_ip': local_ip,
            'remote_ip': remote_ip,
            'table_id': table_id,
            'tun_sw_if_index': tun_sw_if_index,
            'outer_table_id': outer_table_id,
            'sa_out': sa_out,
            'sa_in': sa_in,
        }
        return self.execute_command('ipsec_gre_tunnel_add_del', **params)

    def show_ipsec_gre_tunnel(self):
        return self.execute_command('ipsec_gre_tunnel_dump')

# Example usage
if __name__ == "__main__":
    vpp_client_ipsec_gre = VPPClientIPSecGRE()

    # Example: Create IPSec-GRE Tunnel
    response, error = vpp_client_ipsec_gre.create_ipsec_gre_tunnel(
        local_ip='192.168.1.1', remote_ip='192.168.2.1', table_id=0, tun_sw_if_index=0, outer_table_id=0, sa_out=0, sa_in=0
    )
    if error:
        print("Create IPSec-GRE Tunnel Error:", error)
    else:
        print("Create IPSec-GRE Tunnel Output:", response)

    # Example: Show IPSec-GRE Tunnel
    response, error = vpp_client_ipsec_gre.show_ipsec_gre_tunnel()
    if error:
        print("Show IPSec-GRE Tunnel Error:", error)
    else:
        print("Show IPSec-GRE Tunnel Output:", response)

    # Add additional example usages as needed for other commands
