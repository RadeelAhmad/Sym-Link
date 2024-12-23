import time
import random
import subprocess

# Path to the flag.txt file
file_path = '/home/naahl/Desktop/flag.txt'

# Function to write to the file with sudo privileges and suppress output
def write_with_sudo(content, file_path):
    # Use sudo to write the content to the file and suppress stdout output
    command = ['sudo', 'tee', file_path, '> /dev/null']  # Suppresses the output
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.communicate(input=content.encode())

while True:
    # Generate a random number up to 10 digits (between 1 and 9999999999)
    random_number = random.randint(1, 9999999999)
    
    # Format the flag as flag{<random-number>}
    flag = f"flag{{{random_number}}}"
    
    # Write to the file with sudo privileges (it will overwrite the file)
    write_with_sudo(flag, file_path)
    
    # Print "Done." after writing to the file (this won't print the flag)
    print("Done.")
    
    # Wait for 1 minute before running the loop again
    time.sleep(10)
