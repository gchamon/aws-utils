import json
import urllib

import boto3


def get_session_from_role(role_name, region_name, timeout=1):
    try:
        credentials = json.loads(
            urllib.request
                .urlopen(f"http://169.254.169.254/latest/meta-data/iam/security-credentials/{role_name}",
                         timeout=timeout)
                .read()
                .decode()
        )
        return boto3.Session(region_name=region_name,
                             aws_access_key_id=credentials["AccessKeyId"],
                             aws_secret_access_key=credentials["SecretAccessKey"],
                             aws_session_token=credentials["Token"])
    except urllib.error.URLError:
        return boto3.Session(region_name=region_name)
