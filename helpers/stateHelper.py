import os
import json

# =====================
# STATE MANAGEMENT
# =====================
def load_state(config):
    if not os.path.exists(config["state_file"]):
        return {"failures": 0}
    with open(config["state_file"], "r") as f:
        return json.load(f)

def save_state(state, config):
    with open(config["state_file"], "w") as f:
        json.dump(state, f)