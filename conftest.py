import pytest
import subprocess
import os
def pytest_terminal_summary(terminalreporter, exitstatus):
    """
    Hook function to execute code after pytest runs and generate a report.
    """
    try:
        # Call the sendmail script
        # subprocess.run(["python", "sendmail.py"], check=True)

        # Absolute path to the sendmail script in the utilities folder
        script_path = os.path.join(os.path.dirname(__file__), 'utilities', 'sendmail.py')

        # Call the sendmail script and capture output
        result = subprocess.run(
            ["python", script_path],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)


    except subprocess.CalledProcessError as e:
            print(f"Failed to execute sendmail script: {e}")
            print(f"Error output: {e.stderr}")