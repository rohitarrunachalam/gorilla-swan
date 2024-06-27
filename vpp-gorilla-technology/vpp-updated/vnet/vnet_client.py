import logging
from vpp_papi import VPPApiClient  # Replace with the actual import statement for VPP PAPI

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VNetClient:
    def __init__(self):
        self.vpp_api = VPPApiClient()  # Replace with the actual initialization for VPPApiClient
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        self.logger.debug(f"Running command: {command}")
        # Example assuming VPPApiClient.execute_command exists
        return self.vpp_api.execute_command(command)

    def set_interface_handoff(self, interface_name, workers_list):
        command = f'set interface handoff {interface_name} {" ".join(map(str, workers_list))}'
        return self.run_vpp_command(command)

    def clear_hardware_interfaces(self, brief=False, verbose=False, detail=False, bond=None, *interfaces):
        command = 'clear hardware-interfaces'
        if brief:
            command += ' brief'
        elif verbose:
            command += ' verbose'
        elif detail:
            command += ' detail'
        if bond:
            command += f' bond {bond}'
        if interfaces:
            command += f' {" ".join(interfaces)}'
        return self.run_vpp_command(command)

    # Define other methods similarly
