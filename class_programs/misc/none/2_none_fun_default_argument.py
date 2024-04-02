# None is often used as a default value for function arguments that are optional.

def send_email(address, subject, body, attachment=None):
    if attachment is None:
        print("Sending email without an attachment...")
    else:
        print("Sending email with an attachment...")


send_email("example@example.com", "Hello", "This is the body")
send_email("example@example.com", "Hello", "This is the body", "file.pdf")
