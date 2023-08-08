import os
import datetime
import subprocess

def get_formatted_date():
    # Get the current date
    current_date = datetime.datetime.now()

    # Format the date as "Month day_suffix Year", e.g., "July 23rd 2023"
    day_suffix = "th"
    if 10 <= current_date.day % 100 <= 20:
        day_suffix = "th"
    else:
        day_suffix = {1: "st", 2: "nd", 3: "rd"}.get(current_date.day % 10, "th")

    formatted_date = current_date.strftime(f"%B %d{day_suffix} %Y")
    return formatted_date

def get_next_script_number(folder):
    # Get a list of all files in the folder
    file_list = os.listdir(folder)

    # Filter the files to get only those with the naming pattern "python_practice_N.py"
    script_files = [f for f in file_list if f.startswith("problem_") and f.endswith(".py")]

    # Extract the numbers from the filenames and find the maximum
    numbers = [int(f[len("problem_"):-len(".py")]) for f in script_files]
    next_number = max(numbers) + 1 if numbers else 1

    return next_number

def generate_python_script(file_name, date, number):
    # The content of the new Python script you want to generate
    script_content = f"""
## https://www.w3resource.com/python-exercises/puzzles/index.php
## {date}
## Problem number {number}

# Main
def main():
    print("")
    
# Run main()
if __name__ == "__main__":
    main()
"""

    # Write the script_content to a new file with the provided file_name
    with open(file_name, "w") as f:
        f.write(script_content)

if __name__ == "__main__":
    date = get_formatted_date()
    folder_path = "." 
    next_script_number = get_next_script_number(folder_path)
    new_script_file_name = f"problem_{next_script_number}.py"
    generate_python_script(new_script_file_name, date, next_script_number)
    print(f"New Python script '{new_script_file_name}' has been created.")

    # Close the active window after the script finishes
    pid = os.getpid()
    subprocess.run(["taskkill", "/F", "/PID", str(pid)])
    
