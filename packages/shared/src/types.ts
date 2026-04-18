import type { EVENT_CATEGORIES, LAG_LABELS, SECTORS } from "./constants";

export type Sector = (typeof SECTORS)[number];
export type EventCategory = (typeof EVENT_CATEGORIES)[number];
export type LagLabel = (typeof LAG_LABELS)[number];

export interface TariffEvent {
  id: string;
  title: string;
  summary: string;
  source: string;
  eventDate: string;
  countries: string[];
  goods: string[];
  tariffRate?: number | null;
  eventCategory: EventCategory;
  severityScore: number;
  sectors: Sector[];
  status: "draft" | "confirmed" | "archived";
}

export interface SectorReaction {
  id: string;
  eventId: string;
  sector: Sector;
  abnormalReturn: number;
  cumulativeAbnormalReturn: number;
  volumeSpike: number;
  volatilitySpike: number;
  lagLabel: LagLabel;
}

export interface Prediction {
  id: string;
  eventId: string;
  sector: Sector;
  predictedReactionSpeed: LagLabel;
  predictedMagnitude: number;
  confidence: number;
  similarPastEvents: string[];
  modelName: string;
}

export interface AlertSubscription {
  id: string;
  email: string;
  sectors: Sector[];
  minimumSeverity: number;
  lagLabels: LagLabel[];
  deliveryChannel: "email" | "slack" | "webhook";
}

