SKILLS = {
    "attack": {
        "name": "Attack",
        "enabled": False,
        "icon": "Attack_icon.png",
    },
    "hitpoints": {
        "name": "Hitpoints",
        "enabled": False,
        "icon": "Hitpoints_icon.png",
    },
    "mining": {
        "name": "Mining",
        "enabled": True,
        "icon": "Mining_icon.png",
        "actions": [
    {"level": 1, "action": "Rune essence", "exp": 50,"image":"Rune_essence_detail.png"},
    {"level": 1, "action": "Copper ore", "exp": 110,"image":"Copper_ore_detail.png"},
    {"level": 1, "action": "Tin ore", "exp": 110,"image":"Tin_ore_detail.png"},
    {"level": 15, "action": "Iron ore", "exp": 280,"image":"Iron_ore_detail.png"},
    {"level": 30, "action": "Coal", "exp": 420,"image":"Coal_detail.png"},
    {"level": 40, "action": "Gold ore", "exp": 510,"image":"Gold_ore_detail.png"},
    {"level": 55, "action": "Mithril", "exp": 620,"image":"Mithril_ore_detail.png"},
    {"level": 70, "action": "Adamantite ore", "exp":780,"image":"Adamantite_ore_detail.png"},
    {"level": 85, "action": "Runite ore", "exp": 3100,"image":"Runite_ore_detail.png"}
]
    },
    "strength": {
        "name": "Strength",
        "enabled": False,
        "icon": "Strenght_icon.png",
    },
    "agility": {
        "name": "Agility",
        "enabled": True,
        "icon": "Agility_icon.png",
        "actions": [
    {"level": 1, "action": "Agility ticket", "exp": 700,"image":"Agility_arena_ticket_detail.png"},
    {"level": 1, "action": "Gnome Course", "exp": 1980,"image":"Gnomeball_detail.png"},
    {"level": 40, "action": "Barbarian Course", "exp": 3100,"image":"Steel_battleaxe_detail.png"},
    {"level": 60, "action": "Werewolf Course", "exp": 3780,"image":"Stick_(item)_detail.png"},
    {"level": 70, "action": "Wilderness Course", "exp": 5500,"image":"Skull_(item)_detail.png"}
]
    },
    "smithing": {
        "name": "Smithing",
        "enabled": True,
        "icon": "Smithing_icon.png",
        "actions": [
    {"level": 1, "action": "Bronze bar", "exp": 120,"image":"Bronze_bar_detail.png"},
    {"level": 1, "action": "Bronze per 1 bar", "exp": 390,"image":"Bronze_dagger_detail.png"},
    {"level": 15, "action": "Iron bar", "exp": 260, "image":"Iron_bar_detail.png"},
    {"level": 15, "action": "Iron per 1 bar", "exp": 750, "image":"Iron_dagger_detail.png"},
    {"level": 30, "action": "Steel bar", "exp": 360, "image":"Steel_bar_detail.png"},
    {"level": 30, "action": "Steel per 1 bar", "exp": 1140, "image":"Steel_dagger_detail.png"},
    {"level": 40, "action": "Gold bar", "exp": 460, "image":"Gold_bar_detail.png"},
    {"level": 50, "action": "Mithril bar", "exp": 600, "image":"Mithril_bar_detail.png"},
    {"level": 50, "action": "Mithril per 1 bar", "exp": 1500, "image":"Mithril_dagger_detail.png"},
    {"level": 70, "action": "Adamant bar", "exp": 760, "image":"Adamantite_bar_detail.png"},
    {"level": 70, "action": "Adamantite per 1 bar", "exp": 1890, "image":"Adamant_dagger_detail.png"},
    {"level": 85, "action": "Runite bar", "exp": 1000, "image":"Runite_bar_detail.png"},
    {"level": 85, "action": "Rune per 1 bar", "exp": 2250, "image":"Rune_dagger_detail.png"}
]
    },
    "defence": {
        "name": "Defence",
        "enabled": False,
        "icon": "Defense_icon.png",
    },
    "herblore": {
        "name": "Herblore",
        "enabled": True,
        "icon": "Herblore_icon.png",
        "actions": [
    {"level": 3, "action": "Attack Potion", "exp": 200,"image":"Attack_potion(4)_detail.png"},
    {"level": 14, "action": "Strength Potion", "exp": 480,"image":"Strength_potion(4)_detail.png"},
    {"level": 25, "action": "Defence Potion", "exp": 560,"image":"Defence_potion(4)_detail.png"},
    {"level": 38, "action": "Prayer Potion", "exp": 700,"image":"Prayer_potion(4)_detail.png"},
    {"level": 46, "action": "Super Attack Potion", "exp": 840, "image":"Super_attack(4)_detail.png"},
    {"level": 55, "action": "Super Strength Potion", "exp": 1000,"image":"Super_strength(4)_detail.png"},
    {"level": 60, "action": "Super Restore Potion", "exp": 1120,"image""Super_restore(4)_detail.png"},
    {"level": 65, "action": "Super Defence potion", "exp": 1200,"image":"Super_defence(4)_detail.png"},
    {"level": 75, "action": "Ranging Potion", "exp": 1350,"image":"Ranging_potion(4)_detail.png"},
    {"level": 88, "action": "Super Combat Potion", "exp": 600,"image":"Super_combat_potion(4)_detail.png"}
]
    },
    "fishing": {
        "name": "Fishing",
        "enabled": True,
        "icon": "Fishing_icon.png",
        "actions": [
    {"level": 1, "action": "Shrimp", "exp": 110, "image":"Raw_shrimps_detail.png"},
    {"level": 20, "action": "Trout", "exp": 200, "image":"Raw_trout_detail.png"},
    {"level": 30, "action": "Salmon", "exp": 300, "image":"Raw_salmon_detail.png"},
    {"level": 40, "action": "Lobster", "exp": 440, "image":"Raw_lobster_detail.png"},
    {"level": 50, "action": "Swordfish", "exp": 650, "image":"Raw_swordfish_detail.png"},
    {"level": 60, "action": "Monkfish", "exp": 780, "image":"Raw_monkfish_detail.png"},
    {"level": 70, "action": "Shark", "exp": 1100, "image":"Raw_shark_detail.png"},
    {"level": 85, "action": "Sea Turtle", "exp": 1450, "image":"Raw_sea_turtle_detail.png"},
    {"level": 95, "action": "Manta Ray", "exp": 1900, "image":"Raw_manta_ray_detail.png"}
]
    },
    "ranged": {
        "name": "Ranged",
        "enabled": False,
        "icon": "Ranged_icon.png",
    },
    "thieving": {
        "name": "Thieving",
        "enabled": True,
        "icon": "Thieving_icon.png",
        "actions": [
    {"level": 1, "action": "Cage", "exp": 150,"image":"Chicken_cage_detail.png"},
    {"level": 10, "action": "Farmer", "exp": 800,"image":"Thief_Farmer.webp"},
    {"level": 10, "action": "Baker stall", "exp": 100,"image":"Bread_detail.png"},
    {"level": 40, "action": "Fur stall", "exp": 1800,"image":"Cowhide_detail.png"},
    {"level": 65, "action": "Silver stall", "exp": 2500,"image":"Bronze_bar_detail.png"},
    {"level": 70, "action": "Master Farmer", "exp": 1200,"image":"Thief_Master_farmer.webp"},
    {"level": 80, "action": "Spice stall", "exp": 4800,"image":"Grimy_guam_leaf_detail.png"},
    {"level": 90, "action": "Gem stall", "exp": 5800,"image":"Uncut_sapphire_detail.png"}
]
    },
    "cooking": {
        "name": "Cooking",
        "enabled": True,
        "icon": "Cooking_icon.png",
        "actions": [
    {"level": 1, "action": "Shrimp", "exp": 150, "image":"Shrimps_detail.png"},
    {"level": 20, "action": "Trout", "exp": 250, "image":"Trout_detail.png"},
    {"level": 30, "action": "Salmon", "exp": 350, "image":"Salmon_detail.png"},
    {"level": 40, "action": "Lobster", "exp": 500, "image":"Lobster_detail.png"},
    {"level": 50, "action": "Swordfish", "exp": 720, "image":"Swordfish_detail.png"},
    {"level": 60, "action": "Monkfish", "exp": 870, "image":"Monkfish_detail.png"},
    {"level": 70, "action": "Shark", "exp": 1220, "image":"Shark_detail.png"},
    {"level": 85, "action": "Sea Turtle", "exp": 1600,"image":"Sea_turtle_detail.png"},
    {"level": 95, "action": "Manta Ray", "exp": 2100, "image":"Manta_ray_detail.png"}
]
    },
    "prayer": {
        "name": "Prayer",
        "enabled": True,
        "icon": "Prayer_icon.png",
        "actions": [
    {"level": 1, "NewXp": 0, "action": "Bones", "exp": 45,"image":"Bones_detail.webp"},
    {"level": 1, "NewXp": 0, "action": "Bat bones", "exp": 85,"image":"Bat_bones_detail.webp"},
    {"level": 1, "NewXp": 0, "action": "Big bones", "exp": 150, "image":"Big_bones_detail.png"},
    {"level": 1, "NewXp": 0, "action": "Zogre bones", "exp": 265, "image":"Zogre_bones_detail.webp"},
    {"level": 1, "NewXp": 0, "action": "Jogre bones", "exp": 395,"image":"Jogre_bones_detail.png"},
    {"level": 1, "NewXp": 0, "action": "Raurg bones", "exp": 585,"image":"Raurg_bones_detail.png"},
    {"level": 1, "NewXp": 0, "action": "Dragon bones", "exp": 735,"image":"Dragon_bones_detail.png"},
    {"level": 1, "NewXp": 0, "action": "Dagannoth bones", "exp": 1050,"image":"Dagannoth_bones_detail.png"},
    {"level": 1, "NewXp": 0, "action": "Ourg bones", "exp": 1200,"image":"Ourg_bones_detail.png"},
    
]
    },
    "crafting": {
        "name": "Crafting",
        "enabled": True,
        "icon": "Crafting_icon.png",
        "actions": [
    {"level": 1, "action": "Ball of wool", "exp": 100,"image":"Ball_of_wool_detail_2.webp"},
    {"level": 10, "action": "Bow String", "exp": 50,"image":"Bow_string_detail.png"},
    {"level": 48, "action": "Unpowered orb", "exp": 240,"image":"Unpowered_orb_detail.png"},
    {"level": 50, "action": "Green d'hide", "exp": 776,"image":"Green_dragonhide_detail.png"},
    {"level": 62, "action": "Blue d'hide", "exp": 1264,"image":"Blue_dragonhide_detail.png"},
    {"level": 73, "action": "Red d'hide", "exp": 1968,"image":"Red_dragonhide_detail.png"},
    {"level": 82, "action": "Black d'hide", "exp": 2976,"image":"Black_dragonhide_detail.png"},
    {"level": 51, "action": "Water battlestaff", "exp": 450,"image":"Water_battlestaff_detail.png"},
    {"level": 56, "action": "Earth battlestaff", "exp": 500,"image":"Earth_battlestaff_detail.png"},
    {"level": 61, "action": "Fire battlestaff", "exp": 550,"image":"Fire_battlestaff_detail.png"},
    {"level": 66, "action": "Air battlestaff", "exp": 600,"image":"Air_battlestaff_detail.png"}
]
    },
    "firemaking": {
        "name": "Firemaking",
        "enabled": True,
        "icon": "Firemaking_icon.png",
         "actions": [
    {"level": 1, "action": "Logs", "exp": 160,"image""log.png"},
    {"level": 15, "action": "Oak logs", "exp": 240,"image":"oak.png"},
    {"level": 30, "action": "Willow logs", "exp": 360,"image":"willow.png"},
    {"level": 45, "action": "Maple logs", "exp": 540,"image":"maple.png"},
    {"level": 60, "action": "Yew logs", "exp": 812,"image":"yew.png"},
    {"level": 75, "action": "Magic logs", "exp": 1216,"image":"magic.webp"}   
]
    },
    "magic": {
        "name": "Magic",
        "enabled": False,
        "icon": "Magic_icon.png",
    },
    "fletching": {
        "name": "Fletching",
        "enabled": True,
        "icon": "Fletching_icon.png",
        "actions": [
    {"level": 1, "action": "Arrowshaft", "exp": 50,"image":"Arrow_shaft_detail.png"},
    {"level": 20, "action": "Oak Shortbow", "exp": 102,"image":"Oak_shortbow_(u)_detail.png"},
    {"level": 25, "action": "Oak Longbow", "exp": 150,"image":"Oak_longbow_(u)_detail.png"},
    {"level": 35, "action": "Willow Shortbow", "exp": 198,"image":"Willow_shortbow_(u)_detail.png"},
    {"level": 40, "action": "Willow Longbow", "exp": 252,"image":"Willow_longbow_(u)_detail.png"},
    {"level": 50, "action": "Maple Shortbow", "exp": 300, "image":"Maple_shortbow_(u)_detail.png"},
    {"level": 55, "action": "Maple Longbow", "exp": 348,"image":"Maple_longbow_(u)_detail.png"},
    {"level": 65, "action": "Yew Shortbow", "exp": 408,"image":"Yew_shortbow_(u)_detail.png"},
    {"level": 70, "action": "Yew Longbow", "exp": 450,"image":"Yew_longbow_(u)_detail.png"},
    {"level": 80, "action": "Magic Shortbow", "exp": 504,"image":"Magic_shortbow_(u)_detail.png"},
    {"level": 85, "action": "Magic Longbow", "exp": 552,"image":"Magic_longbow_(u)_detail.png"}
]
    },
    "woodcutting": {
        "name": "Woodcutting",
        "enabled": True,
        "icon": "Woodcutting_icon.png",
        "actions": [
                {"level": 1, "action": "Logs", "exp": 100, "image": "log.png"},
                {"level": 15, "action": "Oak logs", "exp": 165, "image": "oak.png"},
                {"level": 30, "action": "Willow logs", "exp": 285, "image": "willow.png"},
                {"level": 45, "action": "Maple logs", "exp": 425, "image": "maple.png"},
                {"level": 60, "action": "Yew logs", "exp": 735, "image": "yew.png"},
                {"level": 75, "action": "Magic logs", "exp": 1075, "image": "magic.webp"}
        ]
    },
    "runecraft": {
        "name": "Runecraft",
        "enabled": True,
        "icon": "Runecraft_icon.png",
        "actions": [
    {"level": 1, "action": "Nature Rune", "exp": 60,"image":"Nature_rune_detail.png"},
    {"level": 50, "action": "Blood Rune", "exp": 85,"image":"Blood_rune_detail.png"},
    {"level": 75, "action": "Cosmic Rune", "exp": 120,"image":"Cosmic_rune_detail.png"}
]
    },
    "slayer": {
        "name": "Slayer",
        "enabled": False,
        "icon": "Slayer_icon.png",
    },
    "farming": {
        "name": "Farming",
        "enabled": False,
        "icon": "Farming_icon.png",
    }
}





