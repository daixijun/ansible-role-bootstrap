# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [0.0.6](https://github.com/daixijun/ansible-role-bootstrap/compare/v0.0.5...v0.0.6) (2020-04-27)


### Features

* 添加 bootstrap_yum_repository_replace 与 bootstrap_yum_repository_repo 两个变量用于替换默认yum仓库源 ([ae928a0](https://github.com/daixijun/ansible-role-bootstrap/commit/ae928a0e345a0d50941cacb6876df62ebb7a4d08))

### [0.0.5](https://github.com/daixijun/ansible-role-bootstrap/compare/v0.0.4...v0.0.5) (2020-03-29)


### Bug Fixes

* **pam:** 修改pam nofile文件路径 ([4f2796d](https://github.com/daixijun/ansible-role-bootstrap/commit/4f2796d92e12cb9190df8c522d98fdc1531bdaae))
* bootstrap_hostname为空时不配置主机名 ([afa1f7b](https://github.com/daixijun/ansible-role-bootstrap/commit/afa1f7b0d0f116c96af3a7e6a1b1d011260a4672))

### [0.0.4](https://github.com/daixijun/ansible-role-bootstrap/compare/v0.0.3...v0.0.4) (2020-01-04)


### Features

* 移除sysctl相关配置 ([136dc5f](https://github.com/daixijun/ansible-role-bootstrap/commit/136dc5ffe57d265d666efba1830a5146284494da))

### [0.0.3](https://github.com/daixijun/ansible-role-bootstrap/compare/v0.0.2...v0.0.3) (2019-12-04)


### Bug Fixes

* 忽略limits配置导致的失败 ([294128b](https://github.com/daixijun/ansible-role-bootstrap/commit/294128b285868b9a8b6e777a7086bc98a5ad48fb))
