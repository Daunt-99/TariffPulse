import type { TariffEvent } from "@tariff-shock/shared";

export function EventTimeline({ events }: { events: TariffEvent[] }) {
  return (
    <section className="dashboard-panel p-6">
      <div className="flex items-center justify-between">
        <div>
          <p className="eyebrow">Event Timeline</p>
          <h2 className="mt-2 text-xl font-semibold">Structured tariff events</h2>
        </div>
        <p className="text-sm text-slate-400">{events.length} tracked events</p>
      </div>
      <div className="mt-6 space-y-4">
        {events.map((event) => (
          <article key={event.id} className="rounded-2xl border border-line/80 bg-slate-950/20 p-4">
            <div className="flex flex-col gap-3 lg:flex-row lg:items-start lg:justify-between">
              <div>
                <p className="text-sm text-slate-400">{event.eventDate}</p>
                <h3 className="mt-1 text-lg font-medium">{event.title}</h3>
                <p className="mt-2 max-w-3xl text-sm leading-6 text-slate-300">{event.summary}</p>
              </div>
              <div className="rounded-2xl bg-danger/10 px-4 py-2 text-sm text-danger">
                Severity {event.severityScore.toFixed(2)}
              </div>
            </div>
            <div className="mt-4 flex flex-wrap gap-2">
              {event.sectors.map((sector) => (
                <span key={sector} className="rounded-full border border-signal/40 px-3 py-1 text-xs text-signal">
                  {sector}
                </span>
              ))}
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}

