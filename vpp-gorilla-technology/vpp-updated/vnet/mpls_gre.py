import logging
from vpp_papi import VPPApiClient  # Ensure VPPApiClient is imported correctly

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientMPLSGRE:
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

    # VPP VNET/MPLS-GRE Commands (replace with actual VPP API method names)
    def create_mpls_ethernet_policy_tunnel(self):
        return self.execute_command("mpls_ethernet_policy_tunnel_create")

    def create_mpls_ethernet_tunnel(self):
        return self.execute_command("mpls_ethernet_tunnel_create")

    def create_mpls_gre_tunnel(self):
        return self.execute_command("mpls_gre_tunnel_create")

    def show_mpls_tunnel(self):
        return self.execute_command("mpls_tunnel_show")

    def mpls_decap_add(self):
        return self.execute_command("mpls_decap_add")

    def mpls_decap_delete(self):
        return self.execute_command("mpls_decap_delete")

    def mpls_encap_add(self):
        return self.execute_command("mpls_encap_add")

    def mpls_encap_delete(self):
        return self.execute_command("mpls_encap_delete")

    def show_mpls_fib(self):
        return self.execute_command("mpls_fib_show")

# Example usage
if __name__ == "__main__":
    vpp_client_mpls_gre = VPPClientMPLSGRE()

    # Example: Show MPLS Tunnel
    response, error = vpp_client_mpls_gre.show_mpls_tunnel()
    if error:
        print("Show MPLS Tunnel Error:", error)
    else:
        print("Show MPLS Tunnel Output:", response)

    # Add additional example usages as needed for other commands
