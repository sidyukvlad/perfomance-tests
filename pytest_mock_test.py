import os
from pytest_mock import MockerFixture


class FileSystem:
    @staticmethod
    def rm(filename: str) -> None:
        os.remove(filename)

def test_unix_fs(mocker: MockerFixture):
    mocker.patch('os.remove')
    FileSystem.rm(filename="file")

    os.remove

