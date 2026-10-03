#!/usr/bin/env python3
"""Build the Markdown docs and clean CSV from a GAM `print chromeschemas` export.

Usage: python3 scripts/generate.py [path/to/raw_schemas.csv]
"""
import csv
import datetime
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data" / "raw_schemas.csv"
TODAY = datetime.date.today().isoformat()

# Display order and labels for the policy areas
AREAS = [
    ("chrome.users", "User settings"),
    ("chrome.users.apps", "App install and pinning"),
    ("chrome.users.appsconfig", "App configuration"),
    ("chrome.devices", "Device settings"),
    ("chrome.devices.kiosk", "Kiosk"),
    ("chrome.devices.managedguest", "Managed guest sessions"),
    ("chrome.networks", "Networks"),
    ("chrome.printers", "Printers"),
    ("chrome.printservers", "Print servers"),
]
AREA_PREFIXES = {prefix for prefix, _ in AREAS}


def area_of(schema):
    parts = schema.split(".")
    for n in (3, 2):
        prefix = ".".join(parts[:n])
        if prefix in AREA_PREFIXES and len(parts) > n:
            return prefix
    return ".".join(parts[:2])


def md_escape(text):
    return text.replace("|", "\\|").replace("\n", " ").strip()


def load():
    policies = []
    with open(RAW, newline="") as f:
        for r in csv.DictReader(f):
            targets = [r[k] for k in r if re.fullmatch(r"validTargetResources\.\d+", k) and r[k]]
            policies.append({
                "schemaName": r["schemaName"],
                "area": area_of(r["schemaName"]),
                "category": r.get("categoryTitle", ""),
                "groupScopable": "GROUP" in targets,
                "targets": "+".join(sorted(targets)),
                "lifecycle": r.get("policyApiLifecycle.policyApiLifecycleStage", ""),
                "description": r.get("policyDescription", ""),
            })
    return sorted(policies, key=lambda p: p["schemaName"].lower())


def write_csv(policies):
    with open(ROOT / "data" / "chrome_policy_targeting.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["schemaName", "area", "category", "groupScopable", "targets", "lifecycleStage", "description"])
        for p in policies:
            w.writerow([p["schemaName"], p["area"], p["category"], "YES" if p["groupScopable"] else "NO",
                        p["targets"], p["lifecycle"], p["description"]])


def summary_table(policies):
    counts = defaultdict(lambda: [0, 0])
    for p in policies:
        counts[p["area"]][0 if p["groupScopable"] else 1] += 1
    lines = ["| Area | Namespace | Group-scopable | OU only | % group |", "| --- | --- | ---: | ---: | ---: |"]
    for prefix, label in AREAS:
        if prefix not in counts:
            continue
        g, o = counts.pop(prefix)
        lines.append(f"| {label} | `{prefix}.*` | {g} | {o} | {round(g / (g + o) * 100)}% |")
    for prefix, (g, o) in sorted(counts.items()):
        lines.append(f"| Other | `{prefix}.*` | {g} | {o} | {round(g / (g + o) * 100)}% |")
    total_g = sum(p["groupScopable"] for p in policies)
    lines.append(f"| **Total** | | **{total_g}** | **{len(policies) - total_g}** | "
                 f"**{round(total_g / len(policies) * 100)}%** |")
    return "\n".join(lines), total_g


def policy_table(rows, with_scope=True):
    head = "| Policy | Category | Group? | Description |" if with_scope else "| Policy | Category | Description |"
    sep = "| --- | --- | :---: | --- |" if with_scope else "| --- | --- | --- |"
    lines = [head, sep]
    for p in rows:
        cells = [f"`{p['schemaName']}`", md_escape(p["category"])]
        if with_scope:
            cells.append("Yes" if p["groupScopable"] else "No")
        cells.append(md_escape(p["description"]))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def write_all_policies(policies):
    out = [f"# All Chrome policies by area\n",
           f"Generated {TODAY} from the Chrome Policy API via GAM. "
           f"\"Group?\" = Yes when the policy's `validTargetResources` includes `GROUP`.\n"]
    labels = dict(AREAS)
    for prefix in [a for a, _ in AREAS] + sorted({p["area"] for p in policies} - AREA_PREFIXES):
        rows = [p for p in policies if p["area"] == prefix]
        if not rows:
            continue
        g = sum(p["groupScopable"] for p in rows)
        out.append(f"## {labels.get(prefix, prefix)} (`{prefix}.*`)\n")
        out.append(f"{g} of {len(rows)} group-scopable.\n")
        out.append(policy_table(rows) + "\n")
    (ROOT / "docs" / "all-policies.md").write_text("\n".join(out))


def write_ou_only(policies):
    core = [p for p in policies if not p["groupScopable"] and p["area"] in ("chrome.users", "chrome.devices")]
    out = [f"# OU-only user and device policies\n",
           f"Generated {TODAY}. These {len(core)} policies in the core `chrome.users.*` and `chrome.devices.*` "
           f"namespaces can only be applied to an organizational unit, not a group. Kiosk, managed guest, "
           f"network and app-configuration policies are also OU-only; see [all-policies.md](all-policies.md).\n"]
    for prefix, label in (("chrome.users", "User settings"), ("chrome.devices", "Device settings")):
        rows = sorted((p for p in core if p["area"] == prefix), key=lambda p: (p["category"], p["schemaName"]))
        out.append(f"## {label} ({len(rows)})\n")
        out.append(policy_table(rows, with_scope=False) + "\n")
    (ROOT / "docs" / "ou-only-policies.md").write_text("\n".join(out))


def update_readme(policies):
    table, total_g = summary_table(policies)
    block = (f"<!-- BEGIN SUMMARY -->\n"
             f"As of {TODAY}: **{total_g} of {len(policies)}** Chrome policies can be scoped to a group; "
             f"**{len(policies) - total_g}** are OU-only.\n\n{table}\n<!-- END SUMMARY -->")
    readme = ROOT / "README.md"
    text = readme.read_text()
    text = re.sub(r"<!-- BEGIN SUMMARY -->.*?<!-- END SUMMARY -->", lambda _: block, text, flags=re.S)
    readme.write_text(text)


def main():
    policies = load()
    write_csv(policies)
    write_all_policies(policies)
    write_ou_only(policies)
    update_readme(policies)
    print(f"{len(policies)} policies processed")


if __name__ == "__main__":
    main()
