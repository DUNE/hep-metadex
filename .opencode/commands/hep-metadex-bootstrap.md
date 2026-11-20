---
description: "Bootstrap this repository onto the hep-metadex OpenSpec workflow - verify prerequisites, install the kit from a versioned release, declare the store reference, and reach doctor green (kit command)"
---

Bootstrap an uninitialized repository onto the hep-metadex OpenSpec workflow: prerequisites verified, workflow scaffolding installed from a versioned kit release, the store reference declared, `openspec doctor` green. Works for greenfield and brownfield repositories alike; in a brownfield repository the bootstrap is additive - existing code and CI stay untouched. This command automates the documented agent-assisted bootstrap prompt in the hep-metadex store's `docs/setup.md`; that prompt remains the fallback and the specification, and drift between the two is a defect.

**Input**: Optionally pin a kit release version after `/hep-metadex-bootstrap` (e.g. `/hep-metadex-bootstrap 1.1.0` or `v1.1.0` - a leading `v` is tolerated and stripped). If omitted, the bootstrap installs the latest kit release. If the argument is anything other than a bare semver, stop with a usage report naming the expected form and install nothing.
**Provided arguments**: $ARGUMENTS

**Steps**

1. **Resolve the release and verify the prerequisites - nothing is written to this repository yet**

   Resolve the release from `$ARGUMENTS` first: absent means the latest release; a bare semver (leading `v` stripped) pins that release; anything else stops the run now with a usage report naming the expected form (`/hep-metadex-bootstrap [v]<major.minor.patch>`, absent meaning latest).

   All fetches and verification happen in a temporary directory; the first write to this repository is step 2's `openspec init`, and it happens only after every check below passes. Check in order - any failure stops the run with a clear report naming the missing prerequisite, before anything is written to this repository:

   - The OpenSpec CLI is installed:
     ```bash
     openspec --version
     ```
   - The hep-metadex store is registered on this machine - `openspec store list` must show hep-metadex and its checkout location.
   - The chosen release's artifacts are fetched into the temporary directory - `SHA256SUMS` first, then every file it lists (the bundle `metadex-kit-<version>.tar.gz` and the command asset `hep-metadex-bootstrap.md`):
     ```bash
     tmp="$(mktemp -d)"
     cd "$tmp"
     base="https://github.com/DUNE/hep-metadex/releases/latest/download"      # latest release
     base="https://github.com/DUNE/hep-metadex/releases/download/v<version>"  # pinned release
     curl -fsSL -o SHA256SUMS "$base/SHA256SUMS"
     for f in $(awk '{print $2}' SHA256SUMS); do curl -fsSL -o "$f" "$base/$f"; done
     ```
     Set exactly one `base` per the resolved release. For the latest release the bundle's file name - and so its version - comes from `SHA256SUMS`; for a pinned release it is the argument. A failed fetch (unknown release or asset) stops the run.
   - The fetched artifacts verify - both assets present, checksums green; on any mismatch stop the run and never extract:
     ```bash
     sha256sum -c SHA256SUMS
     ```
   - The release's declared CLI pin, read from the verified bundle itself - never a hardcoded version - compared against the installed CLI:
     ```bash
     tar -xzf metadex-kit-<version>.tar.gz .metadex-kit
     ```
     The bundled `.metadex-kit` carries `version:` (the kit about to be installed) and `cli:` (the CLI it requires). An installed CLI older than `cli:` stops the run with a report naming the required version.
   - **Version skew - warn and proceed, never stop.** The command file you are executing may come from a different release than the kit being installed: the documented one-liner fetches the command from the latest release, and the install may pin another, or `latest` may have moved on since the fetch. The skew is usually cosmetic. If you can locate the file you are executing (the one-liner saves it as `hep-metadex-bootstrap.md` in the working directory), compare it with the fetched command asset: identical bytes mean no skew, different bytes mean skew. Either way proceed, and record both versions in the final report - the release the executed file came from, and the installed kit's `version:`. If you cannot locate the file, say so in the report rather than claiming a version for it.

2. **Initialize OpenSpec - the first write to this repository**

   From the repository root, run `openspec init` for the agent tools this repository uses:
   ```bash
   openspec init --tools <tools>
   ```
   Infer the tools from the agent harness in use (an OpenCode harness means `--tools opencode`); ask the maintainer if unclear. Every prerequisite has passed; this is the first repository write.

3. **Install the verified kit bundle**

   From the repository root, extract the verified bundle from step 1's temporary directory - it lays the kit out at its natural repository paths:
   ```bash
   tar -xzf "<tmp>/metadex-kit-<version>.tar.gz"
   ```
   - If this repository already has an `AGENTS.md`, capture its content before extracting, then merge the kit's pointers into that content after extraction - the manifest marks `AGENTS.md` merge-guidance; never overwrite the file.
   - The `.metadex-kit` provenance stamp and `KIT-MANIFEST.yaml` arrive via the bundle - never author them separately.

4. **Handle the host-conditional GitHub files**

   Determine this repository's host from its remote (`git remote get-url origin`); ask the maintainer if there is no remote.
   - **GitHub-hosted:** confirm the extraction placed `.github/workflows/validate.yml` and `.github/ISSUE_TEMPLATE/` (`change.yml` and `config.yml`).
   - **Hosted elsewhere:** remove the extracted `.github/` kit files and wire the equivalent gate into this repository's own CI - run `openspec validate --all` over all specs and changes and fail unless it reports `valid: true`, with the OpenSpec CLI pinned to the version the release declares - and replicate the intent-material issue convention in this host's own issue tracker (see the bundled `docs/intent-prompt-guidelines.md`). No implementation is provided for other hosts.

5. **Author `openspec/config.yaml`**

   If the repository already had an `openspec/config.yaml` before this bootstrap (brownfield), add ONLY the `references:` block naming the store id and remote - preserve the existing schema, context, and rules untouched. Otherwise write the full file:

   ```yaml
   schema: intent-driven

   # Read-only connection to the hep-metadex OpenSpec Store.
   # Never add a `store:` line: this repository keeps its own specs and changes.
   references:
     - id: hep-metadex
       remote: https://github.com/DUNE/hep-metadex.git

   context: |
     Tech stack: <the real stack; ask the maintainer if unknown>
     Domain: <this repository's real domain>

   rules:
     proposal:
       - Must use grill-me skill
       - Must use adversarial-authoring skill
       - Must use glossary skill
     design:
       - Must use c4-diagrams skill
       - Must use glossary skill
     adr:
       - Must use architectural-decision-records skill
     specs:
       - Must use spec-as-source skill
     tasks:
       - Must use spec-as-source skill
   ```

   The `context:` block must describe this repository's REAL domain and tech stack - ask the maintainer if unknown, and never ship the placeholders. NEVER add a `store:` line, in either case: this repository keeps its own specs and changes.

6. **Iterate `openspec doctor` to green**

   ```bash
   openspec doctor
   ```
   Iterate until it reports the hep-metadex reference as ok, fixing what it names. The final output goes in the report.

**Output**

The bootstrap ends with a report to the maintainer:
- **What was installed** - the kit's files at their natural paths (scaffolding, `AGENTS.md` merged or fresh, the `.metadex-kit` provenance stamp, `KIT-MANIFEST.yaml`), the host-conditional outcome (GitHub files confirmed, or removed with the equivalents named), and the authored or references-extended `openspec/config.yaml`.
- **The versions in play** - the release the executed command file came from, the installed kit's `version:`, the installed `openspec --version`, and any version-skew warning from step 1.
- **The final `openspec doctor` output**, with the hep-metadex reference reported ok.
- **Brownfield note** - if this repository already has code, confirm its real tech stack is recorded in `context:` and note that the first change here should be characterization-first: spec the seams as they behave today, agents drafting from the code, before anything changes (see `docs/setup.md` in the hep-metadex store).

**Guardrails**
- Create no change and write no implementation code in this repository - nothing lands in `openspec/changes/` and no source file is authored; the first change is the maintainer's to start.
- Never add a `store:` line to `openspec/config.yaml` - this repository keeps its own specs and changes, and common-capability improvements route to the store explicitly with `--store hep-metadex`.
- Never overwrite an existing `openspec/config.yaml` beyond adding the `references:` block; in a repository that already has code, the existing code and CI stay untouched.
- Stop on any prerequisite failure or checksum mismatch - the CLI missing or older than the release's declared pin, the store unregistered, an unparseable version argument, a failed fetch, a failed `sha256sum -c` - with a clear report naming what is missing, before anything is written to this repository.
- Install the kit only from a versioned kit release with checksum verification - latest by default, an explicit pin accepted - never from the registered store checkout.
- `AGENTS.md` is merge-guidance: merge the kit's pointers, never overwrite. The `.metadex-kit` provenance stamp and `KIT-MANIFEST.yaml` arrive via the bundle - never author them.
- The documented agent-assisted bootstrap prompt in the hep-metadex store's `docs/setup.md` remains the fallback and the specification this command automates - mirror it; do not invent steps beyond it.
