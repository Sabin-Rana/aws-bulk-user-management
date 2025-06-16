"""
AWS IAM User Generator - PRODUCTION READY
Creates 100 test users with randomized passwords
Output: ../scripts/sales-users.csv (gitignored)
"""
import csv
import random
import string
import os
from pathlib import Path

def generate_password():
    """Generate 12-character password meeting AWS requirements"""
    chars = string.ascii_letters + string.digits + "!@#%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

def generate_users():
    """Generate CSV with test users"""
    # Create scripts directory if missing
    output_dir = Path("../scripts")
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / "sales-users.csv"
    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["User Name", "Password", "Access Key", "Secret Key"])
        
        for i in range(1, 101):
            writer.writerow([
                f"sales{i}",
                generate_password(),
                "auto",  # AWS generates real keys
                "auto"   # Never store actual secrets
            ])
    print(f"✅ Generated {output_file} with 100 test users")
    print(f"Location: {output_file.resolve()}")

if __name__ == "__main__":
    generate_users()