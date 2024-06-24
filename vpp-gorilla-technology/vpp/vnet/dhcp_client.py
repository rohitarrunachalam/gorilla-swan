import logging
from command import VPPCommand

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class DhcpClient:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Assuming VPPCommand is appropriately defined
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        self.logger.debug(f"Running command: {command}")
        return self.vpp_command.run_vpp_command(command)

    def set_dhcp_client(self, interface_name):
        command = f'set dhcp client {interface_name}'
        return self.run_vpp_command(command)

    def show_dhcp_client(self):
        command = 'show dhcp client'
        return self.run_vpp_command(command)

    def set_dhcp_option_82_vss(self):
        command = 'set dhcp option-82 vss'
        return self.run_vpp_command(command)

    def set_dhcp_proxy(self):
        command = 'set dhcp proxy'
        return self.run_vpp_command(command)

    def show_dhcp_option_82_address_interface(self):
        command = 'show dhcp option-82-address interface'
        return self.run_vpp_command(command)

    def show_dhcp_proxy(self):
        command = 'show dhcp proxy'
        return self.run_vpp_command(command)

    def show_dhcp_vss(self):
        command = 'show dhcp vss'
        return self.run_vpp_command(command)


class Dhcpv6Client:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Assuming VPPCommand is appropriately defined
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        self.logger.debug(f"Running command: {command}")
        return self.vpp_command.run_vpp_command(command)

    def set_dhcpv6_proxy(self, interface_name):
        command = f'set dhcpv6 proxy {interface_name}'
        return self.run_vpp_command(command)

    def set_dhcpv6_vss(self, interface_name, enable=True):
        command = f'set dhcpv6 vss {interface_name}'
        if not enable:
            command += ' disable'
        return self.run_vpp_command(command)

    def show_dhcpv6_link_address_interface(self):
        command = 'show dhcpv6 link-address interface'
        return self.run_vpp_command(command)

    def show_dhcpv6_proxy(self):
        command = 'show dhcpv6 proxy'
        return self.run_vpp_command(command)

    def show_dhcpv6_vss(self):
        command = 'show dhcpv6 vss'
        return self.run_vpp_command(command)

