import subprocess

# /status
def uptime_info():
    command_uptime = "uptime -p | awk {'print $2\" hours \"$4\" minutes\"'}"
    uptime = subprocess.run(command_uptime, shell=True, capture_output=True, text=True)
    return uptime.stdout

def free_ram_info():
    command_free = "free -h | awk {'print $7'} | grep -o '[^A-Za-z]' | tr -d '\n'"
    free = subprocess.run(command_free, shell=True, capture_output=True, text=True)
    return free.stdout #output in GiB
