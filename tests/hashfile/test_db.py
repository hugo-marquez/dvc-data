from dvc_data.hashfile.db import HashFile, HashFileDB


def test_db(tmp_upath):
    odb = HashFileDB(tmp_upath.fs, tmp_upath)

    assert not odb.exists("123456")
    assert list(odb.all()) == []

    obj = odb.get("123456")
    assert type(obj) == HashFile
