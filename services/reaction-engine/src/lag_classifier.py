def classify_lag(
    day_zero_abnormal_return: float,
    early_window_car: float,
    full_window_car: float,
    threshold: float = 0.75,
) -> str:
    """
    Label sector timing using simple heuristics.

    immediate: large day-0 move and early window dominates
    lagged: small day-0 move but larger cumulative effect later
    mixed: both immediate and extended reaction signals exist
    neutral: no meaningful reaction detected
    """
    if abs(day_zero_abnormal_return) >= threshold and abs(early_window_car) >= threshold:
        return "immediate" if abs(full_window_car - early_window_car) < threshold else "mixed"
    if abs(day_zero_abnormal_return) < threshold and abs(full_window_car) >= threshold:
        return "lagged"
    if abs(full_window_car) < threshold:
        return "neutral"
    return "mixed"

