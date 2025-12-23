def verify_outputs(a, b):
    same = a["stdout"] == b["stdout"] and a["exit"] == b["exit"]
    return {
        "parity": same,
        "confidence": 1.0 if same else 0.4,
        "source": a,
        "target": b
    }
