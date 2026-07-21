---
name: paik-onboarding
description: Read an entire paik/ folder (project, systems, components, teams, environments, configuration) and produce a concise onboarding brief for a new team member or a new AI agent joining the project. Use when the user asks to "onboard me to this project", "summarize this project", or "what do I need to know to work on X".
---

# paik-onboarding

Turn a `paik/` folder into a short onboarding brief for a new human or AI contributor.

## Steps

1. Start at `paik/project.md` — read the description and status, then follow every link it
   contains (that's the point of PAIK: two hops from `project.md` reaches everything).
2. Read every `systems/*.md` file: note the type, base URL, and identifier (project key / space
   key / API id / repo URL) for each. Do not fetch their live content unless the user specifically
   asks — this brief is about orientation, not a data dump.
3. Read `component*.md`: for each component, note its repo/API/environments/configuration and
   what it depends on — this is the actual service graph.
4. Read `team*.md`: summarize what each team owns (cross-reference the `owner_ref` fields you
   saw in steps 2-3 back to team names here). Do not invent or look up individual people — team
   docs deliberately don't list names; point to `directory_ref` if the user wants that.
5. Read `environments/*.md`: list each environment's purpose and how to reach it (`app_url`,
   access restrictions) — skip listing raw database connection strings, there aren't any to list
   per the PAIK secrets policy.
6. Read `configuration*.md`: summarize the tool and where it's managed, not any actual secret.
7. Write the brief in this shape:
   - One paragraph: what the project is and its current status.
   - "Where things live": one line per system with a link.
   - "Components": one line per component — what it is, its repo/API, what it depends on.
   - "Who owns what": component/system → owning team → chat/on-call link.
   - "Environments": name → purpose → URL.
   - "Config & secrets": tool + location, explicitly noting none are embedded here.
8. Keep the whole brief short enough to read in under two minutes — it's a map to the real
   systems, not a replacement for reading them.
