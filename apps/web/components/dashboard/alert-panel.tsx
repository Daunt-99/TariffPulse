import type { AlertSubscription } from "@tariff-shock/shared";

export function AlertPanel({ alerts }: { alerts: AlertSubscription[] }) {
  return (
    <section className="dashboard-panel p-6">
      <div className="flex items-center justify-between">
        <div>
          <p className="eyebrow">Alert Panel</p>
          <h2 className="mt-2 text-xl font-semibold">Current subscriptions</h2>
        </div>
        <span className="rounded-full border border-accent/30 px-3 py-1 text-xs text-accent">
          {alerts.length} active
        </span>
      </div>
      <div className="mt-6 space-y-3">
        {alerts.map((alert) => (
          <div key={alert.id} className="rounded-2xl border border-line/80 bg-slate-950/20 p-4">
            <p className="text-sm font-medium text-white">{alert.email}</p>
            <p className="mt-1 text-sm text-slate-400">
              Severity ≥ {alert.minimumSeverity.toFixed(2)} • {alert.deliveryChannel}
            </p>
            <div className="mt-3 flex flex-wrap gap-2">
              {alert.sectors.map((sector) => (
                <span key={sector} className="rounded-full bg-white/5 px-3 py-1 text-xs text-slate-300">
                  {sector}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

