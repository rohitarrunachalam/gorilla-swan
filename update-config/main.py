from flask import Flask, request, jsonify
import subprocess
import difflib
import os
import datetime
import traceback

app = Flask(__name__)

# The Nginx Part is purely for testing purposes but everything should work fine for FRR and VPP.


# Generic function to save current configuration for a given service
def save_current_config(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True, shell=True)
    current_config = result.stdout
    return current_config

# Generic function to backup current configuration
def backup_current_config(service_name, current_config):
    backup_dir = f'./{service_name}_backup'
    try:
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        backup_path = os.path.join(backup_dir, f'{service_name}.conf.backup.{timestamp}')
        
        with open(backup_path, 'w') as backup_file:
            backup_file.write(current_config)
        
        print(f"Backup saved successfully: {backup_path}")
        
    except Exception as e:
        print(f"Error saving backup: {e}")
        traceback.print_exc() 

# Generic function to update configuration
def update_config_file(service_name, new_config, temp_path, config_path, reload_command):
    with open(temp_path, 'w') as file:
        file.write(new_config)
    subprocess.run(['sudo', 'cp', temp_path, config_path])
    subprocess.run(reload_command, shell=True)

# Format the differences
def format_diff(differences):
    formatted_diff = []
    line_number = 1  # Starting line number
    for line in differences:
        if line.startswith('--- ') or line.startswith('+++ ') or line.startswith('@@ '):
            formatted_diff.append(line)
        elif line.startswith('-'):
            formatted_diff.append(f'Removed: {line[1:]} \t(Line {line_number})')
        elif line.startswith('+'):
            formatted_diff.append(f'Added: {line[1:]} \t(Line {line_number})')
        else:
            formatted_diff.append(f'Unchanged: {line} \t(Line {line_number})')
        line_number += 1
    return formatted_diff

# Compare configurations
def compare_configs(old_config, new_config):
    diff = difflib.unified_diff(old_config.splitlines(), new_config.splitlines(), lineterm='')
    return list(diff)

# Handle update process
def handle_update(service_name, new_config, save_command, config_path, reload_command):
    current_config = save_current_config(save_command)
    backup_current_config(service_name, current_config)
    temp_path = f'/tmp/{service_name}.conf'
    update_config_file(service_name, new_config, temp_path, config_path, reload_command)
    differences = compare_configs(current_config, new_config)
    formatted_diff = format_diff(differences)
    return formatted_diff

@app.route('/update-config/<service_name>', methods=['POST'])
def update_config(service_name):
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    new_config = file.read().decode('utf-8')

    if service_name == 'nginx':
        save_command = 'sudo cat /etc/nginx/nginx.conf'
        config_path = '/etc/nginx/nginx.conf'
        reload_command = 'sudo systemctl reload nginx'
    elif service_name == 'frr':
        save_command = 'sudo vtysh -c "show running-config"'
        config_path = '/etc/frr/frr.conf'
        reload_command = 'sudo systemctl reload frr'
    elif service_name == 'vpp':
        save_command = 'sudo cat /etc/vpp/startup.conf'
        config_path = '/etc/vpp/startup.conf'
        reload_command = 'sudo systemctl reload vpp'
    else:
        return jsonify({'error': 'Unsupported service'}), 400

    differences = handle_update(service_name, new_config, save_command, config_path, reload_command)
    
    return jsonify({'differences': differences}), 200

if __name__ == '__main__':
    app.run(debug=True)
