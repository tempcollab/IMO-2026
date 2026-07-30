# IMO 2026 Run Archive

Full process trails for every run reported in the accompanying paper, so that the grading can be checked and regraded independently.

## Layout

Runs are grouped by harness, then model, then run:

```
autofyn/<model>/[run-N/]problem-K/    multi-agent harness runs
claude-code/<model>/run-N/            provider-agent runs (Claude Code)
codex/<model>/                        provider-agent runs (Codex CLI)
zcode/<model>/                        provider-agent runs (Zcode)
webchat/<model>/                      web interface runs
```

Each AutoFyn problem directory holds three files:

| file | contents |
| --- | --- |
| `logs.jsonl` | tool calls, one JSON object per line |
| `events.jsonl` | lifecycle and control events, including the submitted prompt |
| `run.json` | run-level summary (model, timings, token and cost totals) |

Provider-agent and web runs expose no tool-call trail, so those directories hold the graded write-up (`problem-K.md`) and the audit that scored it.

## Grading

Every run was audited by a frontier model other than the one that produced it, under a fixed reviewer prompt. A panel of past IMO medalists then reviewed those audits. Each run directory contains its audit file alongside the write-up it scored, so both can be read together.

## Timing

Episode lengths in the paper are computed from `logs.jsonl` timestamps as the span from the first to the last event, minus every idle gap longer than five minutes. The gap subtraction removes time spent waiting on a rate-limit reset. The `duration_minutes` field in `run.json` is not the source for those figures.

## Redactions

This archive is released for double-blind review. Author names and internal infrastructure identifiers were replaced with anonymous placeholders in the recorded trails, and internal extraction tooling was omitted. Only these identifiers were changed; no tool call, audit, score, or write-up was altered.
