#Yp2 
import re
import requests

# Read URLs from the .txt file
input_txt_filename = "input_urls.txt"
with open(input_txt_filename, "r") as file:
    urls = file.read().splitlines()

# Extract mobile numbers for each URL
mobile_numbers = []
for url in urls:
    # Send a GET request to the URL
    response = requests.get(url)

    # Find the mobile number
    mobile_number_pattern = r"\d{3}-\d{3}-\d{4}"
    mobile_number_match = re.search(mobile_number_pattern, response.text)
    if mobile_number_match:
        mobile_number = mobile_number_match.group()
    else:
        mobile_number = "Mobile number not found"

    mobile_numbers.append(mobile_number)

# Save the extracted mobile numbers to the .txt file
output_txt_filename = "output_mobile_numbers.txt"
with open(output_txt_filename, "w") as file:
    for number in mobile_numbers:
        file.write(number + "\n")

print(f"Mobile numbers extracted from {len(urls)} URLs and saved to {output_txt_filename}")
