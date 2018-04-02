# Ansible Role apache2

This role installs and configures the NFSv4 kernel servr.


# Example play

```yaml
- hosts: dm.public-debian.vagrant
  become: yes
  vars:
    # role php
    nfs_server_enabled: yes
    nfs_server_exports:
      - path: '/var/www'
        owner: www-data
        group: www-data
        clients:
          - '10.0.0.10(rw,no_root_squash,sync,no_subtree_check)'
    roles:
      - blunix.role-nfs

- hosts: sm.public-debian.vagrant
  become: yes
  tasks:
    - name: install nfs-common
      apt:
        name: nfs-common
        state: installed
        update_cache: no
    - name: mount /var/www from nfs0
      mount:
        path: /var/www
        src: "10.0.0.5:/var/www"
        fstype: nfs4
        opts: "noatime,tcp,bg,nosuid,rsize=32768,wsize=32768,soft,proto=tcp"
        dump: 0
        passno: 0
        state: mounted- hosts: www_webs
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
