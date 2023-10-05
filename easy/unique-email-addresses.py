# https://leetcode.com/problems/unique-email-addresses/


def num_unique_emails(emails: list[str]) -> int:
    validate_email_set = set()
    for email in emails:
        name, domain = email.split("@")
        name = name.split("+")[0].replace(".", "")
        validate_email_set.add(f"{name}@{domain}")
    return len(validate_email_set)


def main():
    # emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    print(num_unique_emails(emails))


if __name__ == '__main__':
    main()
