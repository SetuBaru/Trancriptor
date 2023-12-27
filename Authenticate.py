import os


# Attempting to Set Environment Variables for the Google Cloud Platform Service Access Key
def ServiceAccKey():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "private/service_account_key.json"


if __name__ == '__main__':
    ServiceAccKey()
