# ML Plan

## Objectives

Predict for each affected sector:

- reaction speed
- reaction magnitude
- confidence
- similar past events

## Baseline

The initial model is XGBoost over engineered tabular features such as:

- tariff rate change
- severity score
- sector exposure scores
- macro context
- pre-event volatility and volume
- source credibility and policy-vs-news indicators

## Primary Model

Temporal Fusion Transformer will later model:

- sector return histories
- cross-sector dependencies
- macro sequences
- event timing and text-derived covariates

## Retrieval Layer

Similarity search will complement model predictions by returning historically analogous events with:

- source similarity
- goods overlap
- country overlap
- sector exposure overlap
- embedding similarity

## Evaluation

- classification metrics for lag labels
- regression metrics for magnitude
- calibration quality for confidence
- retrieval precision for similar events
