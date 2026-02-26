#!/usr/bin/env python3
from helpers.configHelper import get_config
from helpers.mailHelper import send_email
from helpers.routerHelper import reboot_router, is_connected_to_bts
from helpers.stateHelper import load_state, save_state

config = get_config()

# =====================
# MAIN
# =====================
def main():
    state = load_state(config)

    if is_connected_to_bts(config):
        state["failures"] = 0
        save_state(state, config)
        print("✅ BTS connection OK")
        return

    # failure
    state["failures"] += 1
    save_state(state, config)

    print(f"❌ BTS connection lost ({state['failures']}/{config['max_failures']})")

    if state["failures"] >= config["max_failures"]:
        print("🔁 Restarting router...")
        reboot_router(config)

        send_email(
            subject="LTE Router Has Been Restarted",
            body=f"Router {config['router_ip']} lost connection to the BTS and was automatically restarted.",
            config=config,
        )

        state["failures"] = 0
        save_state(state, config)

if __name__ == "__main__":
    main()