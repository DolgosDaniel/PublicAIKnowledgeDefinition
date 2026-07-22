# Troubleshooting `paik_validate.py` errors

Common mistakes, each with a minimal broken snippet and the exact error
`python tools/paik_validate.py <paik-dir>` prints for it. Every message below is copied from a
real run against a deliberately broken fixture, not paraphrased — see
`tools/test_paik_validate.py` for the actual test cases these come from. The first is an OKF
*base-conformance* error (layer 1 — see `SPEC.md` section 2 and `tools/check_okf_conformance.py`);
the rest are PAIK-*profile* errors (layer 2, on top of a document that already satisfies OKF).

## Missing `type` field (OKF base conformance)

```yaml
# components/a.md
id: a
title: A
# no `type` field at all
```

```
ERROR: components/a.md: OKF base conformance: missing or empty 'type' field
```

Every PAIK document is also an OKF concept, and OKF's one hard requirement is a non-empty `type`.
This is the only error `tools/check_okf_conformance.py` alone will ever report — everything else
below is `paik_validate.py`-specific, on top of it.

## Duplicate id

```yaml
# components/a.md
id: dev
```
```yaml
# environments/dev.md
id: dev
```

```
ERROR: component:components/a.md, environment:environments/dev.md: duplicate id 'dev' used by 2 documents
```

Ids are unique across the *whole* project, not just within one kind — a component and an
environment can't share an id either. Rename one of them. (This `id` is PAIK's own field, not
OKF's concept identity, which is always the file's path — see `SPEC.md` section 2.)

## Reference pointing at the wrong kind of file

```yaml
# project.md
components:
  - environments/dev.md
```

```
ERROR: project.md: components entry 'environments/dev.md' points at a 'paik-environment' document, expected 'paik-component'
```

The path resolved to a real file, but that file's own `type` doesn't match what a `components`
entry is supposed to point at. Almost always a copy-paste mistake between the `components` and
`environments` arrays.

## Component missing from `project.md`

A `components/b.md` file exists on disk with `type: paik-component`, but `project.md`'s
`components` array never lists it:

```
ERROR: project.md: component 'b' (components/b.md) exists but isn't listed in this project's 'components'
```

Add it to `project.md`'s `components` array — this is the error `paik-maintain` (see
`skills/paik-maintain/SKILL.md`, rule 1) exists specifically to avoid: it's easy to create a new
component file and forget the one-line addition that makes it reachable from `project.md`.

## Unknown `depends_on` target

```yaml
depends_on:
  - some-service-that-was-renamed
```

```
ERROR: components/a.md: depends_on references unknown component id 'some-service-that-was-renamed'
```

Either the id was renamed and `depends_on` wasn't updated to match, or the dependency was never
actually created as a component. `paik_validate.py` also detects a cycle in `depends_on` the same
way (`ERROR: <paik-dir>: dependency cycle: a -> b -> a`).

## Empty `links[].kind`

```yaml
links:
  - kind: ""
```

```
ERROR: components/a.md: links[0] has an empty or missing 'kind'
```

Every `links[]` entry needs a `kind` — it's the one field that isn't optional (see SPEC.md
section 4). If you don't know what kind to use yet, that's what `paik-spec/LINKS.md` is for. Note
this `kind` is unrelated to the document's own top-level `type` field above — it's a nested,
PAIK-only field on each link.

## Reference resolving outside the `paik/` folder

```yaml
# components/a.md
environments:
  - ../../../etc/passwd
```

```
ERROR: components/a.md: environments entry '../../../etc/passwd' resolves outside the paik/ folder - PAIK documents must only reference other PAIK documents
```

A relative path with enough `../` can walk out of the `paik/` folder entirely. PAIK documents
only ever cross-reference each other (SPEC.md section 5) — if you need to point at something
outside `paik/`, that's an absolute URL in a `links[]` entry, not a relative reference.

## Invalid URI

```yaml
links:
  - kind: repository
    url: "https://exa mple.com"
```

```
ERROR: components/a.md: schema violation at ['links', 0, 'url']: 'https://exa mple.com' is not a 'uri'
```

Any field with `format: uri` in the schema (`links[].url`, `owner.ref`, `app_url`,
`health_endpoint`) is checked against RFC 3987, not just "is this a non-empty string." A missing
scheme (`https://`) or a typo in it is the most common cause.
