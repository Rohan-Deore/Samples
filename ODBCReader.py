import obd

# Initialize OBD connection (auto-connects to USB or RF port)
connection = obd.OBD()

# Define the OBD command (sensor) you want to read
cmd = obd.commands.SPEED  # Example: Vehicle speed

# Send the command and parse the response
response = connection.query(cmd)

if response.is_null():
    print("Error: Unable to retrieve data.")
else:
    print(f"Speed: {response.value} km/h")

# Close the OBD connection
connection.close()


