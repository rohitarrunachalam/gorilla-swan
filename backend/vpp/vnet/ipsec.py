import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientIPSec:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP VNET/IPSec Commands
    def ikev2_profile(self, profile_name, key_exchange='ikev2', encryption='aes-cbc-256', integrity='sha256'):
        return self.execute_command(f"ikev2 profile {profile_name} key-exchange {key_exchange} encryption {encryption} integrity {integrity}")

    def set_ikev2_local_key(self, profile_name, key_type, key_value):
        return self.execute_command(f"set ikev2 local-key {profile_name} type {key_type} value {key_value}")

    def show_ikev2_profile(self):
        return self.execute_command("show ikev2 profile")

    def show_ikev2_sa(self):
        return self.execute_command("show ikev2 sa")

    def clear_ipsec_counters(self):
        return self.execute_command("clear ipsec counters")

    def create_ipsec_tunnel(self, tunnel_name, local_ip, remote_ip, profile_name):
        return self.execute_command(f"create ipsec tunnel {tunnel_name} local-ip {local_ip} remote-ip {remote_ip} profile {profile_name}")

    def ipsec_policy(self, policy_name, action, priority=100):
        return self.execute_command(f"ipsec policy {policy_name} action {action} priority {priority}")

    def ipsec_sa(self):
        return self.execute_command("ipsec sa")

    def ipsec_spd(self):
        return self.execute_command("ipsec spd")

    def set_interface_ipsec_key(self, interface, direction, key_type, key_value):
        return self.execute_command(f"set interface ipsec key {interface} {direction} {key_type} {key_value}")

    def set_interface_ipsec_spd(self, interface, direction, policy_name):
        return self.execute_command(f"set interface ipsec spd {interface} {direction} {policy_name}")

    def set_ipsec_sa(self, tunnel_name, spi, local_crypto_key, remote_crypto_key):
        return self.execute_command(f"set ipsec sa {tunnel_name} spi {spi} local-crypto-key {local_crypto_key} remote-crypto-key {remote_crypto_key}")

    def show_ipsec(self):
        return self.execute_command("show ipsec")

# Example usage
if __name__ == "__main__":
    vpp_client_ipsec = VPPClientIPSec()

    # Example: Create IKEv2 Profile
    stdout, stderr = vpp_client_ipsec.ikev2_profile('my_profile', key_exchange='ikev2', encryption='aes-cbc-256', integrity='sha256')
    print("Create IKEv2 Profile Output:", stdout)
    print("Create IKEv2 Profile Error:", stderr)

    # Add additional example usages as needed for other commands
