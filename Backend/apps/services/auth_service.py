import os


def validate_credentials(username, password):
    expected_username = os.getenv("ADMIN_USERNAME")
    expected_password = os.getenv("ADMIN_PASSWORD")
    if not expected_username or not expected_password:
        return False
    return username == expected_username and password == expected_password
