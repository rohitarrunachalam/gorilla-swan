import logging
from command import VPPCommand

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class FlowClient:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Assuming VPPCommand is appropriately defined
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        self.logger.debug(f"Running command: {command}")
        return self.vpp_command.run_vpp_command(command)

    def set_ipfix(self, collector_ip, collector_port, src_ip=None, vrf_id=None, path_mtu=None):
        command = f'set ipfix collector {collector_ip} port {collector_port}'
        if src_ip:
            command += f' src-ip {src_ip}'
        if vrf_id:
            command += f' vrf-id {vrf_id}'
        if path_mtu:
            command += f' path-mtu {path_mtu}'
        return self.run_vpp_command(command)

    def flow_classify(self, flow_name, match_criteria, action):
        command = f'flow classify {flow_name} match {match_criteria} action {action}'
        return self.run_vpp_command(command)

