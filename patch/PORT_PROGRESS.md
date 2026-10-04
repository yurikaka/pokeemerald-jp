# US-to-JP localization tracker

## Current Status — 2026-10-04

The dashboard below is historical, not the current resume queue. The completed
3326-row review and the final seven active structured-display groups are tracked
in `REMAINING_PORT_2026-10-04.md` and
`mapping_reports/remaining_display_port_2026-10-04.json`.
All seven groups now have implementations and automated validation; full GBA
gameplay validation remains pending. Deliberate save/link/keyboard exclusions
and dormant JP-only resources are not counted as untranslated active targets.

## Historical Dashboard

**Current target:** `fe570a7e5` — **IN PROGRESS; do not start a later US
commit.** The exact resume point is `patch/FE570A7E5_QUEUE.md`; work only its
first `NEXT` row. A batch is not complete until all four columns below are
complete.

| Work item | Written to JP patch | Source/ROM audit | Build | Game test | State / next gate |
| --- | ---: | ---: | --- | --- | --- |
| Main story map dialogue | 3,455 texts / 3,680 pointers | **Done** | Pass | Not run | Game-test story/NPC dialogue |
| Battle Frontier map dialogue | 706 texts / 793 pointers | Partial | Pass | Not run | **NEXT:** 138 candidates, starting at batch 199 |
| Remaining map dialogue | 444 texts / 470 pointers | Partial | Pass | Not run | 157 candidates, after Frontier maps |
| Script/map/C text batches | 6,827 texts / 7,593 pointer writes | 6,984 auto-verified; 609 tool warnings | Pass | Not run | Follow queue rows 1–4; some warnings are known static-table limits |
| Unmapped source candidates | 0 / 1,187 | Reasons recorded | N/A | N/A | Resolve dynamic provenance first (772) |
| Frontier trainer names | 300 fixed fields | 300 verified | Pass | Not run | Test a Frontier battle |
| Battle Tent trainer names | 90 fixed fields | 90 verified | Pass | Not run | Test all three tents |
| Structured/graphics-only sources | 0 / 4 work items | Classified | Pass | Not run | Need separate designs; see report 430 |
| `fe570a7e5` overall | **Partial** | **Partial** | **Pass** | **Not run** | **Not complete** |

### What the numbers mean

- **Verified (6,984):** 4,243 fixed Wokann text-label matches, 2,627 matching
  Wokann source definitions plus exact base-ROM pointer values, 64 direct
  source references, and 50 verified fragments.
- **Applied references needing review (609):** 608 have no exact Wokann symbol
  match and 1 has a symbol-name mismatch. These are already in generated
  batches, so they must be audited before any commit is called complete.
- **Unmapped candidates (1,187):** 772 dynamic placeholders, 127 no JP
  pointer, 116 ambiguous JP texts, 66 missing JP labels, 66 unsupported JP
  encoding, 32 missing Wokann source, and 8 already covered elsewhere.
- **Structured exclusions:** contest opponent records are link-transferred;
  decoration names exceed the JP inline field; the Berry Program UI is
  graphics. These are not safe text-pointer ports.

**Rules:** source: `../pokeemerald_us_chs`; JP source of truth:
`../pokeemerald_wokann_dev` `dev`; target branch: `chs-port`. Do not mark a
commit complete from a successful build, and do not commit or push this work
until it has been reviewed and game-tested.

## Commit order

| US commit | Scope | Audit state | Next evidence needed |
| --- | --- | --- | --- |
| `d9f0a6088` | Chinese renderer and fonts | Existing port; completeness not signed off | Compare engine/font behavior |
| `3755ecd46` | Main menu | Three missing wireless errors added | Review every source string and test wireless errors |
| `32221cdd3` | Birch introduction and options | Source/ROM audit complete; emulator not tested | In-game check of intro, options, and unknown Pokédex category |
| `fe570a7e5` | Main game text | **In progress — dashboard above is authoritative** | Clear applied-reference audit, then dynamic candidates, then game tests |
| `ec1ebe69d` | Map locations | Existing indexed resource | Verify table entries and UI |
| `d55760e98` | Saved default phrases | Not audited | Confirm intentional English behavior |
| `8410fbfd5` | Rival/family terms | Not audited | Compare exact source and JP display |
| `93f16ebcd` | Starter categories | Not audited | Compare exact source and JP display |
| `08c6fdcc7` | Expansion translations | Partial generated batches 400–405 | Audit all files and unresolved entries |
| `5a5f15b4d` | In-game trade names | Not audited | Confirm original JP data remains unchanged |
| `8a58666f0` | Structured translations | Partial generated batch 399 | Audit remaining source resources |
| `6a0f4bf95` | Battle placeholders | Not audited | Compare battle placeholder behavior |
| `62fd354eb` | Party item action | Not audited | Check party text and display |
| `958f8d8dd` | Whiteout message | Not audited | Check exact message and control codes |
| `2c4fdf145` | Default box names | Not audited | Confirm original JP data remains unchanged |
| `1ee117fa1` | Missed text and type names | Not audited | Compare all changed files |
| `c4dca0448` | Expansion alignment | Partial report-only batch 407 | Resolve report-only entry and compare all changed files |
| `8ce2542e1` | Easy Chat defaults | Not audited | Confirm intentional English behavior |
| `557bca791` | Abandoned Ship keys | Not audited | Check exact item descriptions |
| `31154fc10` | Frontier Brain quotes | Batch 198 generated | Review mapping and in-game display |
| `cab40ddee` | Expansion translations | Partial generated batch 406 | Audit all files and unresolved entries |
| `4bebb77e2` | Remaining no-menu option | Not audited | Check exact text and reference |
| `2e2ff18c5` | Interface graphics | Not audited | Compare image assets and JP screens |
| `4027385ac` | Item name length | Not audited | Check JP capacity changes |
| `424aa86fe` | Remaining interface graphics | Not audited | Compare image assets and JP screens |
| `74d783b8a` | Title graphics | Existing port; completeness not signed off | Compare source art and JP screen |
| `31dc97496` | Easy Chat controls | Not audited | Compare graphics/control behavior |
| `75cf6108b` | Contest results tilemap | Not audited | Compare tilemap and JP screen |

## Next actions for `fe570a7e5`

Follow `patch/FE570A7E5_QUEUE.md` in order. It is the authoritative task
state and records the exact report, cursor, and acceptance criterion for the
next item; the dashboard only summarizes it.
