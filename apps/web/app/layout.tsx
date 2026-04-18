import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Tariff Shock Intelligence System",
  description: "Policy shock detection, sector reaction analytics, and lag prediction dashboard.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

