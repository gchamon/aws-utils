import boto3
import requests

METADATA_URL = "http://169.254.169.254/latest/meta-data"


def get_session_from_attached_role(region_name):
    role_name = get_role_attached_to_instance()
    return get_session_from_role(role_name=role_name,
                                 region_name=region_name)


def get_role_attached_to_instance():
    response = requests.get(f"{METADATA_URL}/iam/security-credentials")
    response.raise_for_status()
    return response.text


def get_session_from_role(role_name, region_name, timeout=1):
    try:
        response = requests.get(f"{METADATA_URL}/iam/security-credentials/{role_name}",
                                timeout=timeout)
        response.raise_for_status()
        credentials = response.json()

        return boto3.Session(region_name=region_name,
                             aws_access_key_id=credentials["AccessKeyId"],
                             aws_secret_access_key=credentials["SecretAccessKey"],
                             aws_session_token=credentials["Token"])
    except requests.HTTPError:
        return boto3.Session(region_name=region_name)
