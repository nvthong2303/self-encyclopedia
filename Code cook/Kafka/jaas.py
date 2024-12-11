import re
import subprocess
from tempfile import NamedTemporaryFile


def create_jaas_file(users, file_path):
    config_content = 'KafkaServer {\n'
    config_content += '   org.apache.kafka.common.security.plain.PlainLoginModule required\n'
    config_content += '   username="admin"\n'
    config_content += '   password="admin-password"\n'

    for i, (user, password) in enumerate(users):
        config_content += f'   user_{user}="{password}"\n'

    config_content += '	;\n'
    config_content += '};\n'

    with open("/tmp/jaas.config", 'w') as tmp_file:
        tmp_file.write(config_content)

    subprocess.run(["sudo", "mv", "/tmp/jaas.config", file_path])


def read_file(file_path):
    result = subprocess.run(["sudo", "cat", file_path], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Failed to read file {file_path}: {result.stderr}")
    return result.stdout.splitlines()


def write_file(lines, file_path):
    with NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.writelines(line + "\n" for line in lines)
        temp_path = temp_file.name
    subprocess.run(["sudo", "mv", temp_path, file_path], check=True)


def add_user_sasl(user, password, file_path):
    lines = read_file(file_path)

    for line in lines:
        if f'user_{user}="' in line:
            print(f"User {user} already exists.")
            return

    lines.insert(-2, f'   user_{user}="{password}"')

    lines = [line for line in lines if line.strip() != ""]

    write_file(lines, file_path)
    print(f"User {user} added.")
    return


def remove_user_sasl(user, file_path):
    lines = read_file(file_path)

    lines = [line for line in lines if not re.match(f'^\s*user_{user}=".*"$', line)]

    write_file(lines, file_path)
    print(f"User {user} removed.")
    return


def get_list_user_sasl(file_path):
    try:
        lines = read_file(file_path)
        content = "\n".join(lines)

        user_pattern = r'user_([\w\d]+)="([^"]+)"'
        users = re.findall(user_pattern, content)

        result = [user for user, _ in users if user != 'admin']

        return result
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        return []


def parse_jaas_users(file_path):
    try:
        lines = read_file(file_path)
        content = "\n".join(lines)

        user_pattern = r'user_([\w\d]+)="([^"]+)"'
        users = re.findall(user_pattern, content)

        result = [user for user, _ in users if user != 'admin']

        return result

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        return []


users = [
    ("admin", "admin-password"),
    ("user1", "user1-secret"),
    ("user2", "user2-secret"),
    ("alice", "alice-secret")
]

# create_jaas_file(users, '/etc/kafka/config/kafka_jaas.conf')

add_user_sasl("bob1", "password-bob", '/etc/kafka/config/kafka_jaas.conf')
# remove_user_sasl("bob", '/etc/kafka/config/kafka_jaas.conf')

user_list = parse_jaas_users("/etc/kafka/config/kafka_jaas.conf")
print("Danh sách user:", user_list)
