-- Operations Metrics Dashboard Query Pack
-- Use these queries to build an AI/BI dashboard in Databricks SQL.
-- Primary dataset source for quality metrics:
--   <gold_catalog>.<fact_schema>.pipeline_observability_metrics

-- 1) KPI Snapshot (latest metric date)
SELECT
  metric_date,
  rows_loaded,
  rows_after_quality_filters,
  rows_quarantined,
  quarantine_rate_pct,
  avg_trip_minutes
FROM pipeline_observability_metrics
ORDER BY metric_date DESC
LIMIT 1;

-- 2) Throughput Trend
SELECT
  metric_date,
  rows_loaded,
  rows_after_quality_filters
FROM pipeline_observability_metrics
ORDER BY metric_date;

-- 3) Quarantine Trend
SELECT
  metric_date,
  rows_quarantined,
  quarantine_rate_pct
FROM pipeline_observability_metrics
ORDER BY metric_date;

-- 4) Optional runtime/cost metrics table for Free-tier demos
-- Create this once, then upsert metrics from a lightweight notebook or SQL task.
-- CREATE TABLE IF NOT EXISTS demo_operational_metrics (
--   metric_date DATE,
--   avg_runtime_minutes DOUBLE,
--   est_cost_usd DOUBLE,
--   successful_runs BIGINT,
--   failed_runs BIGINT
-- );

-- Runtime/Cost Trend (optional)
-- SELECT
--   metric_date,
--   avg_runtime_minutes,
--   est_cost_usd,
--   successful_runs,
--   failed_runs
-- FROM demo_operational_metrics
-- ORDER BY metric_date;

-- 5) Optional system-table based cost query (requires Unity Catalog system tables)
-- SELECT
--   usage_date AS metric_date,
--   sum(usage_quantity) AS usage_quantity,
--   any_value(usage_unit) AS usage_unit
-- FROM system.billing.usage
-- WHERE usage_date >= current_date() - INTERVAL 30 DAYS
-- GROUP BY usage_date
-- ORDER BY usage_date;
