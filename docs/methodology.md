# Methodology

## Dataset discipline

Livestream windows from the same room are strongly correlated. A random window-level split can leak the same host, background and speaking style into both training and validation. Evaluation should therefore split by room or session.

Recommended partitions:

- training rooms for model fitting;
- development rooms for iteration;
- newly collected regression rooms for version comparison;
- a sealed blind set opened only after the pipeline is frozen.

## Multimodal error analysis

The most useful analysis asks whether evidence was lost at the ASR/vision stage or ignored by the classifier. For example, a singing stream may contain:

- continuous lyrics in ASR;
- a background-music marker;
- a microphone and singing action in the visual description.

If those signals exist but the output is `chatting`, the error belongs mainly to the fusion/classification layer. Temporal aggregation cannot repair a systematic upstream error.

## Temporal semantics

- `current_activity`: direct prediction for one window.
- `stable_category`: majority label over a short recent history.
- `room_type`: category adopted only after several consecutive stable decisions.

This separation prevents a brief conversation from immediately changing a singer's long-term room type.

