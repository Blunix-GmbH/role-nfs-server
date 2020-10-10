import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_executable_exists(host):
    assert host.file('/sbin/mount.nfs4').exists


def test_testfile_in_mountpoint_exists(host):
    assert host.file('/srv/testfile.txt').exists
