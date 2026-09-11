# Architecture

RANOpt uses a layered architecture so data ingestion, KPI analytics, diagnosis, and optimization can evolve independently.

```text
                 +----------------------+
                 |   RAN Data Sources   |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 | Validation / Loading |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 | Preprocessing        |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 | KPI Analytics         |
                 | Health Scoring        |
                 +----------+-----------+
                            |
              future        |
       +--------------------+--------------------+
       v                    v                    v
   Monitoring           Diagnosis           Optimization
                                              |
                                              v
                                      Graph / RL layer
```

Phase 1 deliberately implements only the first four layers. Future phases will extend the pipeline without coupling optimization code to raw data ingestion.
