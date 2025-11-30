---
Title: Using SSH through proxy
Date: 2025-06-11 10:39
Modified: 2025-06-11 10:39
Category: system
Tags: ssh,proxy,linux
Slug: using-ssh-through-proxy
Authors: Alejandro Visiedo
Summary: Quick configuration when you only can do outgoing connections by
         using a proxy.
Status: published
---
# Using SSH through proxy

If the system that you are using use a local proxy for the outgoing connections,
your SSH connections will be rejected without any additional configuration.

In my case I would like to use github and gitlab upstreams through the SSH
connection, so I can push my changes.

It could be more solutions, but the one indicated here require `nc` tool
installed in your system, and some changes to `~/.ssh/config` file.

- Install `nc` in fedora by: `run0 dnf install -y nc`
- Open `~/.ssh/config` and add the configuration below:

```raw
Host github.com
    ProxyCommand  nc --proxy-type http --proxy <proxy-host-or-ip>:<proxy-port> %h %p

Host gitlab.com
    ProxyCommand  nc --proxy-type http --proxy <proxy-host-or-ip>:<proxy-port> %h %p
```

> NOTE Change `<proxy-host-or-ip>` by the address of your proxy, and
> `<proxy-port>` by the port where your proxy is listening.

> If the number of hosts is small, I recommend to keep the list specific
> so you can block any outgoing connection to other hosts you don't know
> that your system is connecting to.

## Wrap up!

We have have seen how we can use `nc` to use proxy connections to our git
repositories when we have network restrictions.

Happy coding! :)

