# LTE Failover Watchdog – Huawei B818-263

## 📌 What is this script?

This is a simple monitoring script for my Huawei B818-263 LTE router, which acts as a backup internet source (failover WAN) in my network.

The script:
- checks whether the router has an active connection to a BTS (cell tower),
- if a problem is detected:
  - performs a router reboot,
  - sends me an email notification informing me about the incident.

The goal is simple:

Ensure that the backup connection is always ready to take over when the primary connection fails.

## 🤔 Why did I create this script?

This script was created after a real-world incident.

During a fiber outage, I discovered that:
- the LTE router had lost its connection to the BTS,
- everything returned to normal only after a manual reboot.

The failover configuration on the router worked correctly —
but the backup internet source itself was not actually ready to handle traffic.

I wanted:
- automatic detection of LTE connection loss,
- automatic recovery (router reboot),
- email notification whenever this happens.

This script acts as a lightweight watchdog for my backup connection.

## 🏗 My setup

My network infrastructure looks like this:
- Primary WAN: `Fiber connection`
- Edge router: `Ubiquiti EdgeRouter ER-12`
- Secondary WAN (failover): `Huawei B818-263 with a SIM card and LTE data plan`

Huawei B818 details:
- Modem hardware version: `WL3B818M`
- Modem firmware version: `11.0.1.1(H220SP1C983)`
- WebUI version: `WEBUI 11.0.1.1(W2SP3C7201)`

The B818 is connected to the ER-12 as a secondary WAN interface configured in failover mode.

## 🚀 How to run the script

### 1️⃣ Install dependencies
```bash
pip3 install huawei-lte-api python-dotenv
```

### 2️⃣ Configure .env file
```bash
cp .env.example .env
```

Fill in the following variables:

| Variable       | Description                                  |
| -------------- | -------------------------------------------- |
| `ROUTER_IP`    | IP address of the B818 router                |
| `ROUTER_USER`  | Router username (default: `admin`)           |
| `ROUTER_PASS`  | Router admin password                        |
| `MAX_FAILURES` | Number of failed checks before reboot        |
| `STATE_FILE`   | Path to the state file (e.g. `./state.json`) |
| `SMTP_HOST`    | SMTP server hostname                         |
| `SMTP_PORT`    | SMTP server port                             |
| `SMTP_USER`    | SMTP username                                |
| `SMTP_PASS`    | SMTP password                                |
| `EMAIL_FROM`   | Sender email address                         |
| `EMAIL_TO`     | Recipient email address                      |

### 3️⃣ Run the script

```bash
python3 main.py
```

### Or download the zipapp package and run it

Instead of installing dependencies manually, you can download the prebuilt `zipapp` package from the repository releases.

Run it with:

```bash
python3 lte_failover.pyz
```

The application still requires a properly configured .env file in the same directory.

This method is recommended for production or scheduled environments (cron, TrueNAS, etc.).

### Recommended usage:
- run via cron,
- schedule via TrueNAS task scheduler,
- or use any system task scheduler for periodic execution.

## 🔄 Distribution & “CI/CD”

This project intentionally does not use traditional CI/CD.

And yes — that’s on purpose 😉

The script:
- is delivered as a zipapp ready to run,
- includes a .env file,
- comes with a small update-check script that verifies whether a newer version is available in the repository.

Updates:
- are executed automatically at night,
- at a scheduled time,
- using a separate update script.

Why this approach?
- simplicity,
- minimal overhead,
- no need for full CI/CD for a private infrastructure tool,
- controlled update timing (no surprise updates during the day).

This is a pragmatic solution built for a real need.

## 🔮 Next steps

This script will be refined to a “near-production” level, but:

❗ I do not plan to actively develop it further.

Why?

In the future, this functionality will become part of a larger service I plan to build.
That service will include additional features (such as SMS notifications and extended monitoring).

Maintaining two separate tools that serve the same purpose does not make sense.

For now, the goal of this script is simple:

> Provide stability and readiness of the LTE failover connection so it can reliably take over when the primary fiber connection fails.

## ⚠️ Disclaimer

This tool was created as a practical solution to a specific infrastructure issue.
It is not intended to be an enterprise-grade LTE monitoring framework.

If it helps someone else — great.