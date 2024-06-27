import logging
from vpp_papi import VPPApiClient

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class GreClient:
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

    def create_gre_tunnel(self, src_address, dst_address, outer_fib_id=None, session_id=None):
        params = {
            'src': src_address,
            'dst': dst_address
        }
        if outer_fib_id:
            params['outer_fib_id'] = outer_fib_id
        if session_id:
            params['session_id'] = session_id
        return self.run_vpp_command('gre_tunnel_add_del', is_add=1, **params)

    def show_gre_tunnel(self):
        return self.run_vpp_command('gre_tunnel_dump')


# Example usage
if __name__ == "__main__":
    gre_client = GreClient()

    # Example: Create GRE Tunnel
    response, error = gre_client.create_gre_tunnel('192.168.1.1', '192.168.1.2', outer_fib_id=0, session_id=1)
    if error:
        print(f"Error creating GRE tunnel: {error}")
    else:
        print(f"GRE tunnel created successfully: {response}")

    # Example: Show GRE Tunnels
    response, error = gre_client.show_gre_tunnel()
    if error:
        print(f"Error showing GRE tunnels: {error}")
    else:
        print(f"GRE tunnels: {response}")

    # Add additional example usages as needed
