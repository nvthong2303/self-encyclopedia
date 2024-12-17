import subprocess


def get_volume_info_from_df(path):
    try:
        output = subprocess.check_output(['df', '-h', path], text=True)
        lines = output.splitlines()
        if len(lines) > 1:
            parts = lines[1].split()
            return {
                "filesystem": parts[0],
                "size": parts[1],
                "used": parts[2],
                "available": parts[3],
                "used_percent": parts[4],
                "mount_point": parts[5]
            }
    except Exception as e:
        print(f"Error fetching volume info: {e}")
        return None


volume_info = get_volume_info_from_df("/var/lib/")
print(volume_info)
