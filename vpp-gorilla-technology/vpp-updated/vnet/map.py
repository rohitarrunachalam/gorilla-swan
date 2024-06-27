import logging
from vpp_papi import VPPApiClient  # Ensure VPPApiClient is imported correctly

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientMAP:
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

    # VPP VNET/MAP Commands (replace with actual VPP API method names)
    def map_add_domain(self, domain):
        return self.execute_command("map_add_domain", domain=domain)

    def map_add_rule(self, domain, ip4_prefix, ip6_prefix):
        return self.execute_command("map_add_rule", domain=domain, ip4_prefix=ip4_prefix, ip6_prefix=ip6_prefix)

    def map_del_domain(self, domain):
        return self.execute_command("map_del_domain", domain=domain)

    def map_params_fragment(self):
        return self.execute_command("map_params_fragment")

    def map_params_fragment_ignore_df(self):
        return self.execute_command("map_params_fragment_ignore_df")

    def map_params_icmp_source_address(self):
        return self.execute_command("map_params_icmp_source_address")

    def map_params_icmp6_unreachables(self):
        return self.execute_command("map_params_icmp6_unreachables")

    def map_params_pre_resolve(self):
        return self.execute_command("map_params_pre_resolve")

    def map_params_reassembly(self):
        return self.execute_command("map_params_reassembly")

    def map_params_security_check(self):
        return self.execute_command("map_params_security_check")

    def map_params_security_check_fragments(self):
        return self.execute_command("map_params_security_check_fragments")

    def map_params_traffic_class(self):
        return self.execute_command("map_params_traffic_class")

    def show_map_domain(self):
        return self.execute_command("show_map_domain")

    def show_map_fragments(self):
        return self.execute_command("show_map_fragments")

    def show_map_stats(self):
        return self.execute_command("show_map_stats")

# Example usage
if __name__ == "__main__":
    vpp_client_map = VPPClientMAP()

    # Example: Show MAP Domain
    response, error = vpp_client_map.show_map_domain()
    if error:
        print("Show MAP Domain Error:", error)
    else:
        print("Show MAP Domain Output:", response)

    # Add additional example usages as needed for other commands
