from datetime import datetime

# Get current time as a string yes1
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to or update done.txt
with open("done.txt", "w") as file:
    file.write(f"Done at: {now}\n")

print("done.txt updated.")
