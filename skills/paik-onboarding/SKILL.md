---
name: paik-onboarding
description: Read an entire paik/ folder (project, components, environments) and produce a concise onboarding brief for a new team member or a new AI agent joining the project. Use when the user asks to "onboard me to this project", "summarize this project", or "what do I need to know to work on X".
---

# paik-onboarding

Turn a `paik/` folder into a short onboarding brief for a new human or AI contributor.

## Steps

1. Start at `paik/project.md` — read the description, `owner`, and `links`, then follow
   `components`/`environments` (that's the point of PAIK: two hops from `project.md` reaches
   everything).
2. Read `component*.md`: for each component, note its `component_type`, `owner`, `environments`,
   `depends_on`, and group its `links[]` by `kind` (repository, api, ticketing, secrets,
   external-service, ...). Do not fetch any link's live content unless the user specifically
   asks — this brief is about orientation, not a data dump.
3. Read `environments/*.md`: list each environment's `purpose` and how to reach it (`app_url`,
   `access`) — skip listing raw database connection strings, `databases[].host_ref` is a pointer,
   never a credential.
4. Collect every `owner` object you saw in steps 1-3 into a "who owns what" list. Do not invent
   or look up individual people — `owner` is deliberately just `{ name, ref? }`; point to `ref`
   if the user wants the org's actual directory.
5. Write the brief in this shape:
   - One paragraph: what the project is and its current `lifecycle`.
   - "Where things live": one line per `links[]` kind seen across the project (ticketing, wiki,
     ...), with the URL.
   - "Components": one line per component — what it is, its repository/API links, what it
     depends on.
   - "Who owns what": component/environment → owner name → `ref` if present.
   - "Environments": title → purpose → URL.
   - "Secrets": note where each `kind: secrets` link points, explicitly noting none are embedded
     here.
6. Keep the whole brief short enough to read in under two minutes — it's a map to the real
   systems, not a replacement for reading them.
