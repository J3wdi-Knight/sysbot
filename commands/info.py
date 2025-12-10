import subprocess

# /status
def uptime_info():
    command_uptime = "uptime -p | sed 's/^up //'"
    uptime = subprocess.run(command_uptime, shell=True, capture_output=True, text=True)
    return uptime.stdout

def free_ram_info():
    command_free = "free -h | awk {'print $7'} | grep -o '[^A-Za-z]' | tr -d '\n'"
    free = subprocess.run(command_free, shell=True, capture_output=True, text=True)
    return free.stdout #output in GiB

def top_cpu():
    command_top = "top -bn1 -o %CPU | awk 'NR>7 && NR<=17' | awk '{print $12}'"
    top_per = subprocess.run(command_top, shell=True, capture_output=True, text=True)
    return top_per.stdout
