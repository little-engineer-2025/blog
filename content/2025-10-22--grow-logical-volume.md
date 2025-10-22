---
Title: Grow logical volume
Date: 2025-10-22 17:52
Modified: 2025-10-22 17:52
Category: 
Tags: raspi,fedora
Slug: grow-logical-volume
Authors: Alejandro Visiedo
Summary: Quick steps that I followed to extend the logical volume to the whole disk in a fedora system.
Header_Cover: 
---
# Grow logical volume

Sometimes I had been the scenario where I needed to extend the
logical volume of my system such as:

- A VM which required more space and after increase the available disk
  I had to extend the logical volume.
- A raspy using not the usual distros.

The same steps worked for me in a fedora system. I won't extend
and I will go straight to the point.

In this steps I am using `/dev/sda3` update it for your scenario:

- Increase the physical partition: `fdisk /dev/sda3`
- Increase the physical volume: `pvresize /dev/sda3`
- Increase logical volume: `/dev/mapper/systemVG-LVRoot -L+100%FREE`
- Grow filesystem: `xfs_growfs /dev/mapper/systemVG-LVRoot`

> Hope this helps you in similar scenario, take the above steps at your
> own risk and create a backup before run them if you are not sure
> what your are running. Be warned that something wrong could
> state in a broken system.

See you on the next post!

