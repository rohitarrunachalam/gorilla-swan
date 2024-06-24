import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientVxlanGPE:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP VNET/VXLAN-GPE Commands
    def create_vxlan_gpe_tunnel(self, tunnel_id, src_ip, dst_ip, vni, encap_vrf_id):
        return self.execute_command(f"create vxlan-gpe tunnel {tunnel_id} src {src_ip} dst {dst_ip} vni {vni} encap-vrf-id {encap_vrf_id}")

    def show_vxlan_gpe(self):
        return self.execute_command("show vxlan-gpe")

# Example usage
if __name__ == "__main__":
    vpp_client_vxlan_gpe = VPPClientVxlanGPE()

    # Example: Create VXLAN-GPE Tunnel
    tunnel_id = 1
    src_ip = "192.168.1.1"
    dst_ip = "192.168.2.1"
    vni = 100
    encap_vrf_id = 0
    stdout, stderr = vpp_client_vxlan_gpe.create_vxlan_gpe_tunnel(tunnel_id, src_ip, dst_ip, vni, encap_vrf_id)
    print("Create VXLAN-GPE Tunnel Output:", stdout)
    print("Create VXLAN-GPE Tunnel Error:", stderr)

    # Example: Show VXLAN-GPE
    stdout, stderr = vpp_client_vxlan_gpe.show_vxlan_gpe()
    print("Show VXLAN-GPE Output:", stdout)
    print("Show VXLAN-GPE Error:", stderr)

    # Add additional example usages as needed for other commands

