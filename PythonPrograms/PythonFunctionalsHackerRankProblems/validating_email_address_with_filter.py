# def fun(s):
#     # return True if s is a valid email, else return False
#     import re
#     if(re.search(r"^[\w,-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$",s)):
#         return True
#     else:
#         return False
#
# def filter_mail(emails):
#     return list(filter(fun, emails))
#
# if __name__ == '__main__':
#     n = int(input())
#     emails = []
#     for _ in range(n):
#         emails.append(input())
#
# filtered_emails = filter_mail(emails)
# filtered_emails.sort()
# print(filtered_emails)

def fun(s):
    try:
        username, other = s.split('@')
        websitename, extension = other.split('.')
    except:
        return False

    username = username.replace("-", "").replace("_", "")
    if username.isalnum() == False:
        return False
    elif websitename.isalnum() == False:
        return False
    elif len(extension) > 3:
        return False
    else:
        return True
    # return True if s is a valid email, else return False


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


