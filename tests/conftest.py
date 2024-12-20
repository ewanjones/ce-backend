import os

import pytest


@pytest.fixture(scope="session", autouse=True)
def set_env():
    os.environ["SECRET_KEY"] = "testing"
