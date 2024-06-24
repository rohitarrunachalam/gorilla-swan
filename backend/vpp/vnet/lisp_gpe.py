import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientLISPGPE:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP VNET/LISP-GPE Commands
    def lisp_gpe_iface(self):
        return self.execute_command("lisp gpe iface")

    def lisp_gpe(self):
        return self.execute_command("lisp gpe")

    def lisp_gpe_tunnel(self):
        return self.execute_command("lisp gpe tunnel")

    def show_lisp_gpe_interface(self):
        return self.execute_command("show lisp gpe interface")

    def show_lisp_gpe_tunnel(self):
        return self.execute_command("show lisp gpe tunnel")

# Example usage
if __name__ == "__main__":
    vpp_client_lisp_gpe = VPPClientLISPGPE()

    # Example: Show LISP GPE Tunnel
    stdout, stderr = vpp_client_lisp_gpe.show_lisp_gpe_tunnel()
    print("Show LISP GPE Tunnel Output:", stdout)
    print("Show LISP GPE Tunnel Error:", stderr)

    # Add additional example usages as needed for other commands
