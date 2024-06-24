import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientLISPCP:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP VNET/LISP-CP Commands
    def lisp(self):
        return self.execute_command("lisp")

    def lisp_adjacency(self):
        return self.execute_command("lisp adjacency")

    def lisp_eid_table(self):
        return self.execute_command("lisp eid-table")

    def lisp_eid_table_map(self):
        return self.execute_command("lisp eid-table map")

    def lisp_locator(self):
        return self.execute_command("lisp locator")

    def lisp_locator_set(self):
        return self.execute_command("lisp locator-set")

    def lisp_map_request_itr_rlocs(self):
        return self.execute_command("lisp map-request itr-rlocs")

    def lisp_map_resolver(self):
        return self.execute_command("lisp map-resolver")

    def lisp_pitr(self):
        return self.execute_command("lisp pitr")

    def lisp_remote_mapping(self):
        return self.execute_command("lisp remote-mapping")

    def show_lisp_eid_table(self):
        return self.execute_command("show lisp eid-table")

    def show_lisp_eid_table_map(self):
        return self.execute_command("show lisp eid-table map")

    def show_lisp_locator_set(self):
        return self.execute_command("show lisp locator-set")

    def show_lisp_map_request_itr_rlocs(self):
        return self.execute_command("show lisp map-request itr-rlocs")

    def show_lisp_map_resolvers(self):
        return self.execute_command("show lisp map-resolvers")

    def show_lisp_pitr(self):
        return self.execute_command("show lisp pitr")

    def show_lisp_status(self):
        return self.execute_command("show lisp status")

# Example usage
if __name__ == "__main__":
    vpp_client_lisp_cp = VPPClientLISPCP()

    # Example: Show LISP Status
    stdout, stderr = vpp_client_lisp_cp.show_lisp_status()
    print("Show LISP Status Output:", stdout)
    print("Show LISP Status Error:", stderr)

    # Add additional example usages as needed for other commands
