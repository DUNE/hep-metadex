# AGENTS.md

- For OpenSpec propose/apply/verify/archive workflows, use the local `openspec-git-discipline` skill to enforce proposal commits before apply and merge-before-archive discipline.
- When crafting intent prompts for `/opsx-new` or `/opsx-propose`, follow `docs/intent-prompt-guidelines.md`: name the receiving actor, state observable rules, and declare deliverables and out-of-scope so the pipeline does not generate unrequested implementation.
- Commits use conventional format and reference their change's issue number as a `(#N)` subject suffix; `Closes #N` appears only in the archive-phase commit, since one issue tracks a change's entire lifecycle.
