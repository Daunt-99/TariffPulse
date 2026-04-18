import type { Prediction, TariffEvent } from "@tariff-shock/shared";

export function ShockProfile({
  event,
  predictions,
}: {
  event: TariffEvent;
  predictions: Prediction[];
}) {
  const relevantPredictions = predictions.filter((item) => item.eventId === event.id);

  return (
    <section className="dashboard-panel p-6">
      <p className="eyebrow">Shock Profile</p>
      <h2 className="mt-2 text-xl font-semibold">{event.title}</h2>
      <p className="mt-3 text-sm leading-6 text-slate-300">{event.summary}</p>
      <div className="mt-6 grid gap-4 md:grid-cols-2">
        <div className="rounded-2xl border border-line/80 bg-slate-950/20 p-4">
          <p className="text-sm text-slate-400">Event metadata</p>
          <ul className="mt-3 space-y-2 text-sm text-slate-200">
            <li>Countries: {event.countries.join(", ")}</li>
            <li>Goods: {event.goods.join(", ")}</li>
            <li>Category: {event.eventCategory}</li>
            <li>Tariff rate: {event.tariffRate ?? "TBD"}%</li>
          </ul>
        </div>
        <div className="rounded-2xl border border-line/80 bg-slate-950/20 p-4">
          <p className="text-sm text-slate-400">Model outlook</p>
          <div className="mt-3 space-y-3">
            {relevantPredictions.map((prediction) => (
              <div key={prediction.id} className="flex items-center justify-between rounded-xl bg-white/5 px-3 py-2">
                <span>{prediction.sector}</span>
                <span className="capitalize text-accent">{prediction.predictedReactionSpeed}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

