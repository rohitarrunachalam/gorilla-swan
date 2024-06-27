import logging
from vpp_papi import VPPApiClient

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class DpdkClient:
    def __init__(self):
        self.vpp = VPPApiClient()
        self.vpp.connect('vpp_api_client')
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command, **params):
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

    def clear_efd(self):
        return self.run_vpp_command('clear_efd')

    def pcap_tx_trace(self, state, max_packets=None, interface=None, file=None):
        params = {'state': state}
        if max_packets:
            params['max_packets'] = max_packets
        if interface:
            params['interface'] = interface
        if file:
            params['file'] = file
        return self.run_vpp_command('pcap_tx_trace', **params)

    def set_dpdk_interface_descriptors(self, interface, n_rx_desc=None, n_tx_desc=None):
        params = {'interface': interface}
        if n_rx_desc:
            params['n_rx_desc'] = n_rx_desc
        if n_tx_desc:
            params['n_tx_desc'] = n_tx_desc
        return self.run_vpp_command('set_dpdk_interface_descriptors', **params)

    def set_dpdk_interface_placement(self, interface, workers):
        params = {'interface': interface, 'workers': workers}
        return self.run_vpp_command('set_dpdk_interface_placement', **params)

    def set_efd(self, mode, interface=None):
        params = {'mode': mode}
        if interface:
            params['interface'] = interface
        return self.run_vpp_command('set_efd', **params)

    def show_dpdk_buffer(self):
        return self.run_vpp_command('show_dpdk_buffer')

    def show_dpdk_interface_placement(self):
        return self.run_vpp_command('show_dpdk_interface_placement')

    def show_efd(self):
        return self.run_vpp_command('show_efd')

    def test_dpdk_buffer(self):
        return self.run_vpp_command('test_dpdk_buffer')

    def create_vhost_user(self, socket, server=None):
        params = {'socket': socket}
        if server:
            params['server'] = server
        return self.run_vpp_command('create_vhost_user', **params)

    def delete_vhost_user(self, socket):
        params = {'socket': socket}
        return self.run_vpp_command('delete_vhost_user', **params)

    def show_vhost_user(self):
        return self.run_vpp_command('show_vhost_user')


# Example usage
if __name__ == "__main__":
    dpdk_client = DpdkClient()

    # Example: Show DPDK buffer
    response, error = dpdk_client.show_dpdk_buffer()
    if error:
        print(f"Error showing DPDK buffer: {error}")
    else:
        print(f"DPDK buffer details: {response}")

    # Example: Enable pcap tx trace
    response, error = dpdk_client.pcap_tx_trace(state='enable')
    if error:
        print(f"Error enabling pcap tx trace: {error}")
    else:
        print(f"Pcap tx trace enabled successfully: {response}")

    # Add additional example usages as needed
