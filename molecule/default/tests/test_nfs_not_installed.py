import os

import testinfra.utils.ansible_runner

# Test if any nfs packages are installed

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nfs_not_installed(host):
    full_package_list = host.run('dpkg --get-selections').stdout
    nfs_package_list = []
    for package_line in full_package_list.split('\n'):
        eline = package_line.encode('utf-8')
        if 'nfs-kernel-server' in eline:
            nfs_package_list.append(eline)
    assert nfs_package_list == []
