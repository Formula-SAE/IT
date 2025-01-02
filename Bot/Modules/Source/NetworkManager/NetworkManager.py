

import subprocess


class NetworkError():

    def __init__(self):
        pass

    def handle(self):
        try:
            # List all network interfaces to identify the Wi-Fi adapter name
            result = subprocess.run(["netsh", "interface", "show", "interface"],
                                    capture_output=True, text=True)

            # Look for the Wi-Fi adapter name
            lines = result.stdout.splitlines()
            wifi_adapter = None
            for line in lines:
                if "Wi-Fi" in line or "Wireless" in line:  # Adjust based on your system's adapter name
                    wifi_adapter = line.split()[-1]  # Assuming the last column is the adapter name
                    break

            if not wifi_adapter:
                print("Wi-Fi adapter not found.")
                return

            print(f"Found Wi-Fi adapter: {wifi_adapter}")

            # Enable the Wi-Fi adapter
            enable_result = subprocess.run(["netsh", "interface", "set", "interface", wifi_adapter, "enabled"],
                                           capture_output=True, text=True)

            if enable_result.returncode == 0:
                print("Wi-Fi enabled successfully!")
            else:
                print("Failed to enable Wi-Fi.")
                print(enable_result.stderr)

        except Exception as e:
            print(f"An error occurred: {e}")
