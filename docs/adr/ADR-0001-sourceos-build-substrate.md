# ADR-0001: SourceOS build substrate as a dedicated repository

- Status: Accepted
- Date: 2026-07-04

## Context

SourceOS risked becoming a monolithic platform repository. Build orchestration, IaC,
and artifact provenance were being scattered into product repositories and into `socios`.

## Decision

Create `SociOS-Linux/sourceos-build` as the canonical build substrate. It holds:

- IaC (Terraform, Ansible) for build infrastructure;
- build orchestration (Tekton pipelines, Argo CD applications);
- typed `BuildRequest` / `BuildReceipt` schemas and example payloads;
- artifact build receipts (provenance + digests).

`socios` remains the opt-in automation/orchestration commons that *drives* this substrate
by emitting `BuildRequest` documents and consuming `BuildReceipt` documents.

## Consequences

- Clear separation: substrate (this repo) vs. orchestration commons (`socios`) vs. product/runtime.
- Downstream consumers depend on stable schema paths (`schemas/sourceos/*.schema.json`).
- No secrets, credentials, weights, or datasets are committed here.

## Non-goals

- Recreating a `sourceos-platform` monorepo.
- Moving `agentplane`, `workstation-contracts`, or `socios` responsibilities into this repo.
