from capture.services import auth


class TestPasswords:
    def test_password_hash_and_verify(self) -> None:
        hashed_password = auth.hash_password("testing")

        assert auth.verify_password("testing", hashed_password)
