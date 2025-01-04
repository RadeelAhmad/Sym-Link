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

For Symbolic Link
```bash
ln -s [target_file] [link_name]
```

## Python Scripts

**1. generate_flag.py**

This script generates a flag, writes it to flag.txt, and removes the flag after sending it.

```bash                                                                                                                    
┌──(V3c70r㉿kali)-[~/Desktop]
└─$ python3 generate_flag.py
Done.
Done.
```
flag.txt file:

```bash
┌──(root㉿kali)-[/home/V3c70r/Desktop]
└─# cat flag.txt
flag{6107274195}  
```

Symbolic link file also save the same flag that store in flag.txt

```bash
┌──(V3c70r㉿kali)-[~/Desktop]
└─$ sudo cat symbolic_flag.txt                    
flag{6107274195}  
```

**2. Image.py**

This script handles moving an image from the images folder to the temp_images folder and deletes it after processing.

```bash
┌──(V3c70r㉿kali)-[~/Desktop]
└─$ python3 image.py
Image added
Image added
Image added
```

temp-images folder:

```bash
┌──(root㉿kali)-[/home/naahl/Desktop/temp-images]
└─# ls
3.png
```

**3. fetch_flag.py**

```bash
┌──(V3c70r㉿kali)-[~/Desktop]
└─$ sudo python3 fetch_flag.py

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

Select an option:
1 - Kill the generate_flag.py process and fetch the flag
2 - Fetch the flag without killing the process
3 - Fetch Image from temp-images folder
4 - Exit
Enter your choice (1, 2, 3, or 4): 1

[+] Option 1 Selected: Killing the process...
[+] Searching for generate_flag.py process...
[+] Killing process with PID: 6453
[+] generate_flag.py process terminated successfully.
[+] Reading flag from flag.txt...
[+] Flag: flag{6107274195}
```
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


