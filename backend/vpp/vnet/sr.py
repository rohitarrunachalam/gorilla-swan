import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientSR:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP VNET/SR Commands
    def set_ip6_sr_rewrite(self):
        return self.execute_command("set ip6 sr rewrite")

    def show_sr_hmac(self):
        return self.execute_command("show sr hmac")

    def show_sr_multicast_map(self):
        return self.execute_command("show sr multicast-map")

    def show_sr_policy(self):
        return self.execute_command("show sr policy")

    def show_sr_tunnel(self):
        return self.execute_command("show sr tunnel")

    def sr_hmac(self):
        return self.execute_command("sr hmac")

    def sr_multicast_map(self):
        return self.execute_command("sr multicast-map")

    def sr_policy(self):
        return self.execute_command("sr policy")

    def sr_tunnel(self):
        return self.execute_command("sr tunnel")

    def test_sr_debug(self):
        return self.execute_command("test sr debug")

    def test_sr_hmac(self):
        return self.execute_command("test sr hmac")

# Example usage
if __name__ == "__main__":
    vpp_client_sr = VPPClientSR()

    # Example: Show SR HMAC
    stdout, stderr = vpp_client_sr.show_sr_hmac()
    print("Show SR HMAC Output:", stdout)
    print("Show SR HMAC Error:", stderr)

    # Add additional example usages as needed for other commands
