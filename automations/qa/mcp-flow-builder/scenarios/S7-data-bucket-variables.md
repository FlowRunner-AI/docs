# S7 — Data Bucket variables and references

Covered by S4 and S5 rather than built separately:
- set_data_bucket_fields returns a `references` map (`{{Data Buckets:<bucket> - <field>->}}`) that resolved in return-result, data-transformer
  args, and set_condition_parts (S4, S5).
- Reference resolution requires the bucket to be wired upstream first; otherwise `BAD_REQUEST: resolveText: could not resolve …` (S5, F-S5-3).
- Writing back into a bucket variable from a Transform Data block needs BOTH `saveToVariable` and `setResultToVariable: true`; the first alone
  is silently inert (S4, F-S4-1).
- Fields replace the whole array on each set_data_bucket_fields call (not exercised as a negative test yet — Phase 3 E10).
