# Home Directory README

## SearXNG

**Source**: `/var/search/searxng`

**Settings**: `/etc/searxng/settings.yml`

**uWSGI app config**: `/etc/uwsgi/apps-available/searxng.ini`

**uWSGI socket**: `/usr/local/searxng/run/socket`

**Host mapping**: `/etc/hosts`

**Local URLs and client env**: `/home/dzack/.envrc`

### Agent permissions

The agent can use these passwordless commands:

- `sudo -n /usr/bin/systemctl reload uwsgi`
- `sudo -n /usr/sbin/nginx -t`
- `sudo -n /usr/bin/systemctl reload nginx`

The agent cannot type a sudo password. Any privileged command must already be
allowed with `NOPASSWD`.

### Files used in this setup

- `/home/dzack/web-server.conf`
  Running nginx site config for the local dashboard and local hostnames.
- `/var/www/html/index.html`
  Dashboard landing page.
- `/home/dzack/.envrc`
  Local shell env for SearXNG client URLs and related settings.
- `/etc/searxng/settings.yml`
  Instance overrides. Uses `use_default_settings: true`.
- `/var/search/searxng/searx/settings.yml`
  Default engine definitions.
- `/var/search/searxng/searx/engines/`
  Engine modules (zbmath, mathnet, hal, etc.).

### Operational notes

- The `library genesis` engine is an `xpath` engine; domain changes are handled
  by updating its `search_url` in settings.yml.
- Before changing Library Genesis domains, check the Shadow Library Uptime
  Monitor: `https://open-slum.org/`.
- Check `/home/dzack/.envrc`, `/home/dzack/web-server.conf`, and `/etc/hosts`
  for the current local SearXNG URL and hostname wiring.
- After editing `/home/dzack/.envrc`, reload the shell with `direnv reload` or
  open a new shell.

## Remote Access via Cloudflare Tunnel

**Tool**: `octunnel` (https://github.com/chabinhwang/octunnel)

**Location**: `~/go/bin/octunnel`

**Service**: systemd user service (`octunnel.service`)

### Management

```bash
# Start the tunnel
systemctl --user start octunnel

# Stop the tunnel
systemctl --user stop octunnel

# Get current URL (recorded on each start)
cat ~/.octunnel/current_url

# Check status
systemctl --user status octunnel

# Enable on boot
systemctl --user enable octunnel

# View logs
journalctl --user -u octunnel -f
```

### How it works

1. `octunnel` checks for `opencode` and `cloudflared` dependencies
2. Starts `opencode serve` on a random port (or reuses existing on 4096)
3. Launches `cloudflared` quick tunnel to expose the server
4. Outputs a `*.trycloudflare.com` URL

### Current Setup

- **Opencode server**: `http://127.0.0.1:4096`
- **Current URL**: `https://york-plumbing-key-life.trycloudflare.com`
- **URL file**: `~/.octunnel/current_url` (updated automatically on each start)
- **Security**: Unauthenticated — do not share URL publicly

### Config

- **octunnel config**: `~/.octunnel/config.json`
- **cloudflared credentials**: `~/.cloudflared/`
- **systemd service**: `~/.config/systemd/user/octunnel.service`

## OTLP Telemetry Collector

**Source**: `~/opencode-plugins/otlp-collector`

**Service**: systemd user service (`otlp-collector.service`)

**Ports**: HTTP `:4318` (OTLP/HTTP), gRPC `:4317` (OTLP/gRPC)

**Database**: `~/.local/share/otlp-collector/telemetry.db`

### Management

```bash
# Status
systemctl --user status otlp-collector.service

# Start/Stop/Restart
systemctl --user start otlp-collector.service
systemctl --user stop otlp-collector.service
systemctl --user restart otlp-collector.service

# Logs
journalctl --user -u otlp-collector.service -f

# Query database
sqlite3 ~/.local/share/otlp-collector/telemetry.db ".tables"
sqlite3 ~/.local/share/otlp-collector/telemetry.db "SELECT * FROM spans LIMIT 10;"
```

### What's sending telemetry

| Provider        | Config Location            | Status               |
| --------------- | -------------------------- | -------------------- |
| **Qwen Code**   | Default                    | ✅ Working           |
| **Gemini CLI**  | `~/.gemini/settings.json`  | ✅ Working           |
| **Claude Code** | `~/.envrc` (OTEL\_\* vars) | ✅ Working           |
| **Codex CLI**   | `~/.codex/config.toml`     | ✅ Working           |
| **OpenCode**    | N/A                        | ❌ No native support |

## OpenRouter OTLP Tunnel

**Service**: systemd user service (`openrouter-tunnel.service`)

**URL**: `https://openrouter-otlp.loca.lt/v1/traces` (fixed subdomain)

**Purpose**: Exposes OTLP collector to receive OpenRouter telemetry via tunnel.

### Management

```bash
# Status
systemctl --user status openrouter-tunnel.service

# Start/Stop/Restart
systemctl --user start openrouter-tunnel.service
systemctl --user stop openrouter-tunnel.service
systemctl --user restart openrouter-tunnel.service

# Logs (includes tunnel URL)
journalctl --user -u openrouter-tunnel.service | grep "your url"
```

### Setup

1. OpenRouter sends traces to the tunnel URL via its built-in Broadcast feature
2. Tunnel forwards to local OTLP collector on port 4318
3. Collector stores traces in SQLite database

### Configuration

- **Systemd service**: `~/.config/systemd/user/openrouter-tunnel.service`
- **Depends on**: `otlp-collector.service`
- **Restart policy**: on-failure, 10s delay
- **Tunnel**: `localtunnel` via npx, fixed subdomain `openrouter-otlp`

### Dependencies

- `otlp-collector.service` must be running first
- `npx`/`localtunnel` available via `~/.pathrc`

### Important Notes

- The subdomain is fixed (`openrouter-otlp`) so URL persists across restarts
- If the tunnel dies, OpenRouter traces are silently dropped
- Restart with `systemctl --user start openrouter-tunnel.service` to resume

## Kiro Gateway

**Source**: `~/.clones/kiro-gateway`

**Service**: systemd user service (`kiro-gateway.service`)

**Local URL**: `http://127.0.0.1:18080`

**Credentials source**: `~/.local/share/kiro-cli/data.sqlite3`

### Management

```bash
# Status
systemctl --user status kiro-gateway.service

# Start/Stop/Restart
systemctl --user start kiro-gateway.service
systemctl --user stop kiro-gateway.service
systemctl --user restart kiro-gateway.service

# Enable on login/boot for this user
systemctl --user enable kiro-gateway.service

# Logs
journalctl --user -u kiro-gateway.service -f

# Quick health check
uvx --from httpie http GET http://127.0.0.1:18080/health
```

### Configuration

- **Systemd service**: `~/.config/systemd/user/kiro-gateway.service`
- **Bind address**: `127.0.0.1:18080`
- **Runtime command**: `uv run --with-requirements requirements.txt python main.py --host 127.0.0.1 --port 18080`
- **Auth source**: `kiro-cli` SQLite database via `KIRO_CLI_DB_FILE`
- **Restart policy**: `on-failure`, 5s delay

### Operational notes

- This machine already has `loginctl show-user dzack -p Linger -> Linger=yes`, so the user service can remain running after logout.
- The service currently relies on the gateway's built-in default `PROXY_API_KEY` behavior. The OpenCode `kiro-proxy` provider is configured to match that current gateway key.
- If the local `kiro-cli` database path changes, update `KIRO_CLI_DB_FILE` in `~/.config/systemd/user/kiro-gateway.service`, then run `systemctl --user daemon-reload` and restart the service.
