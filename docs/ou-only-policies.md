# OU-only user and device policies

Generated 2026-10-03. These 69 policies in the core `chrome.users.*` and `chrome.devices.*` namespaces can only be applied to an organizational unit, not a group. Kiosk, managed guest, network and app-configuration policies are also OU-only; see [all-policies.md](all-policies.md).

## User settings (60)

| Policy | Category | Description |
| --- | --- | --- |
| `chrome.users.LookalikeWarningAllowlistDomains` | Chrome Safe Browsing | Suppress lookalike domain warnings on domains. |
| `chrome.users.PasswordAlert` | Chrome Safe Browsing | Password alert. |
| `chrome.users.SafeBrowsingAllowlistDomain` | Chrome Safe Browsing | Safe Browsing allowed domains. |
| `chrome.users.AutoUpdateCheckPeriodNew` | Chrome updates | Auto-update check period. |
| `chrome.users.RelaunchNotificationWithDuration` | Chrome updates | Relaunch notification. |
| `chrome.users.AutoOpen` | Content | Auto open downloaded files. |
| `chrome.users.AutoplayAllowlist` | Content | Autoplay video. |
| `chrome.users.ClientCertificates` | Content | Client certificates. |
| `chrome.users.ClipboardSettings` | Content | Clipboard. |
| `chrome.users.Cookies` | Content | Cookies. |
| `chrome.users.EnableCaptureAllowedSettings` | Content | Screen video capture allowed by sites. |
| `chrome.users.Images` | Content | Images. |
| `chrome.users.InsecureContentAllowedForUrls` | Content | Allow insecure content on these sites. |
| `chrome.users.InsecureContentBlockedForUrls` | Content | Block insecure content on these sites. |
| `chrome.users.InsecurePrivateNetworkRequestsAllowed` | Content | Requests from insecure websites to more-private network endpoints. |
| `chrome.users.JavaScriptJitSettings` | Content | JavaScript JIT. |
| `chrome.users.Javascript` | Content | JavaScript. |
| `chrome.users.LegacySameSiteCookieBehaviorEnabledForDomainList` | Content | Per-site legacy SameSite cookie behavior. |
| `chrome.users.Notifications` | Content | Notifications. |
| `chrome.users.PdfLocalFileAccessAllowedForDomains` | Content | Local file access to file:// URLs in the PDF Viewer. |
| `chrome.users.Popups` | Content | Pop-ups. |
| `chrome.users.ThirdPartyStoragePartitioningSettings` | Content | Third-party storage partitioning. |
| `chrome.users.DeskApi` | Desk API | Desk API for third-party ChromeOS desk control. |
| `chrome.users.DeviceTrustConfigurationSelection` | Device trust connector | Pub/Sub topics for device signals. |
| `chrome.users.SessionLength` | General | Maximum user session length. |
| `chrome.users.AudioCaptureAllowedUrls` | Hardware | Audio input allowed URLs. |
| `chrome.users.DefaultSensorsSetting` | Hardware | Sensors. |
| `chrome.users.FileSystemRead` | Hardware | File system read access. |
| `chrome.users.FileSystemWrite` | Hardware | File system write access. |
| `chrome.users.SerialAllowUsbDevicesForUrls` | Hardware | Web Serial API allowed devices. |
| `chrome.users.VideoCaptureAllowedUrls` | Hardware | Video input allowed URLs. |
| `chrome.users.WebHidAllowDevicesForUrls` | Hardware | WebHID API allowed devices. |
| `chrome.users.WebSerialPortAccess` | Hardware | Web Serial API. |
| `chrome.users.WebUsbAllowDevicesForUrls` | Hardware | WebUSB API allowed devices. |
| `chrome.users.WebUsbPortAccess` | Hardware | Controls which websites can ask for USB access. |
| `chrome.users.BrowserSwitcherDelayDuration` | Legacy Browser Support | Delay before launching alternative browser. |
| `chrome.users.BrowserSwitcherUrlGreylist` | Legacy Browser Support | Websites to open in either browser. |
| `chrome.users.BrowserSwitcherUrlList` | Legacy Browser Support | Websites to open in alternative browser. |
| `chrome.users.HttpAllowlist` | Network | HTTP Allowlist. |
| `chrome.users.LocalNetworkAccessIpAddressSpaceOverrides` | Network | IP address space overrides. |
| `chrome.users.LocalNetworkUrls` | Network | Local Network URLs. |
| `chrome.users.LoopbackNetworkUrls` | Network | Loopback network URLs. |
| `chrome.users.SslErrorOverrideAllowedForOrigins` | Network | SSL error override allowed domains. |
| `chrome.users.WebRtcLocalIpsAllowedUrls` | Network | WebRTC ICE candidate URLs for local IPs. |
| `chrome.users.ChromeBrowserDmtokenDeletionEnabled` | Other settings | Device Token Management. |
| `chrome.users.MaxInvalidationFetchDelay` | Other settings | Policy fetch delay. |
| `chrome.users.TabDiscardingExceptions` | Other settings | Exceptions to tab discarding. |
| `chrome.users.FetchKeepaliveDurationSecondsOnShutdown` | Power and shutdown | Keepalive duration. |
| `chrome.users.PrintJobHistoryExpirationPeriodNew` | Printing | Print job history retention period. |
| `chrome.users.CertificateTransparencyEnforcementDisabledForUrls` | Security | Allowed certificate transparency URLs. |
| `chrome.users.FileOrDirectoryPickerWithoutGestureAllowedForOrigins` | Security | File/directory picker without user gesture. |
| `chrome.users.GeolocationForUrls` | Security | Geolocation for URLs. |
| `chrome.users.IncognitoModeUrlList` | Security | Incognito mode URL restrictions. |
| `chrome.users.ScreenCaptureWithoutGestureAllowedForOrigins` | Security | Media picker without user gesture. |
| `chrome.users.SecurityTokenSessionSettings` | Security | Security token removal. |
| `chrome.users.SingleSignOn` | Security | Single sign-on. |
| `chrome.users.SiteIsolationAndroid` | Site isolation | Site isolation (Chrome on Android). |
| `chrome.users.SiteIsolationBrowser` | Site isolation | Site isolation. |
| `chrome.users.DeveloperToolsAvailabilityUrls` | User experience | Developer tools URL restrictions. |
| `chrome.users.KeepFullscreenWithoutNotificationUrlAllowList` | User experience | Fullscreen after unlock. |

## Device settings (9)

| Policy | Category | Description |
| --- | --- | --- |
| `chrome.devices.Imprivata` | Imprivata | Imprivata login screen integration. |
| `chrome.devices.ScheduledRebootDuration` | Power and shutdown | Reboot after uptime limit. |
| `chrome.devices.DeviceLoginScreenAutoSelectCertificateForUrls` | Sign-in settings | Single sign-on client certificates. |
| `chrome.devices.DeviceLoginScreenWebHidAllowDevicesForUrls` | Sign-in settings | WebHID API allowed devices on sign-in screen. |
| `chrome.devices.DeviceLoginScreenWebUsbAllowDevicesForUrls` | Sign-in settings | WebUSB API allowed devices on sign-in screen. |
| `chrome.devices.SignInRestriction` | Sign-in settings | Sign-in restriction. |
| `chrome.devices.SsoCameraPermissions` | Sign-in settings | Single sign-on camera permissions. |
| `chrome.devices.AnonymousMetricReporting` | User and device reporting | Metrics reporting. |
| `chrome.devices.EnableReportUploadFrequency` | User and device reporting | Device status report upload frequency. |
