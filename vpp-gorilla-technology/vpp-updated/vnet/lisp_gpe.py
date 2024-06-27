import logging
from vpp_papi import VPPApiClient  # Ensure VPPApiClient is imported correctly

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientLISPGPE:
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

    # VPP VNET/LISP-GPE Commands (replace with actual VPP API method names)
    def lisp_gpe_iface(self):
        return self.execute_command("lisp_gpe_iface")

    def lisp_gpe(self):
        return self.execute_command("lisp_gpe")

    def lisp_gpe_tunnel(self):
        return self.execute_command("lisp_gpe_tunnel")

    def show_lisp_gpe_interface(self):
        return self.execute_command("show_lisp_gpe_interface")

    def show_lisp_gpe_tunnel(self):
        return self.execute_command("show_lisp_gpe_tunnel")

# Example usage
if __name__ == "__main__":
    vpp_client_lisp_gpe = VPPClientLISPGPE()

    # Example: Show LISP GPE Tunnel
    response, error = vpp_client_lisp_gpe.show_lisp_gpe_tunnel()
    if error:
        print("Show LISP GPE Tunnel Error:", error)
    else:
        print("Show LISP GPE Tunnel Output:", response)

    # Add additional example usages as needed for other commands
