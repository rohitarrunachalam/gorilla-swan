import subprocess
import logging
from command import FRRCommand

# Configure logging
logging.basicConfig(filename='logs/frrpy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class FRRClientRouting:
    def __init__(self):
        pass

    def run_vtysh_command(self, command):
        try:
            logging.info(f"Running command: {command}")
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            stdout = result.stdout.decode('utf-8')
            stderr = result.stderr.decode('utf-8')
            if stderr:
                logging.error(f"Error executing command: {stderr}")
            return stdout, stderr
        except subprocess.CalledProcessError as e:
            logging.error(f"Command '{command}' failed with error: {e.stderr}")
            return "", str(e)
        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            return "", str(e)

    def execute_command(self, command):
        frr_command = FRRCommand()
        full_command = f'vtysh -c "{command}"'
        return frr_command.run_vtysh_command(full_command)

        # BGP Commands
    def get_bgp_summary(self):
        return self.execute_command("show ip bgp summary")

    def get_bgp_neighbors(self):
        return self.execute_command("show ip bgp neighbors")

    def add_bgp_neighbor(self, as_number, neighbor_address, peer_as):
        return self.execute_command(f"configure terminal ; router bgp {as_number} ; neighbor {neighbor_address} remote-as {peer_as}")

    def remove_bgp_neighbor(self, as_number, neighbor_address):
        return self.execute_command(f"configure terminal ; router bgp {as_number} ; no neighbor {neighbor_address}")

    # OSPF Commands
    def get_ospf_neighbors(self):
        return self.execute_command("show ip ospf neighbor")

    def get_ospf_database(self):
        return self.execute_command("show ip ospf database")

    def add_ospf_network(self, network, area):
        return self.execute_command(f"configure terminal ; router ospf ; network {network} area {area}")

    def remove_ospf_network(self, network):
        return self.execute_command(f"configure terminal ; router ospf ; no network {network}")

    # Static Routes
    def add_static_route(self, destination, gateway):
        return self.execute_command(f"configure terminal ; ip route {destination} {gateway}")

    def remove_static_route(self, destination):
        return self.execute_command(f"configure terminal ; no ip route {destination}")

    # Additional commands can be added as needed
