#!/usr/bin/env python3
"""Validate example payloads against the sourceos-build JSON Schemas.
Uses jsonschema if available; otherwise a zero-dep structural check."""
import json, re, sys, os

PAIRS=[("schemas/sourceos/build-request.v0.1.schema.json","examples/build-request.example.json"),
       ("schemas/sourceos/build-receipt.v0.1.schema.json","examples/build-receipt.example.json")]

def fail(m): print(f"FAIL: {m}",file=sys.stderr); sys.exit(1)

def structural(schema,doc):
    for k in schema.get("required",[]):
        if k not in doc: fail(f"{doc.get('schemaVersion','?')}: missing required '{k}'")
    sv=schema.get("properties",{}).get("schemaVersion",{}).get("const")
    if sv and doc.get("schemaVersion")!=sv: fail(f"schemaVersion must be {sv}")

def main():
    try:
        import jsonschema; strict=True
    except Exception:
        strict=False
    for s,d in PAIRS:
        if not (os.path.exists(s) and os.path.exists(d)): fail(f"missing {s} or {d}")
        schema=json.load(open(s)); doc=json.load(open(d))
        if strict:
            jsonschema.Draft202012Validator.check_schema(schema)
            jsonschema.validate(doc,schema)
        else:
            structural(schema,doc)
        print(f"ok: {d} validates against {s}" + ("" if strict else " (structural; install jsonschema for strict)"))
    print("OK: sourceos-build example payloads validated")

if __name__=="__main__": raise SystemExit(main())
