'''
Validate IP Address
Check if a given string is a valid IPv4 or IPv6 address.
Example:
Input: "192.168.0.1"
Output: "IPv4"
'''


def validate_ip(IP):
    if '.' in IP:
        parts = IP.split('.')
        if len(parts) == 4:
            for part in parts:
                if not part.isdigit() or not 0 <= int(part) <= 255 or (part[0] == '0' and len(part) > 1):
                    return "Neither"
            return "IPv4"
    elif ':' in IP:
        parts = IP.split(':')
        if len(parts) == 8:
            for part in parts:
                if not (1 <= len(part) <= 4) or not all(c in "0123456789abcdefABCDEF" for c in part):
                    return "Neither"
            return "IPv6"
    return "Neither"

# Example usage
print(validate_ip("192.168.0.1"))        # IPv4
print(validate_ip("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # IPv6
print(validate_ip("256.256.256.256"))    # Neither



