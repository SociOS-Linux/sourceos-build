# sourceos-build

Canonical **SourceOS build substrate**: infrastructure-as-code, build orchestration
(Tekton / Argo CD), typed `BuildRequest` / `BuildReceipt` schemas, and artifact build
receipts for the SourceOS / SociOS estate.

## Boundary (what this repo is — and is not)

**Ships:** IaC skeletons (Terraform, Ansible), CD/pipeline skeletons (Argo CD, Tekton),
JSON Schemas for build requests and receipts, example payloads, and a local schema
validation target.

**Does NOT ship:** product or runtime application code, model weights, datasets, secrets,
registry credentials, or Foreman/Katello credentials. This is not a `sourceos-platform`
monorepo and does not absorb `agentplane`, `workstation-contracts`, or `socios`
responsibilities. `socios` remains the opt-in automation/orchestration commons that
*drives* this substrate.

## Layout

| Path | Purpose |
|------|---------|
| `schemas/sourceos/` | `build-request.v0.1` and `build-receipt.v0.1` JSON Schemas |
| `examples/` | Example `BuildRequest` / `BuildReceipt` payloads (validate against the schemas) |
| `terraform/` | Terraform skeleton (build infra) |
| `ansible/` | Ansible skeleton (build host config) |
| `argocd/` | Argo CD Application skeleton |
| `tekton/` | Tekton pipeline + task skeleton |
| `tools/validate_examples.py` | Validates the example payloads against the schemas |
| `docs/adr/` | Architecture decision records |

## Validate

```
make validate
```

Offline, deterministic; no network or credentials required.
