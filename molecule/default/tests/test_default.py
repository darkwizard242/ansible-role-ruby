import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE1 = 'ruby-full'
PACKAGE2 = 'ruby'
PACKAGE_BINARY = '/usr/bin/ruby'


def test_ruby_package_installed(host):
    """
    Tests if ruby-full/ruby is installed.
    """
    assert host.package(PACKAGE1).is_installed or \
        host.package(PACKAGE2).is_installed


def test_ruby_binary_exists(host):
    """
    Tests if ruby binary exists.
    """
    host.file(PACKAGE_BINARY).exists


def test_ruby_binary_file(host):
    """
    Tests if ruby binary is file type.
    """
    host.file(PACKAGE_BINARY).is_file


def test_ruby_binary_which(host):
    """
    Tests the output to confirm ruby's binary location.
    """
    assert host.check_output('which ruby') == PACKAGE_BINARY
