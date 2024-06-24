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

    def start_bgp(self, port=None, listenon=None, daemon=None, config_file=None, no_kernel=None):
        command = "bgpd"
        if port:
            command += f" -p {port}"
        if listenon:
            command += f" -l {listenon}"
        if daemon:
            command += " -d"
        if config_file:
            command += f" -f {config_file}"
        if no_kernel:
            command += " -n"
        return self.execute_command(command)

    def debug_bgp(self, command):
        return self.execute_command(f"debug {command}")

    def dump_bgp(self, command):
        return self.execute_command(f"dump {command}")

    def show_bgp(self, command):
        return self.execute_command(f"show {command}")

    def show_bgp_dampening(self, command):
        return self.execute_command(f"show {command}")

    def show_bgp_segment_routing(self):
        return self.execute_command("show bgp segment-routing srv6")

    def show_bgp_route_reflector(self):
        return self.execute_command("show bgp dampening flap-statistics")

    def show_bgp_statistics(self):
        return self.execute_command("show bgp statistics-all")

    def show_bgp_cidr_only(self):
        return self.execute_command("show ip bgp cidr-only")

    def show_bgp_neighbor_routes(self, command):
        return self.execute_command(f"show {command}")
    

    # OSPFv2 Commands
    def start_ospf(self, instance=None, vrf=None):
        command = "router ospf"
        if instance:
            command += f" {instance}"
        if vrf:
            command += f" vrf {vrf}"
        return self.execute_command(command)

    def set_ospf_router_id(self, router_id):
        return self.execute_command(f"ospf router-id {router_id}")

    def debug_ospf(self, command):
        return self.execute_command(f"debug ospf {command}")

    def show_ospf(self, command):
        return self.execute_command(f"show ip ospf {command}")

    def clear_ospf(self, command):
        return self.execute_command(f"clear ip ospf {command}")

    # OSPFv3 Commands
    def start_ospfv3(self):
        return self.execute_command("router ospf6")

    def set_ospfv3_router_id(self, router_id):
        return self.execute_command(f"ospf6 router-id {router_id}")

    def debug_ospfv3(self, command):
        return self.execute_command(f"debug ospf6 {command}")

    def show_ospfv3(self, command):
        return self.execute_command(f"show ipv6 ospf6 {command}")

    def clear_ospfv3(self, command):
        return self.execute_command(f"clear ipv6 ospf6 {command}")

