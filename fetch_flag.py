import os
import subprocess
import time
import mimetypes

# Path to the flag.txt file
flag_file = "/home/naahl/Desktop/flag.txt"
temp_images_dir = "/home/naahl/Desktop/temp-images"

# ASCII Banner
banner = r"""
  ██████▓██   ██▓ ███▄ ▄███▓ ▄▄▄▄    ▒█████   ██▓     ██▓ ▄████▄      ██▓     ██▓ ███▄    █  ██ ▄█▀
▒██    ▒ ▒██  ██▒▓██▒▀█▀ ██▒▓█████▄ ▒██▒  ██▒▓██▒    ▓██▒▒██▀ ▀█     ▓██▒    ▓██▒ ██ ▀█   █  ██▄█▒ 
░ ▓██▄    ▒██ ██░▓██    ▓██░▒██▒ ▄██▒██░  ██▒▒██░    ▒██▒▒▓█    ▄    ▒██░    ▒██▒▓██  ▀█ ██▒▓███▄░ 
  ▒   ██▒ ░ ▐██▓░▒██    ▒██ ▒██░█▀  ▒██   ██░▒██░    ░██░▒▓▓▄ ▄██▒   ▒██░    ░██░▓██▒  ▐▌██▒▓██ █▄ 
▒██████▒▒ ░ ██▒▓░▒██▒   ░██▒░▓█  ▀█▓░ ████▓▒░░██████▒░██░▒ ▓███▀ ░   ░██████▒░██░▒██░   ▓██░▒██▒ █▄
▒ ▒▓▒ ▒ ░  ██▒▒▒ ░ ▒░   ░  ░░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░▓  ░░▓  ░ ░▒ ▒  ░   ░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒
░ ░▒  ░ ░▓██ ░▒░ ░  ░      ░▒░▒   ░   ░ ▒ ▒░ ░ ░ ▒  ░ ▒ ░  ░  ▒      ░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░░ ░▒ ▒░
░  ░  ░  ▒ ▒ ░░  ░      ░    ░    ░ ░ ░ ░ ▒    ░ ░    ▒ ░░             ░ ░    ▒ ░   ░   ░ ░ ░ ░░ ░ 
      ░  ░ ░            ░    ░          ░ ░      ░  ░ ░  ░ ░             ░  ░ ░           ░ ░  ░   
         ░ ░                      ░                      ░                                         
"""

def fetch_image():
    """Continuously check for an image in temp-images folder, display it and open the image."""
    print("[+] Checking temp-images folder for images...")
    try:
        result = subprocess.run(
            ["sudo", "ls", temp_images_dir],
            capture_output=True,
            text=True,
        )
        images = [f for f in result.stdout.splitlines() if f.endswith(".png")]
        if images:
            image_path = os.path.join(temp_images_dir, images[0])
            print(f"[+] Image fetched: {image_path}")

            # Check the file size
            file_size = os.path.getsize(image_path)
            print(f"[+] Image size: {file_size} bytes")

            # Check the file permissions
            file_permissions = oct(os.stat(image_path).st_mode)[-3:]
            print(f"[+] Image permissions: {file_permissions}")

            # Verify if it's a valid image file before attempting to open it
            mime_type, _ = mimetypes.guess_type(image_path)
            if mime_type and mime_type.startswith("image"):
                if file_size > 0:
                    # Open the image using eog with sudo privileges
                    subprocess.run(["sudo", "eog", image_path], capture_output=True, text=True)
                    print(f"[+] Image opened successfully.")
                else:
                    print(f"[-] Image is empty or cannot be accessed: {image_path}")
            else:
                print(f"[-] The file {image_path} is not a valid image or cannot be opened.")
        else:
            print("[+] No images found.")
    except Exception as e:
        print(f"[-] Error checking temp-images folder: {e}")


def kill_generate_flag():
    """Find and kill the generate_flag.py process."""
    try:
        print("[+] Searching for generate_flag.py process...")
        result = subprocess.run(
            ["pgrep", "-f", "generate_flag.py"], capture_output=True, text=True
        )
        pids = result.stdout.strip().split("\n")

        if not pids or pids == [""]:
            print("[-] No generate_flag.py process found.")
            return

        for pid in pids:
            print(f"[+] Killing process with PID: {pid}")
            os.kill(int(pid), 9)  # Send SIGKILL signal
        print("[+] generate_flag.py process terminated successfully.")
    except Exception as e:
        print(f"[-] Failed to kill generate_flag.py: {e}")

def fetch_flag():
    """Fetch and display the flag from the flag.txt file."""
    try:
        print("[+] Reading flag from flag.txt...")
        result = subprocess.run(
            ["sudo", "cat", flag_file], capture_output=True, text=True
        )
        if result.returncode == 0:
            flag = result.stdout.strip()
            print(f"[+] Flag: {flag}")
        else:
            print(f"[-] Failed to read flag.txt: {result.stderr}")
    except Exception as e:
        print(f"[-] An error occurred while reading flag: {e}")

def main_menu():
    """Display the main menu in a loop until the user exits."""
    while True:
        print(banner)

        # Show options to the user
        print("Select an option:")
        print("1 - Kill the generate_flag.py process and fetch the flag")
        print("2 - Fetch the flag without killing the process")
        print("3 - Fetch Image from temp-images folder")
        print("4 - Exit")

        choice = input("Enter your choice (1, 2, 3, or 4): ").strip()

        if choice == "1":
            print("\n[+] Option 1 Selected: Killing the process...")
            kill_generate_flag()
            time.sleep(1)  # Small delay
            fetch_flag()
        elif choice == "2":
            print("\n[+] Option 2 Selected: Fetching the flag without killing the process...")
            fetch_flag()
        elif choice == "3":
            print("\n[+] Option 3 Selected: Fetching Image from temp-images...")
            fetch_image()
        elif choice == "4":
            print("\n[+] Exiting. Goodbye!")
            break
        else:
            print("\n[-] Invalid choice. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main_menu()
