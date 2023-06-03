import re
import csv

with open('webpage.html', 'r', encoding='utf-8') as file:
    html_code = file.read()

    name_matches = re.finditer(r'<p\s+class="[^"]*"\s*>(.*?)</p>', html_code, re.DOTALL)
    message_count_matches = re.finditer(r'<p\s+class="[^"]*text-dark-300[^"]*"\s*>(.*?)</p>', html_code, re.DOTALL)
    experience_count_matches = re.finditer(r'<p\s+class="[^"]*hidden[^"]*text-dark-300[^"]*"\s*>(.*?)</p>', html_code, re.DOTALL)
    level_matches = re.finditer(r'<div\s+class="[^"]*text-white[^"]*"\s*>(.*?)</div>', html_code, re.DOTALL)

    names = [match.group(1).strip() for match in name_matches]
    message_counts = [match.group(1).strip() for match in message_count_matches]
    experience_counts = [match.group(1).strip() for match in experience_count_matches]
    levels = [match.group(1).strip() for match in level_matches]

    accounts = zip(names, message_counts, experience_counts, levels)

    with open('accounts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Message Count', 'Experience Count', 'Level'])
        writer.writerows(accounts)

    print("Data saved to accounts.csv")
