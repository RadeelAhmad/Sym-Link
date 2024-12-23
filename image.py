import os
import random
import subprocess
import time

# Paths to the folders
images_dir = "/home/naahl/Desktop/images"
temp_images_dir = "/home/naahl/Desktop/temp-images"

def copy_and_delete_image():
    """Copy a random image from 'images' to 'temp-images', wait, and delete it."""
    try:
        # List all image files in the 'images' folder using sudo
        result = subprocess.run(
            ["sudo", "ls", images_dir],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"Error listing files: {result.stderr}")
            return

        images = [f for f in result.stdout.splitlines() if f.endswith(".png")]
        if not images:
            print("No images left in the 'images' folder.")
            return

        # Select a random image
        selected_image = random.choice(images)
        source = os.path.join(images_dir, selected_image)
        destination = os.path.join(temp_images_dir, selected_image)

        # Copy the image using sudo
        subprocess.run(["sudo", "cp", source, destination], check=True)
        print("Image added")  # Only display 'Image added'

        # Wait 7 seconds
        time.sleep(7)

        # Delete the image from 'temp-images' using sudo
        subprocess.run(["sudo", "rm", destination], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        copy_and_delete_image()
        # Wait 5 seconds before the next loop iteration
        time.sleep(3)

if __name__ == "__main__":
    main()
