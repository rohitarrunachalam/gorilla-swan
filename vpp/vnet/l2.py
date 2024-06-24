import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientL2:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP VNET/L2 Commands
    def set_bridge_domain_arp_entry(self, bridge_domain, ip_address, mac_address):
        return self.execute_command(f"set bridge-domain {bridge_domain} arp entry {ip_address} {mac_address}")

    def set_bridge_domain_arp_term(self, bridge_domain, ip_address):
        return self.execute_command(f"set bridge-domain {bridge_domain} arp term {ip_address}")

    def set_bridge_domain_flood(self, bridge_domain, interface):
        return self.execute_command(f"set bridge-domain {bridge_domain} flood {interface}")

    def set_bridge_domain_forward(self, bridge_domain, interface):
        return self.execute_command(f"set bridge-domain {bridge_domain} forward {interface}")

    def set_bridge_domain_learn(self, bridge_domain, interface):
        return self.execute_command(f"set bridge-domain {bridge_domain} learn {interface}")

    def set_bridge_domain_uu_flood(self, bridge_domain, interface):
        return self.execute_command(f"set bridge-domain {bridge_domain} uu-flood {interface}")

    def show_bridge_domain(self):
        return self.execute_command("show bridge-domain")

    def set_interface_l2_classify(self, interface, classify_table):
        return self.execute_command(f"set interface {interface} l2 classify {classify_table}")

    def set_interface_l2_efp_filter(self, interface, filter_name):
        return self.execute_command(f"set interface {interface} l2 efp-filter {filter_name}")

    def clear_l2fib(self):
        return self.execute_command("clear l2fib")

    def l2fib_add(self, mac_address, bridge_domain, interface):
        return self.execute_command(f"l2fib add {mac_address} {bridge_domain} {interface}")

    def l2fib_del(self, mac_address):
        return self.execute_command(f"l2fib del {mac_address}")

    def show_l2fib(self):
        return self.execute_command("show l2fib")

    def test_l2fib(self, mac_address):
        return self.execute_command(f"test l2fib {mac_address}")

    def set_interface_l2_flood(self, interface, bridge_domain):
        return self.execute_command(f"set interface {interface} l2 flood {bridge_domain}")

    def set_interface_l2_forward(self, interface, bridge_domain):
        return self.execute_command(f"set interface {interface} l2 forward {bridge_domain}")

    def set_interface_l2_bridge(self, interface, bridge_domain):
        return self.execute_command(f"set interface {interface} l2 bridge {bridge_domain}")

    def set_interface_l2_xconnect(self, interface, destination_interface):
        return self.execute_command(f"set interface {interface} l2 xconnect {destination_interface}")

    def show_mode(self):
        return self.execute_command("show mode")

    def set_interface_l2_learn(self, interface):
        return self.execute_command(f"set interface {interface} l2 learn")

    def set_interface_acl_output(self, interface, acl_name):
        return self.execute_command(f"set interface {interface} acl output {acl_name}")

    def show_l2patch(self):
        return self.execute_command("show l2patch")

    def test_l2patch(self, interface):
        return self.execute_command(f"test l2patch {interface}")

    def l2_rewrite_entry(self, entry_name, mac_address, bridge_domain, interface):
        return self.execute_command(f"l2 rewrite entry {entry_name} mac {mac_address} bridge-domain {bridge_domain} interface {interface}")

    def set_bridge_domain_rewrite(self, bridge_domain, rewrite_entry):
        return self.execute_command(f"set bridge-domain {bridge_domain} rewrite {rewrite_entry}")

    def set_interface_l2_rewrite(self, interface, rewrite_entry):
        return self.execute_command(f"set interface {interface} l2 rewrite {rewrite_entry}")

    def show_l2_rewrite_entries(self):
        return self.execute_command("show l2 rewrite entries")

    def show_l2_rewrite_interfaces(self):
        return self.execute_command("show l2 rewrite interfaces")

    def set_interface_l2_tag_rewrite(self, interface, tag_rewrite_entry):
        return self.execute_command(f"set interface {interface} l2 tag-rewrite {tag_rewrite_entry}")

    def set_interface_l2_xcrw(self, interface, xcrw_entry):
        return self.execute_command(f"set interface {interface} l2 xcrw {xcrw_entry}")

    def show_l2xcrw(self):
        return self.execute_command("show l2xcrw")

# Example usage
if __name__ == "__main__":
    vpp_client_l2 = VPPClientL2()

    # Example: Set Bridge Domain ARP Entry
    stdout, stderr = vpp_client_l2.set_bridge_domain_arp_entry(10, '192.168.1.1', '00:11:22:33:44:55')
    print("Set Bridge Domain ARP Entry Output:", stdout)
    print("Set Bridge Domain ARP Entry Error:", stderr)

    # Add additional example usages as needed for other commands
