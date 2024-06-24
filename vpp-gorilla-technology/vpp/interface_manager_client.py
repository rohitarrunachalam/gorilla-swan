import logging
from command import VPPCommand

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class InterfaceManagerClient:
    def __init__(self):
        self.vpp_command = VPPCommand()
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        return self.vpp_command.run_vpp_command(command)

    ### Proxy ARP Commands ###

    def set_interface_proxy_arp(self, interface, enable=True):
        enable_str = 'enable' if enable else 'disable'
        command = f'set interface proxy-arp {interface} {enable_str}'
        return self.run_vpp_command(command)

    def set_ip_arp(self, interface, ip_address, mac_address, static=False):
        static_str = 'static' if static else ''
        command = f'set ip arp {interface} {ip_address} {mac_address} {static_str}'
        return self.run_vpp_command(command)

    def show_ip_arp(self):
        command = 'show ip arp'
        return self.run_vpp_command(command)

    ### Loopback Interface Commands ###

    def create_loopback_interface(self, mac_address=None):
        if mac_address:
            command = f'create loopback interface mac {mac_address}'
        else:
            command = 'create loopback interface'
        return self.run_vpp_command(command)

    def delete_loopback_interface(self, interface):
        command = f'delete loopback interface intfc {interface}'
        return self.run_vpp_command(command)

    def create_loopback_interface_alt(self, mac_address=None):
        if mac_address:
            command = f'loopback create-interface mac {mac_address}'
        else:
            command = 'loopback create-interface'
        return self.run_vpp_command(command)

    def delete_loopback_interface_alt(self, interface):
        command = f'loopback delete-interface intfc {interface}'
        return self.run_vpp_command(command)
