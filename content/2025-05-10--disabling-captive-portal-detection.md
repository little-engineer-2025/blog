---
Title: Disabling captive portal detection
Date: 2025-05-10 20:15
Modified: 2025-05-10 20:15
Category: system
Tags: android,linux,windows,macos,ios
Slug: disabling-captive-portal-detection
Authors: Alejandro Visiedo
Summary: How to disable captive portal probe
Header_Cover: 
Status: draft
---
# Disabling captive portal detection

Captive Portal is a mechanism that allow WiFi networks redirect to new device connected,
normally to authenticated and allow the device to connect after it.

While this increase the user experience, we could want to disable it if
we don't want such functionality, for instance because we could be
redirected to some content in malicious WiFi networks (is the WiFi
at your hotel trustable? The WiFi at McDonalds? and so on...).

If you had been similar concerns, I hope to give you some clues
about how to disable, so let's start!

## Linux (Network Manager)

We could add the `/usr/lib/NetworkManager/conf.d/90-connectivity.conf` with
the content:

```ini
[connectivity]
enabled=false
uri=http://fedoraproject.org/static/hotspot.txt
reponse=OK
interval=300
```

And restarting network manager by: `run0 systemctl restart NetworkManager.service`

## MacOS



## Windows (captive portal probe)

Edit windows

## Browsers

Meanwhile we can disable this behavior at system level, still the browser
do their own probes, and we can disable this probe.

### Firefox

We can disable this by setting the `network.captive-portal-service.enabled` to `false`
from `about:config` site.

### Google Chrome

### Microsoft Edge

## Mobiles

### Android

Using `adb shell` we run: `settings put global captive_portal_detection_enabled 0`

We check the property is changed by `settings get global_captive_portal_detection_enabled`

### iOS

We need to use [Apple Configurator 2](https://support.apple.com/apple-configurator)
and apply 


## Central proxy

The above works for individual devices; but if you are not using your
devices out of some specific place, you could want to centralize the
management of the above; one option is to use a proxy to access to
internet, and setup rules to reject the probe to the sites used for
the captive portal. Meanwhile this avoid to setup every device, still
make the devices vulnerable to rogue WiFi routers, if the space is
not isolated.

List of endpoints to probe connectivity that trigger captive portal:

```raw
http://captive.apple.com/hotspot-detect.html
http://www.apple.com/library/test/success.html
http://connectivitycheck.gstatic.com/generate_204
http://clients3.google.com/generate_204
http://www.msftncsi.com/ncsi.txt
http://nmcheck.gnome.org/check_network_status.txt
http://networkcheck.kde.org/
http://detectportal.firefox.com/canonical.html
```

Sources:

- https://en.wikipedia.org/wiki/Captive_portal
- https://support.mozilla.org/en-US/kb/captive-portal
- https://


