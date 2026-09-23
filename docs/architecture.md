# Architecture

## Public demo boundary

The repository begins after media preprocessing. It accepts ASR text and visual descriptions rather than fetching or decoding a real livestream. This keeps the demo reproducible and prevents accidental publication of platform-specific media access logic.

## Components

1. `WindowInput` defines a model-neutral 15-second event.
2. `KeywordMultimodalClassifier` demonstrates transparent evidence fusion.
3. `TemporalAggregator` maintains recent predictions independently for each room.
4. `ScenePipeline` produces the current activity, stable category and long-term room type.
5. JSONL input/output makes the demo easy to connect to a future ASR or vision adapter.

## Production-oriented design lessons

- Keep collection and model inference in separate execution units.
- Keep models resident instead of reloading them for every window.
- Give every room, session, window and result stable identifiers.
- Write inference results to a durable outbox before remote delivery.
- Do not expose a database directly to the inference worker.
- Record model, prompt and taxonomy versions with every result.

These are design recommendations only. Private production contracts and deployment files are intentionally excluded.

