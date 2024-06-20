import logging
from command import VPPCommand
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')




class IoamClient:
    def __init__(self):
        self.vpp_command = VPPCommand()
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        return self.vpp_command.run_vpp_command(command)

    def show_ioam_pot_statistics(self):
        command = 'show ioam pot'
        return self.run_vpp_command(command)

    def clear_pot_profile(self, index=None):
        if index is not None:
            command = f'clear pot profile {index}'
        else:
            command = 'clear pot profile all'
        return self.run_vpp_command(command)

    def set_pot_profile(self, name, id, validator_key=None, prime_number=None, secret_share=None, lpc=None, polynomial2=None, bits_in_random=None):
        command = f'set pot profile name {name} id {id}'
        if validator_key:
            command += f' validator-key {validator_key}'
        if prime_number:
            command += f' prime-number {prime_number}'
        if secret_share:
            command += f' secret_share {secret_share}'
        if lpc:
            command += f' lpc {lpc}'
        if polynomial2:
            command += f' polynomial2 {polynomial2}'
        if bits_in_random:
            command += f' bits-in-random {bits_in_random}'
        return self.run_vpp_command(command)

    def set_pot_profile_active(self, name, id):
        command = f'set pot profile-active name {name} id {id}'
        return self.run_vpp_command(command)

    def show_pot_profile(self):
        command = 'show pot profile'
        return self.run_vpp_command(command)
