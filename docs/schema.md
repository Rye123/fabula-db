# Class
- **`name`** (string): name of the class. 
- **`sourcebook`** (string): sourcebook of this class.
- **`description`** (string): description of the class.
- **`benefits`**:
  - **`custom`** (string): *comma-separated string* of custom benefits, including if the HP/MP bonus is an optional choice.
  - **`hpBonus`** (int): bonus HP for taking the class
  - **`mpBonus`** (int): bonus MP for taking the class
  - **`ipBonus`** (int): bonus IP for taking the class
  - **`martial`**:
	- **`melee`** (bool): whether this class allows martial melee weapons
	- **`ranged`** (bool): whether this class allows martial ranged weapons
	- **`armor`** (bool): whether this class allows martial armor to be equipped
	- **`shield`** (bool): whether this class allows martial shields to be equipped
  - **`rituals`**:
	- **`arcanism`** (bool): whether this class grants Arcanism rituals
	- **`chimerism`** (bool): whether this class grants Chimerism rituals
	- **`elementalism`** (bool): whether this class grants Elementalism rituals
	- **`entropism`** (bool): whether this class grants Entropism rituals
	- **`ritualism`** (bool): whether this class grants Ritualism rituals
	- **`spiritism`** (bool): whether this class grants Spiritism  rituals

**Template**:
```json
{
    "name": "Class",
    "sourcebook": "Core Rules",
    "description": "",
    "benefits": {
        "hpBonus": 0,
        "mpBonus": 0,
        "ipBonus": 0,
        "martial": {
            "melee": false,
            "ranged": false,
            "armor": false,
            "shield": false
        },
        "rituals": {
            "arcanism": false,
            "chimerism": false,
            "elementalism": false,
            "entropism": false,
            "ritualism": false,
            "spiritism": false
        },
	    "initiateProjects": false,
		"custom": ""
    }
}
```

# Skill
- **`name`** (string): name of the skill. 
- **`sourcebook`** (string): sourcebook of this skill.
- **`description`** (string): description of the skill.
- **`requirements`** (string): a *comma-separated string* that describes the prerequisites for taking the skill (e.g. class, mastered class, known skill, known spell)
- **`isHeroicSkill`** (bool): whether or not this skill is a heroic skill.
- **`isPassiveSkill`** (bool): whether or not this skill is passive, or is active (i.e. is a potential action)
- **`maxSkillLevel`** (int): maximum skill level

# Spell
- **`name`** (string): name of the spell. 
- **`sourcebook`** (string): sourcebook of this spell.
- **`description`** (string): description of the spell. this includes the opportunity effect, if any.
- **`origin`** (string): where the spell comes from (e.g. the class, the skill, or the species if it's a Chimerist spell)
- **`mpCost`** (string): cost in MP. this is a string, as it could be `"5 x T"` or `"20"`.
- **`target`** (string): possible targets of this spell.
- **`duration`** (string): how long the spell lasts. typically, this is `"instantaneous"` or `"scene"`.

# Class-specific
## Arcana (Arcanist)
- **`name`** (string): name of the arcanum.
- **`sourcebook`** (string): sourcebook of this arcanum.
- **`description`** (string): description of the arcanum.
- **`domains`** (string): a *comma-separated string* of the domains of this arcanum
- **`mergeEffect`** (string): the effect of merging this arcanum
- **`dismissEffect`** (string): the effect of dismissing this arcanum

## Psychic Gift (Esper)
- **`name`** (string): name of the gift. 
- **`sourcebook`** (string): sourcebook of this gift.
- **`description`** (string): description of the gift.
- **`event`** (string): event that activates the gift

## Therioform (Mutant)
- **`name`** (string): name of the therioform. 
- **`sourcebook`** (string): sourcebook of this therioform.
- **`description`** (string): description of the therioform.
- **`genoclepsisSuggestions`** (string): a *comma-separated string* of the creatures that would give this therioform in Genoclepsis.

## Dances (Dancer)
- **`name`** (string): name of the dance. 
- **`sourcebook`** (string): sourcebook of this dance.
- **`description`** (string): description of the dance.
- **`duration`** (string) how long the dance lasts (e.g. until the start of your next turn, instantaneous)

## Symbols (Symbolist)
- **`name`** (string): name of the symbol. 
- **`sourcebook`** (string): sourcebook of this symbol.
- **`description`** (string): description of the symbol.

## Magiseed (Floralist)
- **`name`** (string): name of the magiseed. 
- **`sourcebook`** (string): sourcebook of this magiseed.
- **`description`** (string): description of the magiseed.
- **`effect`**: each child of this dictionary describes the effect of the seed on that turn.
  - **`turn1`** (string)
  - **`turn2`** (string)
  - **`turn3`** (string)
  - **`turn4`** (string)

