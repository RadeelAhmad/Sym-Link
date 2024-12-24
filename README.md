```yaml
  ██████▓██   ██▓ ███▄ ▄███▓    ██▓     ██▓ ███▄    █  ██ ▄█▀
▒██    ▒ ▒██  ██▒▓██▒▀█▀ ██▒   ▓██▒    ▓██▒ ██ ▀█   █  ██▄█▒ 
░ ▓██▄    ▒██ ██░▓██    ▓██░   ▒██░    ▒██▒▓██  ▀█ ██▒▓███▄░ 
  ▒   ██▒ ░ ▐██▓░▒██    ▒██    ▒██░    ░██░▓██▒  ▐▌██▒▓██ █▄ 
▒██████▒▒ ░ ██▒▓░▒██▒   ░██▒   ░██████▒░██░▒██░   ▓██░▒██▒ █▄
▒ ▒▓▒ ▒ ░  ██▒▒▒ ░ ▒░   ░  ░   ░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒
░ ░▒  ░ ░▓██ ░▒░ ░  ░      ░   ░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░░ ░▒ ▒░
░  ░  ░  ▒ ▒ ░░  ░      ░        ░ ░    ▒ ░   ░   ░ ░ ░ ░░ ░ 
      ░  ░ ░            ░          ░  ░ ░           ░ ░  ░   
         ░ ░
```
## Project Structure

```yaml
project-directory/
├── generate_flag.py
├── image.py
├── fetch_flag.py
├── flag.txt
├── images/
├── temp_images/
```
## Setup

**1. Create Required Files and Directories**

Run the following commands to set up the structure:

```bash
mkdir temp_images
touch flag.txt
```

**2. Restrict Permissions**

Ensure that flag.txt and the folders images/ and temp_images/ can only be accessed with sudo privileges:

```bash
sudo chown root:root flag.txt
sudo chmod 600 flag.txt

sudo chmod 700 images
sudo chmod 700 temp_images
sudo chown root:root images
sudo chown root:root temp_images
```

**3. Python Scripts**

1. generate_flag.py

This script generates a flag, writes it to flag.txt, and removes the flag after sending it.

import time

def generate_flag():
    while True:
        flag = "flag{example_flag}"
        with open("flag.txt", "w") as f:
            f.write(flag)
        print("Flag sent: Done")
        time.sleep(10)
        with open("flag.txt", "w") as f:
            f.truncate(0)  # Clear the flag

if __name__ == "__main__":
    generate_flag()

2. image.py

This script handles moving an image from the images folder to the temp_images folder and deletes it after processing.

import os
import shutil
import time

def process_image():
    while True:
        images_folder = "images"
        temp_folder = "temp_images"

        for file_name in os.listdir(images_folder):
            if file_name.endswith(".png"):
                src = os.path.join(images_folder, file_name)
                dest = os.path.join(temp_folder, file_name)

                shutil.copy(src, dest)
                print(f"Image {file_name} sent to temp_images folder.")

                time.sleep(10)
                os.remove(dest)
                print(f"Image {file_name} removed from temp_images folder.")

if __name__ == "__main__":
    process_image()

3. fetch_flag.py

This script provides a menu-driven interface for fetching flags and images.

import os
import signal
import subprocess

FLAG_FILE = "flag.txt"
GENERATE_FLAG_PROCESS = None

def fetch_flag():
    try:
        with open(FLAG_FILE, "r") as f:
            content = f.read().strip()
            print(f"Fetched flag: {content}")
    except Exception as e:
        print(f"Error fetching flag: {e}")

def fetch_flag_kill():
    global GENERATE_FLAG_PROCESS
    if GENERATE_FLAG_PROCESS:
        os.kill(GENERATE_FLAG_PROCESS.pid, signal.SIGTERM)
        print("generate_flag process terminated.")
    fetch_flag()

def fetch_image():
    temp_folder = "temp_images"
    try:
        for file_name in os.listdir(temp_folder):
            if file_name.endswith(".png"):
                print(f"Fetched image: {file_name}")
                return
        print("No images found in temp_images folder.")
    except Exception as e:
        print(f"Error fetching image: {e}")

def main():
    global GENERATE_FLAG_PROCESS
    while True:
        print("\nOptions:")
        print("1. Fetch Flag")
        print("2. Fetch Flag (Kill Process)")
        print("3. Fetch Image")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            fetch_flag()
        elif choice == "2":
            fetch_flag_kill()
        elif choice == "3":
            fetch_image()
        elif choice == "4":
            if GENERATE_FLAG_PROCESS:
                os.kill(GENERATE_FLAG_PROCESS.pid, signal.SIGTERM)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    GENERATE_FLAG_PROCESS = subprocess.Popen(["python3", "generate_flag.py"])
    main()

Usage

Run the scripts with sudo to ensure proper access to restricted files and folders.

Start the fetch_flag.py script to interact with the system.

sudo python3 fetch_flag.py

Follow the menu to fetch flags or images.

Notes

Ensure you have the necessary permissions to run these scripts with sudo.

Use this system responsibly and in compliance with your organization's security policies.

Future Improvements

Add logging for all operations to track activities.

Implement encryption for flags and images to enhance security.

Optimize the scripts for better performance and scalability.


