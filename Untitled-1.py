import os

def open_app(app_name):
    # Define the possible installation directories for the application
    possible_dirs = [
        "C:\\Program Files\\",
        "C:\\Program Files (x86)\\",
        "C:\\Users\\{}\\AppData\\Local\\Programs\\".format(os.getlogin())
    ]

    # Iterate over the possible installation directories
    for dir in possible_dirs:
        # Iterate over the files in the directory
        for file in os.listdir(dir):
            # Check if the file is the .exe file for the application
            if file.lower().startswith(app_name.lower()) and file.endswith(".exe"):
                # Open the application
                os.startfile(os.path.join(dir, file))
                return

    # If the application is not found, print an error message
    print("Application not found.")

# Test the function
open_app("Chrome")