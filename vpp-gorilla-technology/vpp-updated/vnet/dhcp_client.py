import logging
from vpp_papi import VPPApiClient

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class DhcpClient:
    def __init__(self):
        self.vpp = VPPApiClient()
        self.vpp.connect('vpp_api_client')
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command, **kwargs):
        self.logger.debug(f"Running command: {command} with arguments {kwargs}")
        try:
            response = getattr(self.vpp.api, command)(**kwargs)
            return response, None
        except AttributeError:
            error_msg = f"Command '{command}' not available in VPP API"
            self.logger.error(error_msg)
            return None, error_msg
        except Exception as e:
            self.logger.error(f"Error executing command {command}: {e}")
            return None, str(e)

    def set_dhcp_client(self, interface_name):
        return self.run_vpp_command('dhcp_client_config', interface_name=interface_name, enable=True)

    def show_dhcp_client(self):
        return self.run_vpp_command('dhcp_client_dump')

    def set_dhcp_option_82_vss(self):
        return self.run_vpp_command('dhcp_proxy_set_vss')

    def set_dhcp_proxy(self):
        return self.run_vpp_command('dhcp_proxy_config', enable=True)

    def show_dhcp_option_82_address_interface(self):
        return self.run_vpp_command('dhcp_option_82_address_dump')

    def show_dhcp_proxy(self):
        return self.run_vpp_command('dhcp_proxy_dump')

    def show_dhcp_vss(self):
        return self.run_vpp_command('dhcp_vss_dump')


class Dhcpv6Client:
    def __init__(self):
        self.vpp = VPPApiClient()
        self.vpp.connect('vpp_api_client')
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command, **kwargs):
        self.logger.debug(f"Running command: {command} with arguments {kwargs}")
        try:
            response = getattr(self.vpp.api, command)(**kwargs)
            return response, None
        except AttributeError:
            error_msg = f"Command '{command}' not available in VPP API"
            self.logger.error(error_msg)
            return None, error_msg
        except Exception as e:
            self.logger.error(f"Error executing command {command}: {e}")
            return None, str(e)

    def set_dhcpv6_proxy(self, interface_name):
        return self.run_vpp_command('dhcpv6_proxy_config', interface_name=interface_name, enable=True)

    def set_dhcpv6_vss(self, interface_name, enable=True):
        return self.run_vpp_command('dhcpv6_vss_config', interface_name=interface_name, enable=enable)

    def show_dhcpv6_link_address_interface(self):
        return self.run_vpp_command('dhcpv6_link_address_dump')

    def show_dhcpv6_proxy(self):
        return self.run_vpp_command('dhcpv6_proxy_dump')

    def show_dhcpv6_vss(self):
        return self.run_vpp_command('dhcpv6_vss_dump')


# Example usage
if __name__ == "__main__":
    dhcp_client = DhcpClient()
    dhcpv6_client = Dhcpv6Client()

    # Example: Set DHCP Client
    response, error = dhcp_client.set_dhcp_client('eth0')
    if error:
        print(f"Error setting DHCP client: {error}")
    else:
        print(f"DHCP client set successfully: {response}")

    # Add additional example usages as needed
