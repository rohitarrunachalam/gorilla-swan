import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientMPLSGRE:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP VNET/MPLS-GRE Commands
    def create_mpls_ethernet_policy_tunnel(self):
        return self.execute_command("create mpls ethernet policy tunnel")

    def create_mpls_ethernet_tunnel(self):
        return self.execute_command("create mpls ethernet tunnel")

    def create_mpls_gre_tunnel(self):
        return self.execute_command("create mpls gre tunnel")

    def show_mpls_tunnel(self):
        return self.execute_command("show mpls tunnel")

    def mpls_decap_add(self):
        return self.execute_command("mpls decap add")

    def mpls_decap_delete(self):
        return self.execute_command("mpls decap delete")

    def mpls_encap_add(self):
        return self.execute_command("mpls encap add")

    def mpls_encap_delete(self):
        return self.execute_command("mpls encap delete")

    def show_mpls_fib(self):
        return self.execute_command("show mpls fib")

# Example usage
if __name__ == "__main__":
    vpp_client_mpls_gre = VPPClientMPLSGRE()

    # Example: Show MPLS Tunnel
    stdout, stderr = vpp_client_mpls_gre.show_mpls_tunnel()
    print("Show MPLS Tunnel Output:", stdout)
    print("Show MPLS Tunnel Error:", stderr)

    # Add additional example usages as needed for other commands
