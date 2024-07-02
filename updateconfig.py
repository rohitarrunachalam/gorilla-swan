from flask import Flask, request, jsonify
import subprocess
import difflib
import os
import datetime
import traceback

app = Flask(__name__)

@app.route('/update-config', methods=['POST'])
def update_config():
    # Check if a file was uploaded in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']

    # Check if the file name is empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Read the file content
    new_config = file.read().decode('utf-8')

    # Handle the update with the new configuration file content
    differences = handle_update(new_config)
    
    return jsonify({'differences': differences}), 200

def save_current_config():
    result = subprocess.run(['sudo', 'cat', '/etc/nginx/nginx.conf'], stdout=subprocess.PIPE, text=True)
    current_config = result.stdout
    return current_config

def backup_current_config(current_config):
    backup_dir = './nginx_backup'
    try:
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        backup_path = os.path.join(backup_dir, f'nginx.conf.backup.{timestamp}')
        
        with open(backup_path, 'w') as backup_file:
            backup_file.write(current_config)
        
        print(f"Backup saved successfully: {backup_path}")
        
    except Exception as e:
        print(f"Error saving backup: {e}")
        traceback.print_exc() 

def update_nginx_config(new_config):
    with open('/tmp/nginx.conf', 'w') as file:
        file.write(new_config)
    subprocess.run(['sudo', 'cp', '/tmp/nginx.conf', '/etc/nginx/nginx.conf'])
    subprocess.run(['sudo', 'systemctl', 'reload', 'nginx'])

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

def compare_configs(old_config, new_config):
    diff = difflib.unified_diff(old_config.splitlines(), new_config.splitlines(), lineterm='')
    return list(diff)

def handle_update(new_config):
    current_config = save_current_config()
    backup_current_config(current_config)
    update_nginx_config(new_config)
    differences = compare_configs(current_config, new_config)
    formatted_diff = format_diff(differences)
    return formatted_diff

if __name__ == '__main__':
    app.run(debug=True)
