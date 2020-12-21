import re
import subprocess

filename = 'docker-compose.yml'
docker_ip = subprocess.check_output("ip addr show docker0 | grep -Po 'inet \\K[\\d.]+'", shell=True).decode('utf8').replace('\n', '')

with open(filename, 'r') as file:
    data = file.read()

form_lines = []
for line in data.split('\n'):
    if 'KAFKA_ADVERTISED_HOST_NAME:' in line:
        line = re.sub(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', docker_ip, line)
    form_lines.append(line)

new_data = '\n'.join(form_lines)

with open(filename, 'w') as file:
    file.write(new_data)
