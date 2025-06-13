---
Title: System monitor gnome extension
Date: 2025-03-29 14:15
Modified: 2025-03-29 14:15
Category: Desktop
Tags: gnome
Slug: system-monitor-gnome-extension
Authors: Alejandro Visiedo
Summary: Installing system monitor shell extension
Status: draft
---
# System monitor gnome extension

If you are using Fedora 41, and try to install the extension
by `dnf install gnome-shell-extension-system-monitor` you
could drive crazy figuring out why the extension is not
even listed (`gnome-extensions list`).

It seems the official version is not working well; but
hopefully, we have some alternatives:

- Fix it and provide the changes as a PR so it will
  get fixed (the project seems abandoned, so no success
  on this).
- Use the fork which provide several fixes, and seems
  active enough at: https://github.com/mgalgs/gnome-shell-system-monitor-next-applet

We describe below the steps to quickly use the second option:

```sh
[ -e ~/opt ] || mkdir ~/opt
[ -e ~/opt/gnome-shell-system-monitor-next-applet ] || git clone https://github.com/mgalgs/gnome-shell-system-monitor-next-applet.git ~/opt/gnome-shell-system-monitor-next-applet
[ -e ~/.local/share/gnome-shell/extensions ] || mkdir -p ~/.local/share/gnome-shell/extensions
cd ~/.local/share/gnome-shell/extensions
ln -svf "$HOME/opt/gnome-shell-system-monitor-next-applet/system-monitor-next@paradoxxx.zero.gmail.com"
gnome-extensions list
gnome-extensions enable system-monitor-next@paradoxxx.zero.gmail.com
```

> I encourage to install from official RPM source, and use the above only if you are
> sure about the source of the repository.

