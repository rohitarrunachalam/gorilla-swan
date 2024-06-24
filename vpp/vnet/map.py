import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientMAP:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP VNET/MAP Commands
    def map_add_domain(self, domain):
        return self.execute_command(f"map add domain {domain}")

    def map_add_rule(self, domain, ip4_prefix, ip6_prefix):
        return self.execute_command(f"map add rule {domain} {ip4_prefix} {ip6_prefix}")

    def map_del_domain(self, domain):
        return self.execute_command(f"map del domain {domain}")

    def map_params_fragment(self):
        return self.execute_command("map params fragment")

    def map_params_fragment_ignore_df(self):
        return self.execute_command("map params fragment ignore-df")

    def map_params_icmp_source_address(self):
        return self.execute_command("map params icmp source-address")

    def map_params_icmp6_unreachables(self):
        return self.execute_command("map params icmp6 unreachables")

    def map_params_pre_resolve(self):
        return self.execute_command("map params pre-resolve")

    def map_params_reassembly(self):
        return self.execute_command("map params reassembly")

    def map_params_security_check(self):
        return self.execute_command("map params security-check")

    def map_params_security_check_fragments(self):
        return self.execute_command("map params security-check fragments")

    def map_params_traffic_class(self):
        return self.execute_command("map params traffic-class")

    def show_map_domain(self):
        return self.execute_command("show map domain")

    def show_map_fragments(self):
        return self.execute_command("show map fragments")

    def show_map_stats(self):
        return self.execute_command("show map stats")

# Example usage
if __name__ == "__main__":
    vpp_client_map = VPPClientMAP()

    # Example: Show MAP Domain
    stdout, stderr = vpp_client_map.show_map_domain()
    print("Show MAP Domain Output:", stdout)
    print("Show MAP Domain Error:", stderr)

    # Add additional example usages as needed for other commands
