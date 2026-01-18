# Count valid Email
def count_valid_emails(emails):
    """
    Count the number of valid email addresses in the input list.
    
    Args:
        emails: A list of strings that may contain email addresses.
    
    Returns:
        int: The count of valid email addresses, or 0 if the list is empty or None.
    """
    # Empty or None input
    if not emails:
        return 0
    
    count = 0  # valid emails counter

    # Iterate through each email in the list
    for email in emails:
        # Check if the item is a string (not None or other type)
        if isinstance(email, str):
            # Basic validation: email must contain '@' and at least one '.' after '@'
            if "@" in email and "." in email:
                # Split on '@' to verify there's content before and after
                parts = email.split("@")
                # Valid if: exactly one '@', content before '@', and '.' in domain part
                if len(parts) == 2 and parts[0] and "." in parts[1]:
                    # Check that domain has content after the last '.'
                    domain_parts = parts[1].split(".")
                    if len(domain_parts) >= 2 and all(part for part in domain_parts):
                        count += 1

    return count
