import os

API_URL = os.getenv('CF_URL', 'https://api.bosh-lite.com')
MASTER_PASSWORD = os.getenv('MASTER_PASSWORD', 'admin')
MASTER_USERNAME = os.getenv('MASTER_USERNAME', 'admin')
TEST_ORG = os.getenv("TEST_ORG", "TEST_ORG")
TEST_SPACE = os.getenv("TEST_SPACE", "TEST_SPACE")
ORG_MANAGER = os.getenv("ORG_MANAGER", "ORG_MANAGER")
ORG_MANAGER_PASSWORD = os.getenv(
    "ORG_MANAGER_PASSWORD", "ORG_MANAGER_PASSWORD")
ORG_AUDITOR = os.getenv("ORG_AUDITOR", "ORG_AUDITOR")
ORG_AUDITOR_PASSWORD = os.getenv(
    "ORG_AUDITOR_PASSWORD", "ORG_AUDITOR_PASSWORD")
SPACE_MANAGER = os.getenv("SPACE_MANAGER", "SPACE_MANAGER")
SPACE_MANAGER_PASSWORD = os.getenv(
    "SPACE_MANAGER_PASSWORD", "SPACE_MANAGER_PASSWORD")
SPACE_DEVELOPER = os.getenv("SPACE_DEVELOPER", "SPACE_DEVELOPER")
SPACE_DEVELOPER_PASSWORD = os.getenv(
    "SPACE_DEVELOPER_PASSWORD", "SPACE_DEVELOPER_PASSWORD")
SPACE_AUDITOR = os.getenv("SPACE_AUDITOR", "SPACE_AUDITOR")
SPACE_AUDITOR_PASSWORD = os.getenv(
    "SPACE_AUDITOR_PASSWORD", "SPACE_AUDITOR_PASSWORD")
API_URL = os.getenv('CF_URL', 'https://api.bosh-lite.com')
TEST_USER = os.getenv('TEST_USER', 'TEST_USER')
TEST_USER_PASSWORD = os.getenv('TEST_USER_PASSWORD', 'TEST_USER_PASSWORD')
TEST_ORG_2 = os.getenv("TEST_ORG_2", "TEST_ORG_2")
TEST_SPACE_2 = os.getenv("TEST_SPACE_2", "TEST_SPACE_2")
TEST_APP = os.getenv("TEST_APP", "TEST_APP")
TEST_ORG_UPDATE = os.getenv("TEST_ORG_UPDATE", "TEST_ORG_UPDATE")
TEST_SPACE_UPDATE = os.getenv("TEST_SPACE_UPDATE", "TEST_SPACE_UPDATE")
CLOSED_SECURITY_GROUP = os.getenv("CLOSED_GROUP", "CLOSED_GROUP")
OPEN_SECURITY_GROUP = os.getenv("OPEN_GROUP", "OPEN_GROUP")
