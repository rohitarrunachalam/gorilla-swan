import logging
from command import VPPCommand

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class ClassifyClient:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Assuming VPPCommand is appropriately defined
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        self.logger.debug(f"Running command: {command}")
        return self.vpp_command.run_vpp_command(command)

    def set_interface_input_acl(self, interface_name, acl_index):
        command = f'set interface input acl intfc {interface_name} acl {acl_index}'
        return self.run_vpp_command(command)

    def show_inacl(self):
        command = 'show inacl'
        return self.run_vpp_command(command)

    def set_policer_classify(self, policer_name, table_index):
        command = f'set policer classify {policer_name} {table_index}'
        return self.run_vpp_command(command)

    def show_classify_policer(self):
        command = 'show classify policer'
        return self.run_vpp_command(command)

    def classify_session(self, table_index, match, hit_next_index, l2=None, miss_next_index=None):
        command = f'classify session table-index {table_index} match {match} hit-next-index {hit_next_index}'
        if l2:
            command += f' l2 {l2}'
        if miss_next_index:
            command += f' miss-next-index {miss_next_index}'
        return self.run_vpp_command(command)

    def classify_table(self, table_index, next_table_index=None, miss_next_index=None, skip_n=None, match_n=None, mask=None, delete=False):
        command = f'classify table table-index {table_index}'
        if next_table_index:
            command += f' next-table-index {next_table_index}'
        if miss_next_index:
            command += f' miss-next-index {miss_next_index}'
        if skip_n:
            command += f' skip_n {skip_n}'
        if match_n:
            command += f' match_n {match_n}'
        if mask:
            command += f' mask {mask}'
        if delete:
            command += ' delete'
        return self.run_vpp_command(command)

    def show_classify_tables(self):
        command = 'show classify tables'
        return self.run_vpp_command(command)

    def test_classify(self):
        command = 'test classify'
        return self.run_vpp_command(command)
