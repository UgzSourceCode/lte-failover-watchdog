from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection


# =====================
# ROUTER CHECK
# =====================
def is_connected_to_bts(config):
    try:
        with Connection(
                f"http://{config['router_ip']}",
                username=config["router_user"],
                password=config["router_pass"]
        ) as conn:

            client = Client(conn)

            register = client.net.register()
            signal = client.device.signal()

            mode = register.get("Mode")
            rsrp = signal.get("rsrp")

            print("Network mode:", mode)
            print("RSRP (signal strength):", rsrp)

            if mode != "0":
                return False

            if not rsrp:
                return False

            return True

    except Exception as e:
        print("Router communication error:", e)
        return False

# =====================
# REBOOT
# =====================
def reboot_router(config):
    with Connection(
            f"http://{config['router_ip']}",
            username=config["router_user"],
            password=config["router_pass"]
    ) as conn:
        client = Client(conn)
        client.device.reboot()