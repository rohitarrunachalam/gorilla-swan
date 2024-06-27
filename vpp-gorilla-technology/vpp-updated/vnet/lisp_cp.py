import logging
from vpp_papi import VPPApiClient  # Ensure VPPApiClient is imported correctly

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientLISPCP:
    def __init__(self):
        self.vpp = VPPApiClient()
        self.vpp.connect('vpp_api_client')
        self.logger = logging.getLogger(__name__)

    def execute_command(self, api_method, **params):
        self.logger.debug(f"Running API method: {api_method} with parameters {params}")
        try:
            response = getattr(self.vpp.api, api_method)(**params)
            return response, None
        except AttributeError:
            error_msg = f"API method '{api_method}' not available in VPP API"
            self.logger.error(error_msg)
            return None, error_msg
        except Exception as e:
            self.logger.error(f"Error executing API method {api_method}: {e}")
            return None, str(e)

    # VPP VNET/LISP-CP Commands (replace with actual VPP API method names)
    def lisp(self):
        return self.execute_command("lisp")

    def lisp_adjacency(self):
        return self.execute_command("lisp_adjacency")

    def lisp_eid_table(self):
        return self.execute_command("lisp_eid_table")

    def lisp_eid_table_map(self):
        return self.execute_command("lisp_eid_table_map")

    def lisp_locator(self):
        return self.execute_command("lisp_locator")

    def lisp_locator_set(self):
        return self.execute_command("lisp_locator_set")

    def lisp_map_request_itr_rlocs(self):
        return self.execute_command("lisp_map_request_itr_rlocs")

    def lisp_map_resolver(self):
        return self.execute_command("lisp_map_resolver")

    def lisp_pitr(self):
        return self.execute_command("lisp_pitr")

    def lisp_remote_mapping(self):
        return self.execute_command("lisp_remote_mapping")

    def show_lisp_eid_table(self):
        return self.execute_command("show_lisp_eid_table")

    def show_lisp_eid_table_map(self):
        return self.execute_command("show_lisp_eid_table_map")

    def show_lisp_locator_set(self):
        return self.execute_command("show_lisp_locator_set")

    def show_lisp_map_request_itr_rlocs(self):
        return self.execute_command("show_lisp_map_request_itr_rlocs")

    def show_lisp_map_resolvers(self):
        return self.execute_command("show_lisp_map_resolvers")

    def show_lisp_pitr(self):
        return self.execute_command("show_lisp_pitr")

    def show_lisp_status(self):
        return self.execute_command("show_lisp_status")

# Example usage
if __name__ == "__main__":
    vpp_client_lisp_cp = VPPClientLISPCP()

    # Example: Show LISP Status
    response, error = vpp_client_lisp_cp.show_lisp_status()
    if error:
        print("Show LISP Status Error:", error)
    else:
        print("Show LISP Status Output:", response)

    # Add additional example usages as needed for other commands
