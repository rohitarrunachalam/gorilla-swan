import logging
from vpp_papi import VPPApiClient

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class ClassifyClient:
    def __init__(self):
        self.vpp = VPPApiClient()
        self.vpp.connect('vpp_api_client')
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command, **kwargs):
        self.logger.debug(f"Running command: {command} with arguments {kwargs}")
        try:
            response = getattr(self.vpp.api, command)(**kwargs)
            return response, None
        except AttributeError:
            error_msg = f"Command '{command}' not available in VPP API"
            self.logger.error(error_msg)
            return None, error_msg
        except Exception as e:
            self.logger.error(f"Error executing command {command}: {e}")
            return None, str(e)

    def set_interface_input_acl(self, interface_name, acl_index):
        return self.run_vpp_command('acl_interface_set_acl', sw_if_index=interface_name, acl_index=acl_index)

    def show_inacl(self):
        return self.run_vpp_command('acl_dump')

    def set_policer_classify(self, policer_name, table_index):
        return self.run_vpp_command('classify_policer_add_del', name=policer_name, policer_index=table_index)

    def show_classify_policer(self):
        return self.run_vpp_command('classify_policer_dump')

    def classify_session(self, table_index, match, hit_next_index, l2=None, miss_next_index=None):
        params = {
            'is_add': True,
            'table_index': table_index,
            'hit_next_index': hit_next_index,
            'opaque_index': match,
        }
        if l2:
            params['l2'] = l2
        if miss_next_index:
            params['miss_next_index'] = miss_next_index
        return self.run_vpp_command('classify_add_del_session', **params)

    def classify_table(self, table_index, next_table_index=None, miss_next_index=None, skip_n=None, match_n=None, mask=None, delete=False):
        params = {
            'is_add': not delete,
            'table_index': table_index,
        }
        if next_table_index:
            params['next_table_index'] = next_table_index
        if miss_next_index:
            params['miss_next_index'] = miss_next_index
        if skip_n:
            params['skip_n'] = skip_n
        if match_n:
            params['match_n'] = match_n
        if mask:
            params['match_n_mask'] = mask
        return self.run_vpp_command('classify_add_del_table', **params)

    def show_classify_tables(self):
        return self.run_vpp_command('classify_table_ids')

    def test_classify(self):
        return self.run_vpp_command('test_classify')


# Example usage
if __name__ == "__main__":
    classify_client = ClassifyClient()

    # Example: Set Interface Input ACL
    response, error = classify_client.set_interface_input_acl(interface_name=1, acl_index=5)
    if error:
        print(f"Error setting interface input ACL: {error}")
    else:
        print(f"Interface input ACL set successfully: {response}")

    # Add additional example usages as needed
