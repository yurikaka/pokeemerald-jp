# Mapping Audit

## Pending High-Confidence Reference Ports

The following `mapped_only` references were found by exact context matching.
Their Chinese text definitions already exist in the named batches; only the
reference writes remain to be added after targeted gameplay testing.

| Batch | Source symbol | Japanese reference | Japanese text |
| --- | --- | --- | --- |
| 029_rustborocity | RustboroCity_Text_BrendanIWontGoEasy | 0x081E7407 | 0x081E8109 |
| 029_rustborocity | RustboroCity_Text_BrendanMrBrineyHint | 0x081E7436 | 0x081E813D |
| 029_rustborocity | RustboroCity_Text_BrendanNoConfidenceInPokemon | 0x081E73FD | 0x081E80CD |
| 029_rustborocity | RustboroCity_Text_BrendanWantToBattle | 0x081E73EA | 0x081E80EC |
| 029_rustborocity | RustboroCity_Text_MayMrBrineyHint | 0x081E731A | 0x081E7F9B |
| 029_rustborocity | RustboroCity_Text_TrainersSchoolSign | 0x081EBC1D | 0x081EC371 |
| 044_slateportcity_harbor | SlateportCity_Harbor_Text_PleaseBoardFerry | 0x08209AA2 | 0x08209CAA |
| 044_slateportcity_harbor | SlateportCity_Harbor_Text_WhereWouldYouLikeToGo | 0x08209A95 | 0x08209CBE |
| 047_slateportcity_oceanicmuseum_2f | SlateportCity_OceanicMuseum_2F_Text_RemindsMeOfAbandonedShip | 0x08205D45 | 0x082060D2 |
| 047_slateportcity_oceanicmuseum_2f | SlateportCity_OceanicMuseum_2F_Text_SSAnneReplica | 0x08205D18 | 0x08205FE8 |
| 053_mauvillecity_gym | MauvilleCity_Gym_Text_AngeloPostBattle | 0x080ADE1F | 0x082020D9 |
| 053_mauvillecity_gym | MauvilleCity_Gym_Text_ExplainDynamoBadgeTakeThis | 0x0828E9C3 | 0x08202231 |
| 061_route110_trickhouseentrance | Route110_TrickHouseEntrance_Text_ConcealedInPlanter | 0x0823CBE5 | 0x0823D30C |
| 084_route111 | Route111_Text_RouteSign113 | 0x0824366E | 0x082642C3 |
| 152_mossdeepcity_gym | MossdeepCity_Gym_Text_GymStatueCertified | 0x081AA3A9 | 0x082101DD |
| 152_mossdeepcity_gym | MossdeepCity_Gym_Text_GymStatueCertified | 0x081AA4C3 | 0x082101DD |
| 152_mossdeepcity_gym | MossdeepCity_Gym_Text_TateAndLizaPostRematch | 0x081E3ED5 | 0x08210300 |
| 152_mossdeepcity_gym | MossdeepCity_Gym_Text_TateAndLizaPostRematch | 0x081E402D | 0x08210300 |
| 172_party | gText_Accuracy2 | 0x0802F760 | 0x082D2900 |

## Rejected Low-Confidence Candidates

The remaining `mapped_only` references use regional-delta, nearest-anchor, or
ordinal inference. Do not add them without an independent code or gameplay
audit.

## Expected-Only Audit

The regenerated reports contain 955 existing references that were not
reconstructed. Keep all of them unchanged for now.

- 925 have no reconstructed reference for their source symbol, primarily in
  code- and table-driven battle, party, and bag text.
- 13 have another exact-context reference for the same source symbol.
- 17 have another inferred reference for the same source symbol.
- No expected-only target points outside the Japanese ROM or to a 16-byte
  all-zero region.

An expected-only reference is therefore an unresolved audit item, not evidence
that the existing reference should be removed.
