[![build-test](https://github.com/darkwizard242/ansible-role-ruby/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-ruby/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-ruby/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-ruby/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/ruby) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-ruby&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-ruby) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-ruby&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-ruby) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-ruby&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-ruby) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-ruby?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-ruby?color=orange&style=flat-square)

# Ansible Role: ruby

Role to install [ruby](https://www.ruby-lang.org/en/) package on **Debian/Ubuntu** and **EL** systems. These are the default versions available in repositories and may change based on whatever is available on the default OS repositories.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
ruby_app_debian_package: ruby-full
ruby_app_el_package: ruby
ruby_desired_state: present
```

### Variables table:

Variable                | Description
----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
ruby_app_debian_package | Defines the app to install on Debian based systems i.e. **ruby-full**
ruby_app_el_package     | Defines the app to install on Enterprise Linux (Redhat/CentOS) systems i.e. **ruby**
ruby_desired_state      | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **ruby** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.ruby
```

For customizing behavior of role (i.e. installation of latest **ruby** package instead of ensure it is installed ) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.ruby
  vars:
    ruby_desired_state: latest
```

For customizing behavior of role (i.e. installation of **ruby** package in regards to EL systems) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.ruby
  vars:
    ruby_app_el_package: ruby
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-ruby/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/), a DevOps/CloudOps Engineer who loves to learn and contribute to Open Source community.
