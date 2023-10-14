import platform
import os

print(f"System: {platform.system()}")
print(f"Hostname: {os.uname()[1]}")
print(f"Current Working Directory: {os.getcwd()"})
