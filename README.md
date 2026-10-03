# Chrome policy targeting: group vs OU

Which Chrome management policies in Google Workspace can be applied to a **group**, and which only to an **organizational unit (OU)**.

Every policy schema in the [Chrome Policy API](https://developers.google.com/chrome/policy/reference/rest/v1/customers.policySchemas) has a `validTargetResources` field. It lists `ORG_UNIT`, or `ORG_UNIT` and `GROUP`. This repo pulls that field with [GAM7](https://github.com/GAM-team/GAM) and turns it into readable tables.

## Summary

<!-- BEGIN SUMMARY -->
As of 2026-10-03: **728 of 1229** Chrome policies can be scoped to a group; **501** are OU-only.

| Area | Namespace | Group-scopable | OU only | % group |
| --- | --- | ---: | ---: | ---: |
| User settings | `chrome.users.*` | 588 | 60 | 91% |
| App install and pinning | `chrome.users.apps.*` | 15 | 0 | 100% |
| App configuration | `chrome.users.appsconfig.*` | 0 | 26 | 0% |
| Device settings | `chrome.devices.*` | 119 | 9 | 93% |
| Kiosk | `chrome.devices.kiosk.*` | 0 | 54 | 0% |
| Managed guest sessions | `chrome.devices.managedguest.*` | 0 | 331 | 0% |
| Networks | `chrome.networks.*` | 0 | 21 | 0% |
| Printers | `chrome.printers.*` | 3 | 0 | 100% |
| Print servers | `chrome.printservers.*` | 3 | 0 | 100% |
| **Total** | | **728** | **501** | **59%** |
<!-- END SUMMARY -->

## Key takeaways

- **Kiosk, managed guest, network and app-configuration policies are all OU-only.**
- **Most core user and device settings support groups.** The exceptions are mostly per-site lists, such as Cookies, JavaScript, Pop-ups, camera and mic allowed URLs, WebUSB/HID/Serial, and Safe Browsing allowlists. A few duration settings (SessionLength, RelaunchNotification, AutoUpdateCheckPeriod) and sign-in screen device settings are also OU-only.
- **Group policies apply to users, not devices.** They apply to the signed-in sessions of the group's members.
- **Groups take priority over OUs.** When a user gets the same policy from both, the group setting wins. Among several targeted groups, the Admin Console's group priority order decides.
- **The API and the Admin Console can differ.** These lists reflect what the Policy API accepts, and they normally match the Admin Console. If the two ever disagree, the console is the final word.

## Contents

| File | What it is |
| --- | --- |
| [docs/ou-only-policies.md](docs/ou-only-policies.md) | The core user and device policies that cannot target a group |
| [docs/all-policies.md](docs/all-policies.md) | Every policy, grouped by area, with group support and description |
| [data/chrome_policy_targeting.csv](data/chrome_policy_targeting.csv) | The same data as a CSV, for filtering in a spreadsheet |
| [scripts/refresh.sh](scripts/refresh.sh) | Pulls fresh data with GAM and regenerates everything |
| [scripts/generate.py](scripts/generate.py) | Builds the Markdown and CSV from a GAM export |

## Check a single policy

```sh
gam info chromeschema chrome.users.Cookies fields validtargetresources
```

## Refresh the data

This needs GAM7, authorized for a Workspace tenant with Chrome management, and Python 3.

```sh
./scripts/refresh.sh
```

The raw GAM export (`data/raw_schemas.csv`) contains your customer ID, so it is git-ignored. Only the cleaned CSV is committed.
