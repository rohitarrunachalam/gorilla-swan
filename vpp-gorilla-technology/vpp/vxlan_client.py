import logging
from command import VPPCommand

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VxlanClient:
    def __init__(self):
        self.vpp_command = VPPCommand()
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        return self.vpp_command.run_vpp_command(command)

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
