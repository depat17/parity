import subprocess
import tempfile

def run_code(code, lang):
    if lang == "python":
        suffix = ".py"
        cmd = ["python"]
    elif lang == "javascript":
        suffix = ".js"
        cmd = ["node"]
    else:
        return {"stdout": "", "stderr": "Unsupported language", "exit": 1}

    with tempfile.NamedTemporaryFile(suffix=suffix) as f:
        f.write(code.encode())
        f.flush()
        result = subprocess.run(
            cmd + [f.name],
            capture_output=True,
            timeout=5
        )
        return {
            "stdout": result.stdout.decode(),
            "stderr": result.stderr.decode(),
            "exit": result.returncode
        }
