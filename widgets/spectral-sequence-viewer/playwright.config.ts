import { defineConfig } from "@playwright/test";
export default defineConfig({
  testDir: "tests",
  use: {
    baseURL: "http://127.0.0.1:4180",
    launchOptions: { executablePath: process.env.CHROMIUM_PATH },
  },
  webServer: [
    { command: "python3 -m http.server 4180 --bind 127.0.0.1", port: 4180 },
    {
      command: "bun run vite --host 127.0.0.1 --port 4181 --strictPort",
      port: 4181,
    },
  ],
});
