import logging
from command import VPPCommand
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class VNetClient:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Assuming VPPCommand is appropriately defined
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        return self.vpp_command.run_vpp_command(command)

    def set_interface_handoff(self, interface_name, workers_list):
        command = f'set interface handoff {interface_name} {" ".join(workers_list)}'
        return self.run_vpp_command(command)

    def clear_hardware_interfaces(self, brief=False, verbose=False, detail=False, bond=None, *interfaces):
        command = 'clear hardware-interfaces'
        if brief:
            command += ' brief'
        elif verbose:
            command += ' verbose'
        elif detail:
            command += ' detail'
        if bond:
            command += f' bond {bond}'
        if interfaces:
            command += f' {" ".join(interfaces)}'
        return self.run_vpp_command(command)

    def clear_interfaces(self):
        command = 'clear interfaces'
        return self.run_vpp_command(command)

    def create_sub_interfaces(self, interface_name, sub_interface_range, *options):
        command = f'create sub-interfaces {interface_name} {sub_interface_range}'
        if options:
            command += f' {" ".join(options)}'
        return self.run_vpp_command(command)

    def interface_commands(self):
        command = 'interface'
        return self.run_vpp_command(command)

    def renumber_interface(self, interface_name, new_dev_instance):
        command = f'renumber interface {interface_name} {new_dev_instance}'
        return self.run_vpp_command(command)

    def set_interface(self, interface_name, *options):
        command = f'set interface {interface_name}'
        if options:
            command += f' {" ".join(options)}'
        return self.run_vpp_command(command)

    def set_interface_hw_class(self, interface_name, hardware_class):
        command = f'set interface hw-class {interface_name} {hardware_class}'
        return self.run_vpp_command(command)

    def set_interface_mtu(self, value, interface_name):
        command = f'set interface mtu {value} {interface_name}'
        return self.run_vpp_command(command)

    def set_interface_promiscuous(self, state, interface_name):
        command = f'set interface promiscuous {state} {interface_name}'
        return self.run_vpp_command(command)

    def set_interface_state(self, interface_name, state):
        command = f'set interface state {interface_name} {state}'
        return self.run_vpp_command(command)

    def set_interface_unnumbered(self, interface_name, use_interface=None, delete_interface=None):
        command = f'set interface unnumbered {interface_name}'
        if use_interface:
            command += f' use {use_interface}'
        if delete_interface:
            command += f' delete {delete_interface}'
        return self.run_vpp_command(command)

    def show_hardware_interfaces(self, mode=None, *interfaces):
        command = 'show hardware-interfaces'
        if mode:
            command += f' {mode}'
        if interfaces:
            command += f' {" ".join(interfaces)}'
        return self.run_vpp_command(command)

    def show_interfaces(self, mode=None, *interfaces):
        command = 'show interfaces'
        if mode:
            command += f' {mode}'
        if interfaces:
            command += f' {" ".join(interfaces)}'
        return self.run_vpp_command(command)

    def pcap_drop_trace(self, state, max_packets, interface_name, file_name, status):
        command = f'pcap drop trace {state} {max_packets} {interface_name} {file_name} {status}'
        return self.run_vpp_command(command)
