import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientL2TP:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP VNET/L2TP Commands
    def clear_counters(self):
        return self.execute_command("clear counters")

    def create_l2tpv3_tunnel(self, tunnel_name, local_address, remote_address):
        return self.execute_command(f"create l2tpv3 tunnel {tunnel_name} local {local_address} remote {remote_address}")

    def set_interface_ip6_l2tpv3(self, interface, tunnel_name):
        return self.execute_command(f"set interface {interface} ip6 l2tpv3 tunnel-name {tunnel_name}")

    def set_l2tpv3_tunnel_cookie(self, tunnel_name, cookie):
        return self.execute_command(f"set l2tpv3 tunnel {tunnel_name} cookie {cookie}")

    def show_l2tpv3(self):
        return self.execute_command("show l2tpv3")

    def test_counters(self):
        return self.execute_command("test counters")

# Example usage
if __name__ == "__main__":
    vpp_client_l2tp = VPPClientL2TP()

    # Example: Clear Counters
    stdout, stderr = vpp_client_l2tp.clear_counters()
    print("Clear Counters Output:", stdout)
    print("Clear Counters Error:", stderr)

    # Add additional example usages as needed for other commands
