
# VitalRisk API — One Pager

**What it is:** A dead-simple API that converts a handful of vitals into a single risk score (0–100) and label (Low/Moderate/High). Great for triage prototypes, analytics dashboards, and teaching ML-to-API workflows.

**Why it matters:** Non-technical teams can demo risk-based flows without wrestling a full model pipeline. Engineers get a plug-and-play contract to swap in their own model later.

**How it works:** `POST /v1/risk` with { age, bmi, systolic_bp, smoker, diabetic } → returns `{ risk_index, risk_label }`.

**Safety:** Not a medical device. Educational/demo only.

**Plans:** Free tier + paid usage. On-prem available.

**Contact:** hello@yourdomain.tld
