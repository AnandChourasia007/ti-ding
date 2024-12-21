import time
import subprocess
import sys
from playsound import playsound

def print_elapsed_time(elapsed_time):
    hours, rem = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print("Command completed successfully.")
    print(f"Execution Time: ")
    if hours>0 :
        print(f"{int(hours):02} hours")
    if minutes>0 :
        print(f"{int(minutes):02} minutes")
    if seconds>0 :
        print(f"{seconds:.2f} seconds")

def run_command_with_notification():
    if len(sys.argv) < 2:
        print("Usage: notify <command> [args...]")
        sys.exit(1)

    # The command to run
    command = sys.argv[1:]
    sound_file = "alert.wav"  # Default notification sound

    try:
        # Run the terminal command
        start_time = time.time()
        process = subprocess.run(command, check=True, shell=True)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print_elapsed_time(elapsed_time)
        
        # Play the notification sound
        playsound(sound_file)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}.")
        playsound(sound_file)  # Optionally, we can use a different sound for failures.
    except Exception as e:
        print(f"An error occurred: {e}")

