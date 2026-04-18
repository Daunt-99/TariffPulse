import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}", "./lib/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#07111F",
        panel: "#0D1727",
        line: "#1D314A",
        accent: "#7CF7D4",
        signal: "#8EA7FF",
        warning: "#F59E0B",
        danger: "#FB7185",
      },
      boxShadow: {
        panel: "0 24px 60px rgba(0, 0, 0, 0.35)",
      },
      backgroundImage: {
        "radial-grid":
          "radial-gradient(circle at top, rgba(124, 247, 212, 0.18), transparent 32%), linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px)",
      },
      backgroundSize: {
        "radial-grid": "auto, 32px 32px, 32px 32px",
      },
    },
  },
  plugins: [],
};

export default config;

