import logging
from command import VPPCommand

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class DpdkClient:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Assuming VPPCommand is appropriately defined
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        self.logger.debug(f"Running command: {command}")
        return self.vpp_command.run_vpp_command(command)

    def clear_efd(self):
        command = 'clear efd'
        return self.run_vpp_command(command)

    def pcap_tx_trace(self, state, max_packets=None, interface=None, file=None):
        command = f'pcap tx trace {state}'
        if max_packets:
            command += f' max-packets {max_packets}'
        if interface:
            command += f' intfc {interface}'
        if file:
            command += f' file {file}'
        return self.run_vpp_command(command)

    def set_dpdk_interface_descriptors(self, interface, n_rx_desc=None, n_tx_desc=None):
        command = f'set dpdk interface descriptors {interface}'
        if n_rx_desc:
            command += f' rx {n_rx_desc}'
        if n_tx_desc:
            command += f' tx {n_tx_desc}'
        return self.run_vpp_command(command)

    def set_dpdk_interface_placement(self, interface, workers):
        command = f'set dpdk interface placement {interface} workers {workers}'
        return self.run_vpp_command(command)

    def set_efd(self, mode, interface=None):
        command = f'set efd {mode}'
        if interface:
            command += f' {interface}'
        return self.run_vpp_command(command)

    def show_dpdk_buffer(self):
        command = 'show dpdk buffer'
        return self.run_vpp_command(command)

    def show_dpdk_interface_placement(self):
        command = 'show dpdk interface placement'
        return self.run_vpp_command(command)

    def show_efd(self):
        command = 'show efd'
        return self.run_vpp_command(command)

    def test_dpdk_buffer(self):
        command = 'test dpdk buffer'
        return self.run_vpp_command(command)

    def create_vhost_user(self, socket, server=None):
        command = f'create vhost-user socket {socket}'
        if server:
            command += f' server {server}'
        return self.run_vpp_command(command)

    def delete_vhost_user(self, socket):
        command = f'delete vhost-user socket {socket}'
        return self.run_vpp_command(command)

    def show_vhost_user(self):
        command = 'show vhost-user'
        return self.run_vpp_command(command)


