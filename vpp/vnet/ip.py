import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientVnet:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP Commands
    def show_adjacency_alloc(self):
        return self.execute_command("show adjacency alloc")

    def set_interface_ip(self, interface, ip_address):
        return self.execute_command(f"set interface ip address {interface} {ip_address}")

    def set_interface_ip_table(self, interface, table_id):
        return self.execute_command(f"set interface ip table {interface} {table_id}")

    def set_ip_classify(self, table, mask, match):
        return self.execute_command(f"set ip classify table {table} mask {mask} match {match}")

    def set_ip_flow_hash(self, table, options):
        return self.execute_command(f"set ip flow-hash {table} {options}")

    def show_ip_local(self):
        return self.execute_command("show ip local")

    def test_lookup(self, table, address):
        return self.execute_command(f"test lookup {table} {address}")

    def set_ip_source_and_port_range_check(self, vrf, start_port, end_port):
        return self.execute_command(f"set ip source-and-port-range-check {vrf} {start_port} {end_port}")

    def show_ip_source_and_port_range_check(self):
        return self.execute_command("show ip source-and-port-range-check")

    def set_interface_ip_source_check(self, interface, enable=True):
        action = 'enable' if enable else 'disable'
        return self.execute_command(f"set interface ip source-check {interface} {action}")

    def test_route(self, address):
        return self.execute_command(f"test route {address}")

    def set_interface_ip6_table(self, interface, table_id):
        return self.execute_command(f"set interface ip6 table {interface} {table_id}")

    def set_ip6_classify(self, table, mask, match):
        return self.execute_command(f"set ip6 classify table {table} mask {mask} match {match}")

    def set_ip6_flow_hash(self, table, options):
        return self.execute_command(f"set ip6 flow-hash {table} {options}")

    def show_ip6_local(self):
        return self.execute_command("show ip6 local")

    def test_ip6_link(self, interface, ip6_address):
        return self.execute_command(f"test ip6 link {interface} {ip6_address}")

    def clear_ioam_rewrite(self):
        return self.execute_command("clear ioam rewrite")

    def set_ioam_destination(self, destination):
        return self.execute_command(f"set ioam destination {destination}")

    def set_ioam_rewrite(self, options):
        return self.execute_command(f"set ioam rewrite {options}")

    def show_ioam_summary(self):
        return self.execute_command("show ioam summary")

    def disable_ip6_interface(self, interface):
        return self.execute_command(f"disable ip6 interface {interface}")

    def enable_ip6_interface(self, interface):
        return self.execute_command(f"enable ip6 interface {interface}")

    def ip6_nd(self, options):
        return self.execute_command(f"ip6 nd {options}")

    def set_ip6_link_local_address(self, interface, address):
        return self.execute_command(f"set ip6 link-local address {interface} {address}")

    def set_ip6_neighbor(self, interface, neighbor, mac_address):
        return self.execute_command(f"set ip6 neighbor {interface} {neighbor} {mac_address}")

    def show_ip6_interface(self):
        return self.execute_command("show ip6 interface")

    def show_ip6_neighbors(self):
        return self.execute_command("show ip6 neighbors")

    def show_ip_features(self):
        return self.execute_command("show ip features")

    def show_ip_interface_features(self):
        return self.execute_command("show ip interface features")

    def ip_probe_neighbor(self, interface, address):
        return self.execute_command(f"ip probe-neighbor {interface} {address}")

    def ip_route(self, options):
        return self.execute_command(f"ip route {options}")

    def show_ip(self):
        return self.execute_command("show ip")

    def show_ip_fib(self):
        return self.execute_command("show ip fib")

    def show_ip4(self):
        return self.execute_command("show ip4")

    def show_ip6(self):
        return self.execute_command("show ip6")

    def show_ip6_fib(self):
        return self.execute_command("show ip6 fib")
    
    def test_crash(self):
        return self.execute_command("test crash")

# Example usage
if __name__ == "__main__":
    vpp_client_vnet = VPPClientVnet()

    # Example: Show Adjacency Alloc
    stdout, stderr = vpp_client_vnet.show_adjacency_alloc()
    print("Show Adjacency Alloc Output:", stdout)
    print("Show Adjacency Alloc Error:", stderr)

    # Example: Test Crash
    stdout, stderr = vpp_client_vnet.test_crash()
    print("Test Crash Output:", stdout)
    print("Test Crash Error:", stderr)

    # Add additional example usages as needed
