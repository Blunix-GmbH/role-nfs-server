# Ansible Role apache2

This role installs and configures the NFSv4 kernel servr.


# Example play

```yaml
- hosts: dm.public-debian.vagrant
  vars:
    nfs_server_enabled: yes
    nfs_server_exports:
      - path: ''/var/www'
        clients:
          - '10.10.0.5(rw,no_root_squash,sync,no_subtree_check)'
  roles:
    - blunix.role-nfs
```

# License

Apache-2.0

# Author Information

Service and support for orchestrated hosting environments,
continuous integration/deployment/delivery and various Linux
and open-source technology stacks are available from:

```
Blunix GmbH - Consulting for Linux Hosting 24/7
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: service[at]blunix.org
Phone: (+49) 30 / 12 08 39 90
```
