from mmdesigner import __version__

def test_version():
    """ceck current version string"""
    mmd = mmdesigner
    assert mmd.version() == __version__
