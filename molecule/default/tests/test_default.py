import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_etc_timezone(host):
    f = host.file('/etc/timezone')

    assert f.exists
    assert f.content_string == 'Asia/Shanghai'


def test_etc_localtime(host):
    f = host.file('/etc/localtime')

    assert f.exists
    assert f.is_symlink
    # assert f.linked_to == '/usr/share/zoneinfo/Asia/Shanghai'
