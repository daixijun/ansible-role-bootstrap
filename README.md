Role name bootstrap
=========

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
