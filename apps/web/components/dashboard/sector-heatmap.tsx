import type { Prediction, SectorReaction } from "@tariff-shock/shared";

import { formatPct } from "@/lib/utils";

export function SectorHeatmap({
  reactions,
  predictions,
}: {
  reactions: SectorReaction[];
  predictions: Prediction[];
}) {
  const rows = reactions.map((reaction) => {
    const prediction = predictions.find(
      (candidate) => candidate.eventId === reaction.eventId && candidate.sector === reaction.sector,
    );
    return { reaction, prediction };
  });

  return (
    <section className="dashboard-panel p-6">
      <p className="eyebrow">Sector Heatmap</p>
      <h2 className="mt-2 text-xl font-semibold">Observed stress versus modeled speed</h2>
      <div className="mt-6 overflow-hidden rounded-2xl border border-line/70">
        <table className="min-w-full divide-y divide-line/70 text-left text-sm">
          <thead className="bg-slate-950/30 text-slate-400">
            <tr>
              <th className="px-4 py-3 font-medium">Sector</th>
              <th className="px-4 py-3 font-medium">AR</th>
              <th className="px-4 py-3 font-medium">CAR</th>
              <th className="px-4 py-3 font-medium">Observed</th>
              <th className="px-4 py-3 font-medium">Predicted</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-line/60">
            {rows.map(({ reaction, prediction }) => (
              <tr key={reaction.id}>
                <td className="px-4 py-3 text-white">{reaction.sector}</td>
                <td className="px-4 py-3">{formatPct(reaction.abnormalReturn)}</td>
                <td className="px-4 py-3">{formatPct(reaction.cumulativeAbnormalReturn)}</td>
                <td className="px-4 py-3 capitalize text-warning">{reaction.lagLabel}</td>
                <td className="px-4 py-3 capitalize text-accent">
                  {prediction?.predictedReactionSpeed ?? "pending"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

