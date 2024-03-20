# WinRM Monitoring Script

This Python script monitors the status of the Windows Remote Management (WinRM) service and automatically disables it if it is found to be running. Additionally, it sends an email notification when the WinRM service is detected as enabled.

## Features

- Continuously checks the status of the WinRM service at regular intervals (default: 30 seconds).
- Disables the WinRM service if it is found to be running.
- Sends an email notification using the Mailgun API when the WinRM service is detected as enabled.
- Handles keyboard interrupts (Ctrl+C) gracefully and displays a message when monitoring is stopped by the user.

## Prerequisites

- Python 3.x installed on the system.
- Required Python packages: `smtplib`, `email`.
- Mailgun API credentials (username and password) for sending email notifications.

## Configuration

Before running the script, make sure to update the following configuration variables:

- `mailgun_user`: Your Mailgun API username.
- `mailgun_password`: Your Mailgun API password.
- `recipient`: The email address where notifications will be sent.

## Usage

1. Clone the repository or download the script file.
2. Open the script file in a text editor and update the configuration variables as mentioned above.
3. Save the script file.
4. Open a command prompt or terminal and navigate to the directory where the script is located.
5. Run the script using the following command:
   ```
   python winrm_monitoring.py
   ```
6. The script will start monitoring the WinRM service and display the current status in the console.
7. If the WinRM service is found to be running, the script will disable it and send an email notification.
8. To stop the monitoring, press Ctrl+C. The script will display a message indicating that monitoring has been stopped by the user.

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT).

## Disclaimer

This script is provided as-is without any warranty. Use it at your own risk. The author is not responsible for any damage or loss caused by the usage of this script.
