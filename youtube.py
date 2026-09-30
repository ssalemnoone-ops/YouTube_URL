import re
import sys

#Extracts shareable youtu.be URLs from the YouTube HTML

def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/([\w-]+)'

    matches = re.search(pattern, s, re.IGNORECASE)
    if matches:
        return f'https://youtu.be/{matches.group(1)}'
    else:
        sys.exit("Worng Input; Please Try Again.")





if __name__ == "__main__":
    main()