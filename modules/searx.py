import asyncio
import sys
import os
import msg
import yaml

async def exec(program: str, args: list[str]) -> None:
    log_error = ""
    proc = await asyncio.create_subprocess_exec(
        program,
        *args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    while True:
        if proc.stdout.at_eof() and proc.stderr.at_eof():
            break

        stderr = (await proc.stderr.readline()).decode()
        if stderr:
            log_error = log_error + "\n" + stderr

        await asyncio.sleep(0.01)

    await proc.communicate()

    if proc.returncode == 0:
        msg.info(f'{program} {" ".join(args)} exited with {proc.returncode}')
    else:
        msg.fatal_error(f'{program} {" ".join(args)} exited with {proc.returncode}\n\n\033[90m<<<LOG(stderr)>>> {log_error}')

# Config SearXNG
msg.info("Configuring SearXNG configuration file...")

with open("/etc/searxng/settings.yml", "r+") as f:
  searxng_config = yaml.safe_load(f)
  searxng_config["outgoing"]["proxies"]["all://"][0] = "socks5h://127.0.0.1:9050"
  yaml.dump(searxng_config, f)

# Start SearXNG
os.chdir('searxng/src')
asyncio.run(exec('python3', ['searx/webapp.py']))
