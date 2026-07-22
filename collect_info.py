from netmiko import ConnectHandler
import pandas as pd

# Read the CSV file
devices = pd.read_csv("devices.csv")

# Empty list to store collected device information
results = []

# Loop through each device
for index, device in devices.iterrows():

    # Device information (used for real connections)
    device_info = {
        "device_type": device["device_type"],
        "host": device["ip"],
        "username": device["username"],
        "password": device["password"]
    }

    print("=" * 50)
    print(f"Processing Device: {device['ip']}")

    # ----------------------------------------------------------------
    # SIMULATED 'show version' OUTPUT
    # Replace this section with ConnectHandler() when using real devices
    # ----------------------------------------------------------------

    output = """
Cisco IOS XE Software, Version 17.09.03

Model number                    : ISR4331

Router#
"""

    # ------------------------
    # Extract Version
    # ------------------------

    version = "Unknown"

    for line in output.splitlines():
        if "Version" in line:
            version = line.split("Version")[1].strip()

    # ------------------------
    # Extract Model
    # ------------------------

    model = "Unknown"

    for line in output.splitlines():
        if "Model number" in line:
            model = line.split(":")[1].strip()

    # ------------------------
    # Extract Hostname
    # ------------------------

    hostname = "Unknown"

    for line in output.splitlines():
        if line.endswith("#"):
            hostname = line.replace("#", "").strip()

    # ------------------------
    # Display Results
    # ------------------------

    print("Hostname :", hostname)
    print("Model    :", model)
    print("Version  :", version)

    # ------------------------
    # Save Results
    # ------------------------

    results.append({
        "IP Address": device["ip"],
        "Hostname": hostname,
        "Model": model,
        "Version": version
    })

# -----------------------------------
# Convert list to DataFrame
# -----------------------------------

df = pd.DataFrame(results)

# Display DataFrame
print("\nCollected Device Information:\n")
print(df)

# -----------------------------------
# Save to Excel
# -----------------------------------

df.to_excel("device_inventory.xlsx", index=False)

print("\nDevice information has been saved to 'device_inventory.xlsx'")