"""Drop nullable properties from `required` before generating the SDK.

The ECF SSD API serialises with "ignore null values", so a property declared
`required` but nullable (e.g. EcfResponse.fileName) is simply absent from the
JSON when it is null. Generated parsers would raise KeyError on it; treating
those properties as optional makes them parse as UNSET instead.
"""

import json
import sys


def is_nullable(prop: dict) -> bool:
    kind = prop.get("type")
    if prop.get("nullable") or (isinstance(kind, list) and "null" in kind):
        return True
    return any(option.get("type") == "null" for option in prop.get("oneOf", []) + prop.get("anyOf", []))


def main(source: str, target: str) -> None:
    spec = json.load(open(source, encoding="utf-8"))
    relaxed = 0
    for schema in spec.get("components", {}).get("schemas", {}).values():
        required = schema.get("required")
        if not required:
            continue
        properties = schema.get("properties", {})
        keep = [name for name in required if not is_nullable(properties.get(name, {}))]
        relaxed += len(required) - len(keep)
        if keep:
            schema["required"] = keep
        else:
            del schema["required"]
    json.dump(spec, open(target, "w", encoding="utf-8"), indent=2)
    print(f"Relaxed {relaxed} required nullable properties")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
