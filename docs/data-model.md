# Data Model

## Core Entities

### TariffEvent

Represents one structured tariff-related event extracted from policy text or news.

- `id`
- `event_date`
- `source`
- `title`
- `summary`
- `countries`
- `goods`
- `tariff_rate`
- `event_category`
- `severity_score`
- `sectors`
- `status`

### SectorReaction

Stores event-study outputs for a sector around a tariff event.

- `event_id`
- `sector`
- `window_start`
- `window_end`
- `abnormal_return`
- `cumulative_abnormal_return`
- `volume_spike`
- `volatility_spike`
- `lag_label`

### Prediction

Model-generated estimate of downstream sector behavior.

- `event_id`
- `sector`
- `predicted_reaction_speed`
- `predicted_magnitude`
- `confidence`
- `similar_past_events`
- `model_name`

### EventEmbedding

Embedding metadata for similarity retrieval.

- `event_id`
- `vector_provider`
- `embedding_model`
- `embedding_dimension`
- `storage_reference`

### AlertSubscription

Tracks user alert preferences.

- `email`
- `sectors`
- `minimum_severity`
- `lag_labels`
- `delivery_channel`

## Data Flow Notes

- raw source payloads should be stored separately once ingestion is implemented
- normalized `TariffEvent` rows become the contract between NLP and analytics
- reaction features can be recomputed as methodology evolves
- predictions should be versioned by model and inference timestamp
