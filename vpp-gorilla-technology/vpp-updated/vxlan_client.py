import logging
from vpp_papi import VPPApiClient  # Replace with actual import statement for VPP PAPI

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VxlanClient:
    def __init__(self):
        self.vpp_api = VPPApiClient()  # Replace with actual initialization of VPP PAPI client
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        self.logger.debug(f"Running command: {command}")
        # Example assuming vpp_api.execute_command exists in VPP PAPI
        return self.vpp_api.execute_command(command)

    def create_vxlan_tunnel(self, src_addr, dst_addr, vni, encap_vrf_id=None, decap_next=None, delete=False):
        command = f'create vxlan tunnel src {src_addr} dst {dst_addr} vni {vni}'
        
        if encap_vrf_id is not None:
            command += f' encap-vrf-id {encap_vrf_id}'
        
        if decap_next is not None:
            command += f' decap-next {decap_next}'
        
        if delete:
            command += ' del'
        
        return self.run_vpp_command(command)

    def show_vxlan_tunnel(self):
        command = 'show vxlan tunnel'
        return self.run_vpp_command(command)

# Example usage
if __name__ == "__main__":
    vxlan_client = VxlanClient()

    # Example: Create VXLAN Tunnel
    src_addr = "192.168.1.1"
    dst_addr = "192.168.2.1"
    vni = 100
    encap_vrf_id = 0
    decap_next = 1
    stdout, stderr = vxlan_client.create_vxlan_tunnel(src_addr, dst_addr, vni, encap_vrf_id, decap_next)
    print("Create VXLAN Tunnel Output:", stdout)
    print("Create VXLAN Tunnel Error:", stderr)

    # Example: Show VXLAN Tunnel
    stdout, stderr = vxlan_client.show_vxlan_tunnel()
    print("Show VXLAN Tunnel Output:", stdout)
    print("Show VXLAN Tunnel Error:", stderr)

    # Add additional example usages as needed
