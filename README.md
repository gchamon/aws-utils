# aws-utils

Common aws utilities to be shared between company projects

## Installing

pipenv:

* `pipenv install -e git+https://github.com/lettdigital/aws-utils.git#egg=aws-utils`

pip

* `pip install git+https://github.com/lettdigital/aws-utils.git`

## Utilities

### AWS Secrets Manager

`aws_utils.secrets.get`

arguments:

| name  | type  | default  | description  |
|---|---|:---:|---|
| secret_name  | string  | -  | Name of the secret to get from aws  |
| region_name  | string  | -  | AWS Region Name  |

returns:

* A python object deserialized from a valid JSON String

### Boto3 Session

`aws_utils.session.get_session_from_role`

arguments:

| name  | type  | default  | description  |
|---|---|:---:|---|
| role_name  | string  | -  | Name of the role to get the credentials from  |
| region_name  | string  | -  | AWS Region Name  |
| timeout  | integer  | 1  | Timeout to read from aws ec2 introspection service  |

returns:

* An instance of `boto3.session.Session`
