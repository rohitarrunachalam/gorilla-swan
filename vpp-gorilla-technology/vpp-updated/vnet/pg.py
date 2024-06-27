import logging
from vpp_papi import VPPApiClient  # Ensure VPPApiClient is imported correctly

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientPG:
    def __init__(self):
        self.vpp = VPPApiClient()
        self.vpp.connect('vpp_api_client')
        self.logger = logging.getLogger(__name__)

    def execute_command(self, api_method, **params):
        self.logger.debug(f"Running API method: {api_method} with parameters {params}")
        try:
            response = getattr(self.vpp.api, api_method)(**params)
            return response, None
        except AttributeError:
            error_msg = f"API method '{api_method}' not available in VPP API"
            self.logger.error(error_msg)
            return None, error_msg
        except Exception as e:
            self.logger.error(f"Error executing API method {api_method}: {e}")
            return None, str(e)

    # VPP VNET/PG Commands
    def create_packet_generator(self):
        return self.execute_command("pg_create")

    def packet_generator(self):
        return self.execute_command("pg")

    def packet_generator_capture(self):
        return self.execute_command("pg_capture")

    def packet_generator_configure(self):
        return self.execute_command("pg_configure")

    def packet_generator_delete(self):
        return self.execute_command("pg_delete")

    def packet_generator_disable_stream(self):
        return self.execute_command("pg_disable_stream")

    def packet_generator_enable_stream(self):
        return self.execute_command("pg_enable_stream")

    def packet_generator_new(self):
        return self.execute_command("pg_new")

    def show_packet_generator(self):
        return self.execute_command("show_pg")

# Example usage
if __name__ == "__main__":
    vpp_client_pg = VPPClientPG()

    # Example: Show Packet Generator
    response, error = vpp_client_pg.show_packet_generator()
    if error:
        print("Show Packet Generator Error:", error)
    else:
        print("Show Packet Generator Output:", response)

    # Add additional example usages as needed for other commands
