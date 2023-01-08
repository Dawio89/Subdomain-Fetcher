import requests
import json

def find_subdomains():
    domain = input("Enter the domain: ")
    subdomains = set()

    response = requests.get(f"https://crt.sh/?q=%.{domain}&output=json")

    subdomain_list = json.loads(response.text)

    for subdomain_dict in subdomain_list:
        subdomain = subdomain_dict["name_value"]

        if "." in subdomain and subdomain.endswith(domain):
            subdomain = subdomain.strip()
            subdomain = " ".join(subdomain.split())
            subdomains.add(subdomain)

    with open(f"{domain}.txt", "w") as f:
        for i, subdomain in enumerate(sorted(subdomains)):
            f.write(subdomain)
            if i < len(subdomains) - 1:
                f.write("\n")

find_subdomains()
