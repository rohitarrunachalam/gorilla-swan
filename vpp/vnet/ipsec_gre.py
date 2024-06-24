import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientIPSecGRE:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP VNET/IPSec-GRE Commands
    def create_ipsec_gre_tunnel(self, tunnel_name, local_ip, remote_ip, profile_name):
        return self.execute_command(f"create ipsec gre tunnel {tunnel_name} local-ip {local_ip} remote-ip {remote_ip} profile {profile_name}")

    def show_ipsec_gre_tunnel(self):
        return self.execute_command("show ipsec gre tunnel")

# Example usage
if __name__ == "__main__":
    vpp_client_ipsec_gre = VPPClientIPSecGRE()

    # Example: Create IPSec-GRE Tunnel
    stdout, stderr = vpp_client_ipsec_gre.create_ipsec_gre_tunnel('my_tunnel', '192.168.1.1', '192.168.2.1', 'my_profile')
    print("Create IPSec-GRE Tunnel Output:", stdout)
    print("Create IPSec-GRE Tunnel Error:", stderr)

    # Add additional example usages as needed for other commands
