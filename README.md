# daixijun.bootstrap

[![Build Status](https://github.com/daixijun/ansible-role-bootstrap/workflows/build/badge.svg)](https://github.com/daixijun/ansible-role-bootstrap/actions)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-daixijun.bootstrap-660198.svg?style=flat)](https://galaxy.ansible.com/daixijun/ansible-role-bootstrap/)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/daixijun/ansible-role-bootstrap?sort=semver)](https://github.com/daixijun/ansible-role-bootstrap/tags)

系统初始化,主要功能如下:

- 更新系统软件
- 修改时区
- 配置主机名
- 修改PAM nofile 限制

## 环境要求

- RHEL/Centos 6.x / 7.x / 8.x
- Ansible 2.7+

## 变量

```yaml
# 时区，默认为 Asia/Shanghai
bootstrap_timezone: Asia/Shanghai
# 是否更新系统上所有软件，相当于执行 `yum update -y`
bootstrap_upgrade: false
# 主机名，为空时不配置
bootstrap_hostname: ''
```

## 依赖

无

## 使用示例

```yaml
- hosts: servers
  roles:
      - { role: daixijun.bootstrap, bootstrap_hostname: "hostname.example.com" }
```

## License

BSD

## 维护者

- Xijun Dai <daixijun1990@gmail.com>
