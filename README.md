daixijun.bootstrap
=========

[![Build Status](https://github.com/daixijun/ansible-role-bootstrap/workflows/build/badge.svg)](https://github.com/daixijun/ansible-role-bootstrap/actions)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-daixijun.bootstrap-660198.svg?style=flat)](https://galaxy.ansible.com/daixijun/ansible-role-bootstrap/)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/daixijun/ansible-role-bootstrap?sort=semver)](https://github.com/daixijun/ansible-role-bootstrap/tags)

系统初始化

Requirements
------------

* Centos 7+
* Ansible 2.7+

Role Variables
--------------

```yaml
bootstrap_timezone: Asia/Shanghai
bootstrap_upgrade: false
bootstrap_hostname: ''
```

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
      - { role: daixijun.bootstrap }
```

License
-------

BSD

Author Information
------------------

Xijun Dai <daixijun1990@gmail.com>
