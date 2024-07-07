# To test particular methods only when a certain condition meets
# for example to execute methods for particuloar so only

import pytest

@pytest.mark.windows
def win_os_1():
    assert True
@pytest.mark.windows
def win_os_2():
    assert True

@pytest.mark.mac
def mac_os_1():
    assert True
@pytest.mark.mac
def mac_os_2():
    assert True