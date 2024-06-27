import logging
from vpp_papi import VPPApiClient  # Ensure VPPApiClient is imported correctly

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientVnet:
    def __init__(self):
        self.vpp = VPPApiClient()
        self.vpp.connect('vpp_api_client')
        self.logger = logging.getLogger(__name__)

    def execute_command(self, command, **params):
        self.logger.debug(f"Running command: {command} with parameters {params}")
        try:
            response = getattr(self.vpp.api, command)(**params)
            return response, None
        except AttributeError:
            error_msg = f"Command '{command}' not available in VPP API"
            self.logger.error(error_msg)
            return None, error_msg
        except Exception as e:
            self.logger.error(f"Error executing command {command}: {e}")
            return None, str(e)

    # VPP Commands
    def show_adjacency_alloc(self):
        return self.execute_command('adjacency_dump')

    def set_interface_ip(self, interface, ip_address):
        return self.execute_command('sw_interface_set_ip_address', sw_if_index=interface, address=ip_address)

    def set_interface_ip_table(self, interface, table_id):
        return self.execute_command('sw_interface_set_table', sw_if_index=interface, vrf_id=table_id)

    def set_ip_classify(self, table, mask, match):
        return self.execute_command('ip_classify_table_add_del', table_index=table, mask=mask, match=match)

    def set_ip_flow_hash(self, table, options):
        return self.execute_command('ip_flow_hash_set', table_index=table, options=options)

    def show_ip_local(self):
        return self.execute_command('ip_address_dump')

    def test_lookup(self, table, address):
        return self.execute_command('ip_table_lookup', table_id=table, address=address)

    def set_ip_source_and_port_range_check(self, vrf, start_port, end_port):
        return self.execute_command('ip_source_and_port_range_check_add_del', vrf_id=vrf, start_port=start_port, end_port=end_port)

    def show_ip_source_and_port_range_check(self):
        return self.execute_command('ip_source_and_port_range_check_dump')

    def set_interface_ip_source_check(self, interface, enable=True):
        action = 1 if enable else 0
        return self.execute_command('sw_interface_ip_source_guard_enable_disable', sw_if_index=interface, enable=action)

    def test_route(self, address):
        return self.execute_command('ip_route_lookup', address=address)

    def set_interface_ip6_table(self, interface, table_id):
        return self.execute_command('sw_interface_set_ip6_table', sw_if_index=interface, vrf_id=table_id)

    def set_ip6_classify(self, table, mask, match):
        return self.execute_command('ip6_classify_table_add_del', table_index=table, mask=mask, match=match)

    def set_ip6_flow_hash(self, table, options):
        return self.execute_command('ip6_flow_hash_set', table_index=table, options=options)

    def show_ip6_local(self):
        return self.execute_command('ip6_address_dump')

    def test_ip6_link(self, interface, ip6_address):
        return self.execute_command('ip6_link_local_address', sw_if_index=interface, ip6_address=ip6_address)

    def clear_ioam_rewrite(self):
        return self.execute_command('ioam_clear_rewrite')

    def set_ioam_destination(self, destination):
        return self.execute_command('ioam_set_destination', destination=destination)

    def set_ioam_rewrite(self, options):
        return self.execute_command('ioam_set_rewrite', options=options)

    def show_ioam_summary(self):
        return self.execute_command('ioam_summary')

    def disable_ip6_interface(self, interface):
        return self.execute_command('ip6_disable', sw_if_index=interface)

    def enable_ip6_interface(self, interface):
        return self.execute_command('ip6_enable', sw_if_index=interface)

    def ip6_nd(self, options):
        return self.execute_command('ip6_nd_proxy_add_del', options=options)

    def set_ip6_link_local_address(self, interface, address):
        return self.execute_command('ip6_link_local_address_set', sw_if_index=interface, address=address)

    def set_ip6_neighbor(self, interface, neighbor, mac_address):
        return self.execute_command('ip6_neighbor_add_del', sw_if_index=interface, neighbor=neighbor, mac_address=mac_address)

    def show_ip6_interface(self):
        return self.execute_command('ip6_interface_dump')

    def show_ip6_neighbors(self):
        return self.execute_command('ip6_neighbor_dump')

    def show_ip_features(self):
        return self.execute_command('ip_feature_dump')

    def show_ip_interface_features(self):
        return self.execute_command('ip_interface_feature_dump')

    def ip_probe_neighbor(self, interface, address):
        return self.execute_command('ip_probe_neighbor', sw_if_index=interface, address=address)

    def ip_route(self, options):
        return self.execute_command('ip_route_add_del', options=options)

    def show_ip(self):
        return self.execute_command('ip_dump')

    def show_ip_fib(self):
        return self.execute_command('ip_fib_dump')

    def show_ip4(self):
        return self.execute_command('ip4_address_dump')

    def show_ip6(self):
        return self.execute_command('ip6_address_dump')

    def show_ip6_fib(self):
        return self.execute_command('ip6_fib_dump')

    def test_crash(self):
        return self.execute_command('test_crash')

# Example usage
if __name__ == "__main__":
    vpp_client_vnet = VPPClientVnet()

    # Example: Show Adjacency Alloc
    response, error = vpp_client_vnet.show_adjacency_alloc()
    if error:
        print("Show Adjacency Alloc Error:", error)
    else:
        print("Show Adjacency Alloc Output:", response)

    # Example: Test Crash
    response, error = vpp_client_vnet.test_crash()
    if error:
        print("Test Crash Error:", error)
    else:
        print("Test Crash Output:", response)

    # Add additional example usages as needed
