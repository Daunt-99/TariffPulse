import type { AlertSubscription, Prediction, SectorReaction, TariffEvent } from "@tariff-shock/shared";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";
const USE_MOCKS = process.env.NEXT_PUBLIC_USE_MOCKS === "true";

async function request<T>(path: string, fallback: T): Promise<T> {
  if (USE_MOCKS) {
    return fallback;
  }

  try {
    const response = await fetch(`${API_BASE_URL}${path}`, { next: { revalidate: 60 } });
    if (!response.ok) {
      return fallback;
    }
    return (await response.json()) as T;
  } catch {
    return fallback;
  }
}

function adaptEvent(payload: Record<string, unknown>): TariffEvent {
  return {
    id: String(payload.id),
    title: String(payload.title),
    summary: String(payload.summary),
    source: String(payload.source),
    eventDate: String(payload.event_date ?? payload.eventDate),
    countries: (payload.countries as string[]) ?? [],
    goods: (payload.goods as string[]) ?? [],
    tariffRate: (payload.tariff_rate as number | null) ?? (payload.tariffRate as number | null),
    eventCategory: String(payload.event_category ?? payload.eventCategory) as TariffEvent["eventCategory"],
    severityScore: Number(payload.severity_score ?? payload.severityScore),
    sectors: (payload.sectors as TariffEvent["sectors"]) ?? [],
    status: String(payload.status) as TariffEvent["status"],
  };
}

function adaptReaction(payload: Record<string, unknown>): SectorReaction {
  return {
    id: String(payload.id),
    eventId: String(payload.event_id ?? payload.eventId),
    sector: String(payload.sector) as SectorReaction["sector"],
    abnormalReturn: Number(payload.abnormal_return ?? payload.abnormalReturn),
    cumulativeAbnormalReturn: Number(
      payload.cumulative_abnormal_return ?? payload.cumulativeAbnormalReturn,
    ),
    volumeSpike: Number(payload.volume_spike ?? payload.volumeSpike),
    volatilitySpike: Number(payload.volatility_spike ?? payload.volatilitySpike),
    lagLabel: String(payload.lag_label ?? payload.lagLabel) as SectorReaction["lagLabel"],
  };
}

function adaptPrediction(payload: Record<string, unknown>): Prediction {
  return {
    id: String(payload.id),
    eventId: String(payload.event_id ?? payload.eventId),
    sector: String(payload.sector) as Prediction["sector"],
    predictedReactionSpeed: String(
      payload.predicted_reaction_speed ?? payload.predictedReactionSpeed,
    ) as Prediction["predictedReactionSpeed"],
    predictedMagnitude: Number(payload.predicted_magnitude ?? payload.predictedMagnitude),
    confidence: Number(payload.confidence),
    similarPastEvents: (payload.similar_past_events ??
      payload.similarPastEvents ??
      []) as Prediction["similarPastEvents"],
    modelName: String(payload.model_name ?? payload.modelName),
  };
}

function adaptAlert(payload: Record<string, unknown>): AlertSubscription {
  return {
    id: String(payload.id),
    email: String(payload.email),
    sectors: (payload.sectors as AlertSubscription["sectors"]) ?? [],
    minimumSeverity: Number(payload.minimum_severity ?? payload.minimumSeverity),
    lagLabels: (payload.lag_labels ?? payload.lagLabels ?? []) as AlertSubscription["lagLabels"],
    deliveryChannel: String(
      payload.delivery_channel ?? payload.deliveryChannel,
    ) as AlertSubscription["deliveryChannel"],
  };
}

export async function getDashboardData() {
  const [{ default: events }, { default: reactions }, { default: predictions }, { default: alerts }] =
    await Promise.all([
      import("@/lib/mocks/events.json"),
      import("@/lib/mocks/reactions.json"),
      import("@/lib/mocks/predictions.json"),
      import("@/lib/mocks/alerts.json"),
    ]);

  const [apiEvents, apiReactions, apiPredictions, apiAlerts] = await Promise.all([
    request<Record<string, unknown>[]>(
      "/api/v1/events",
      events as unknown as Record<string, unknown>[],
    ),
    request<Record<string, unknown>[]>(
      "/api/v1/reactions",
      reactions as unknown as Record<string, unknown>[],
    ),
    request<Record<string, unknown>[]>(
      "/api/v1/predictions",
      predictions as unknown as Record<string, unknown>[],
    ),
    request<Record<string, unknown>[]>(
      "/api/v1/alerts",
      alerts as unknown as Record<string, unknown>[],
    ),
  ]);

  return {
    events: apiEvents.map(adaptEvent),
    reactions: apiReactions.map(adaptReaction),
    predictions: apiPredictions.map(adaptPrediction),
    alerts: apiAlerts.map(adaptAlert),
  };
}
