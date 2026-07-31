# IMO 2026 Run Archive

Every graded write-up and audit report behind the accompanying paper, so that the grading can be checked and regraded independently. The AutoFyn runs additionally carry their process trails; the web and provider-agent harnesses expose no trail, so those cells are write-ups and audits only.

## Layout

Runs are grouped by harness, then model, then run. Cells that were repeated three times have `run-01/`, `run-02/`, `run-03/` subdirectories; cells that ran once do not.

```
autofyn/<model>/[run-N/]problem-K/    multi-agent harness runs
claude-code/<model>/[run-N/]          provider-agent runs (Claude Code)
codex/<model>/                        provider-agent runs (Codex CLI)
zcode/<model>/[run-N/]                provider-agent runs (Zcode)
webchat/<model>/                      web interface runs
```

Every run directory holds one `audit.md`. Each records a frontier model's audit of that run, which a panel of past IMO medalists then reviewed, so the scores in it are the outcome of both stages rather than the model's verdict alone. No model audited its own run: Claude and GLM runs were audited by GPT-5.6, and GPT-5.6 runs by Claude Fable 5.

## What each run contains

**AutoFyn runs** have one directory per problem:

| path | contents |
| --- | --- |
| `problem-K/logs.jsonl` | the run's logs, one JSON object per line |
| `problem-K/current.md` | the working proof state, including the final write-up and its status |
| `problem-K/approaches/` | the distinct approaches the run explored |
| `problem-K/lemmas/` | lemmas stated and proved along the way |
| `problem-K/scratch/` | per-round subagent working notes |

Only `logs.jsonl` is present in every AutoFyn problem directory. The rest reflect what a given run actually produced, so a run that explored one approach has no `approaches/`, and four directories carry the write-up as `imo-2026-0K*.md` rather than `current.md`. `logs.jsonl` holds tool calls alone; the lifecycle events the paper's episode times are computed from are not included here, so those times cannot be recomputed from this archive.

**Provider-agent and web runs** expose no tool-call trail, so those directories hold the graded write-up for each problem as `problem-K.md`, and nothing else for the web runs. Some Claude Code and Zcode runs also kept a `code/` directory holding the verification scripts that run wrote and ran. The exception to the naming is `claude-code/claude-fable-5/`, which uses a `problem-K/` directory per problem and carries its own README describing it.

## Retrieval corpus

`corpus/` holds the fixed pre-2026 corpus the AutoFyn runs retrieve from. `past_problems_database.json` has 1026 problems from olympiads and national team selection tests between 2006 and 2025, and `past_crux_moves_database.json` has 2434 crux moves extracted from their solutions. Every entry predates the 2026 contest. The web and provider-agent harnesses carry no corpus.

## Grading

Every run was audited by a frontier model other than the one that produced it, under a fixed reviewer prompt, and a panel of past IMO medalists then reviewed those audits. Each run's audit file sits beside the write-ups it scored, so both can be read together.

Note that the audit files for the two web runs with unreturned problems report a total over gradable problems only (`28/28`, `14/14`). The paper scores an unreturned problem as zero out of 42, so the same runs appear there as 28/42 and 14/42.

## Redactions

This archive is released for double-blind review. Author names and internal infrastructure identifiers were replaced with anonymous placeholders in the recorded trails, and internal extraction tooling was omitted. Only these identifiers were changed; no tool call, audit, score, or write-up was altered.
