---
Title: Run windows powershell scripts
Date: 2026-02-13 10:00
Modified: 2026-02-13 10:00
Category: Windows
Tags: windows, powershell, profile
Slug: run-windows-powershell-scripts
Authors: Alejandro Visiedo
Summary: Hot to get your $PROFILE signed and running
Header_Cover: static/header-cover.jpg
Status: published
---
# Run windows powershell scripts

I have not used windows from a while, and several things that I use to do in
Linux systems, are different in Windows. One of this things are customize my
Windows terminal session by using an init script ($PROFILE) so I can define
useful alises. In particular I want to start defining my dotfiles alias to
run it in the same way I do in Linux.

- Define the initial content for the `$PROFILE` file.
- Create a self-signed certificate.
- Sign the `$PROFILE` file.
- Verify we can run `$PROFILE` with no issues, and the function `dotfiles` is
  available.

## Define the initial content

```powershell
function dotfiles {
  git --git-dir="$HOME/.dotfiles/" --work-tree="$HOME" @args
}
```

## Create a self-signed certificate

```powershell
$certName = "Alejandro Visiedo"
$dnsName = "PowerShellLocal"
$cert = New-SelfSignedCertificate -Type CodeSigningCert `
                                  -Subject "CN=$certName" `
                                  -DnsName $dnsName `
                                  -CertStoreLocation "Cert:\CurrentUser\My" `
                                  -NotAfter (Get-Date).AddYears(5) `
                                  -KeyExportPolicy Exportable
```

> We can check the certificate by running `certmgr.msc`

And now configure the trust on the new certificate by:

```powershell
$stores = "Root", "TrustedPublisher"
foreach ($storeName in $stores) {
    $store = New-Object System.Security.Cryptography.X509Certificates.X509Store($storeName, "CurrentUser")
    $store.Open("ReadWrite")
    $store.Add($cert)
    $store.Close()
    Write-Host "Added to: $storeName"
}
```

## Sign the `$PROFILE` file

```powershell
if (!(Test-Path $PROFILE)) { 
    New-Item -Path $PROFILE -Type File -Force 
    Add-Content $PROFILE "# File $PROFILE signed"
}

$status = Set-AuthenticodeSignature -FilePath $PROFILE -Certificate $cert
$status.Status
```

## Verify

```powershell
Get-AuthenticodeSignature $PROFILE | Select-Object Path, Status, Hash
```

## Final script

Before to enable $PROFILE you have to run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy AllSigned
```

```powershell
# 1. Configure names
$certName = "Alejandro Visiedo"
$dnsName = "PowerShellLocal"

Write-Host "--- Generating Certificate ---" -ForegroundColor Yellow
$cert = New-SelfSignedCertificate -Type CodeSigningCert `
                                  -Subject "CN=$certName" `
                                  -DnsName $dnsName `
                                  -CertStoreLocation "Cert:\CurrentUser\My" `
                                  -NotAfter (Get-Date).AddYears(5) `
                                  -KeyExportPolicy Exportable

Write-Host "Certificate create with Thumbprint: $($cert.Thumbprint)"

# 2. Trust on the certificate (Move to root and trusted editors)
Write-Host "--- Configuring trust ---" -ForegroundColor Yellow
$stores = "Root", "TrustedPublisher"
foreach ($storeName in $stores) {
    $store = New-Object System.Security.Cryptography.X509Certificates.X509Store($storeName, "CurrentUser")
    $store.Open("ReadWrite")
    $store.Add($cert)
    $store.Close()
    Write-Host "Added to: $storeName"
}

# 3. Sign $PROFILE
Write-Host "--- Signing $PROFILE ---" -ForegroundColor Yellow
if (!(Test-Path $PROFILE)) { 
    New-Item -Path $PROFILE -Type File -Force 
    Add-Content $PROFILE "# File $PROFILE signed"
}

$status = Set-AuthenticodeSignature -FilePath $PROFILE -Certificate $cert
$status.Status

Write-Host "--- Verification ---" -ForegroundColor Yellow
Get-AuthenticodeSignature $PROFILE | Select-Object Path, Status, Hash
```

## Signing another script

```powershell
# the long hash is the fingerprint for the certificate
$cert = Get-Item -Path "Cert:\CurrentUser\My\ea9a1d609c091bb023c1ccd54261e4982d747047"
$status = Set-AuthenticodeSignature -FilePath "myscript.ps1" -Certificate $cert
$status.Status
```

## Wrap up!

We have seen how to prepare our environment to run powershell scripts without
relaxing the execution policy, and how to add a customization for our
environment by defining the `dotfiles` function. Now we can extend this for
additional helper scripts we could want to create in our environment.

What's the next? IMHO use a hardware key increase the security, so instead of
having a certificate in the system certificate storage, I'd rather to have
the private key stored in a cryptographic device (one ring to govern all the
realms).

Another question is, how to rotate the certificate? What happen after 5 years?

But that will be another story.

See you on the next article!
