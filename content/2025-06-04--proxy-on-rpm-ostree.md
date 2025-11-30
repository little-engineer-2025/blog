---
Title: proxy on rpm-ostree
Date: 2025-06-04 15:43
Modified: 2025-06-04 15:43
Category: system
Tags: os,linux,system
Slug: proxy-on-rpm-ostree
Authors: Alejandro Visiedo
Summary: Make rpm-ostree works with our proxy could be not trivial.
         This article describe how I did (or what I missed).
Status: published
---
# proxy on rpm-ostree

Hi there! if you are here, probably are facing similar situation
than me today! I installed Fedora Silverblue in a fresh VM, and
I use a proxy to reach out Internet, so how to make the things
work in Silverblue? I am going to enumerate the failed intents,
before the final solution.

## Failed intents

The first thing I thought was, well just setup the http in the
system and that will make everything. Yeah! I did it, and I rebooted
even several times, but no connection was happening through the
proxy. It makes things like `curl` works from my terminal, but
for any reason, not for `rpm-ostree`.

Secondly, I thought "well, maybe I have to indicate that information
into the repo files". So I edited every `.repo` file at
`/etc/yum.repos.d/*.repo` and I realoaded rpm-ostree by

`run0 systemctl daemon-reload; run0 systemctl restart rpm-ostreed.service`

Even I tried to reboot, but still rpm-ostree was failing and the
request didn't go through my proxy.

Later, I tried googling about it, and I found the below reference
which was really helpful:

https://github.com/coreos/rpm-ostree/issues/762#issuecomment-434256478

I did the change by: `run0 systemctl edit --full rpm-ostreed.service`,
and adding the change below:

```toml
[Service]
Environment="http_proxy=http://<ip-for-my-proxy>:<port>"
```

I run `run0 systemctl daemon-reload; run0 systemctl restart rpm-ostreed.service`,
but surprise, still not working! And I rebooted and nothing changed.

## Final change

Finally, I realized that I could require another environment variable, and that
was the key in case for it, so I added `HTTPS_PROXY` and I run
`run0 systemctl daemon-reload; run0 systemctl restart rpm-ostreed.service` and
finally, it started to work.

## Wrap up!

If you are using a proxy in your system, and you want to use Silverblue
or other rpm-ostree based distribution, you will need to add manually the
`http_proxy` and `HTTPS_PROXY` to the rpm-ostreed.service configuration.

```sh
run0 systemctl edit --full rpm-ostreed.service
```

Add the environment variables:

```toml
[Service]
Environment="http_proxy=http://<ip-for-my-proxy>:<port>"
Environment="HTTPS_PROXY=http://<ip-for-my-proxy>:<port>"
```

Reload the configuration and restart the service by:

```sh
run0 systemctl daemon-reload
run0 systemctl restart rpm-ostreed.service
```

And finally upgrade your system:

```sh
run0 rpm-ostree upgrade
```

