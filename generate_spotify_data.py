import csv
import random
import datetime

random.seed(42)

artists_genres = [
    ("The Weeknd", "R&B / Pop", [
        ("Blinding Lights", "After Hours", "Album Track", "Non-Explicit", 3900000000, 93, 171, 51, 73, 33),
        ("Starboy", "Starboy", "Album Track", "Explicit", 3100000000, 91, 186, 68, 59, 49),
        ("Save Your Tears", "After Hours", "Album Track", "Non-Explicit", 2300000000, 90, 118, 68, 83, 64),
        ("Die For You", "Starboy", "Album Track", "Non-Explicit", 2150000000, 89, 134, 58, 53, 51),
        ("Creepin'", "Heroes & Villains", "Single", "Explicit", 1580000000, 88, 120, 72, 62, 17),
        ("One Of The Girls", "The Idol Episode 4", "Single", "Explicit", 1320000000, 89, 117, 52, 64, 20),
        ("In Your Eyes", "After Hours", "Album Track", "Non-Explicit", 1120000000, 84, 100, 67, 72, 72),
        ("Heartless", "After Hours", "Single", "Explicit", 980000000, 82, 170, 53, 73, 20),
        ("Take My Breath", "Dawn FM", "Single", "Non-Explicit", 740000000, 80, 121, 70, 74, 53),
        ("Sacrifice", "Dawn FM", "Album Track", "Non-Explicit", 620000000, 78, 122, 74, 79, 90),
    ]),
    ("Taylor Swift", "Pop", [
        ("Cruel Summer", "Lover", "Album Track", "Non-Explicit", 2400000000, 96, 170, 55, 70, 56),
        ("Anti-Hero", "Midnights", "Album Track", "Non-Explicit", 1650000000, 92, 97, 64, 64, 53),
        ("Blank Space", "1989 (Taylor's Version)", "Album Track", "Non-Explicit", 1850000000, 90, 96, 76, 70, 58),
        ("Cardigan", "folklore", "Album Track", "Non-Explicit", 1250000000, 87, 130, 61, 58, 55),
        ("Fortnight", "The Tortured Poets Department", "Single", "Explicit", 890000000, 91, 96, 68, 39, 26),
        ("I Can Do It With a Broken Heart", "The Tortured Poets Department", "Album Track", "Explicit", 780000000, 88, 130, 70, 75, 66),
        ("Style", "1989 (Taylor's Version)", "Album Track", "Non-Explicit", 1380000000, 89, 95, 59, 79, 49),
        ("Karma", "Midnights", "Single", "Explicit", 920000000, 86, 90, 64, 62, 10),
        ("Lavender Haze", "Midnights", "Album Track", "Explicit", 810000000, 85, 97, 73, 44, 10),
        ("All Too Well (10 Minute Version)", "Red (Taylor's Version)", "Album Track", "Explicit", 790000000, 86, 93, 63, 63, 21),
    ]),
    ("Drake", "Hip-Hop / Rap", [
        ("One Dance", "Views", "Album Track", "Non-Explicit", 3100000000, 90, 104, 79, 63, 37),
        ("God's Plan", "Scorpion", "Album Track", "Explicit", 2500000000, 88, 77, 75, 45, 36),
        ("Passionfruit", "More Life", "Album Track", "Explicit", 1750000000, 87, 112, 80, 46, 36),
        ("Rich Flex", "Her Loss", "Single", "Explicit", 1200000000, 86, 144, 76, 52, 41),
        ("IDGAF", "For All The Dogs", "Album Track", "Explicit", 950000000, 88, 137, 66, 68, 15),
        ("First Person Shooter", "For All The Dogs", "Album Track", "Explicit", 820000000, 85, 164, 47, 64, 25),
        ("Search & Rescue", "Single", "Single", "Explicit", 690000000, 83, 142, 82, 44, 54),
        ("Slime You Out", "For All The Dogs", "Single", "Explicit", 510000000, 80, 89, 48, 48, 11),
        ("Jimmy Cooks", "Honestly, Nevermind", "Album Track", "Explicit", 980000000, 85, 166, 53, 67, 37),
        ("Knife Talk", "Certified Lover Boy", "Album Track", "Explicit", 1100000000, 85, 146, 85, 42, 21),
    ]),
    ("Ed Sheeran", "Pop / Acoustic", [
        ("Shape of You", "Divide", "Album Track", "Non-Explicit", 3800000000, 92, 96, 83, 65, 93),
        ("Perfect", "Divide", "Album Track", "Non-Explicit", 2950000000, 89, 95, 60, 45, 17),
        ("Bad Habits", "=", "Single", "Non-Explicit", 1850000000, 87, 126, 81, 89, 59),
        ("Shivers", "=", "Album Track", "Non-Explicit", 1600000000, 86, 141, 79, 86, 82),
        ("Eyes Closed", "-", "Single", "Non-Explicit", 620000000, 82, 107, 78, 50, 43),
        ("Thinking Out Loud", "x", "Album Track", "Non-Explicit", 2500000000, 87, 79, 78, 45, 59),
        ("Photograph", "x", "Album Track", "Non-Explicit", 2400000000, 86, 108, 61, 38, 20),
        ("Castle on the Hill", "Divide", "Album Track", "Non-Explicit", 1450000000, 83, 135, 46, 83, 47),
        ("Overpass Graffiti", "=", "Album Track", "Non-Explicit", 510000000, 79, 176, 67, 82, 79),
        ("Celestial", "Single", "Single", "Non-Explicit", 420000000, 77, 123, 59, 85, 48),
    ]),
    ("Bad Bunny", "Latin / Reggaeton", [
        ("Me Porto Bonito", "Un Verano Sin Ti", "Album Track", "Explicit", 1950000000, 90, 92, 91, 71, 42),
        ("Tití Me Preguntó", "Un Verano Sin Ti", "Album Track", "Explicit", 1750000000, 89, 107, 65, 72, 19),
        ("Ojitos Lindos", "Un Verano Sin Ti", "Album Track", "Non-Explicit", 1680000000, 88, 80, 65, 69, 37),
        ("Dakiti", "El Último Tour Del Mundo", "Album Track", "Explicit", 1900000000, 88, 110, 73, 57, 55),
        ("Monaco", "Nadie Sabe Lo Que Va a Pasar Mañana", "Single", "Explicit", 980000000, 89, 140, 79, 63, 38),
        ("Where She Goes", "Single", "Single", "Explicit", 890000000, 86, 144, 65, 80, 23),
        ("Perro Negro", "Nadie Sabe Lo Que Va a Pasar Mañana", "Album Track", "Explicit", 820000000, 87, 96, 91, 78, 44),
        ("Efecto", "Un Verano Sin Ti", "Album Track", "Explicit", 1400000000, 86, 98, 80, 48, 41),
        ("Moscow Mule", "Un Verano Sin Ti", "Album Track", "Explicit", 1320000000, 85, 100, 80, 67, 33),
        ("Yonaguni", "Single", "Single", "Explicit", 1450000000, 85, 180, 64, 65, 44),
    ]),
    ("Dua Lipa", "Dance / Pop", [
        ("Don't Start Now", "Future Nostalgia", "Album Track", "Non-Explicit", 2600000000, 89, 124, 79, 79, 68),
        ("Levitating", "Future Nostalgia", "Album Track", "Non-Explicit", 2150000000, 89, 103, 70, 83, 91),
        ("New Rules", "Dua Lipa", "Album Track", "Non-Explicit", 2050000000, 86, 116, 76, 70, 61),
        ("Dance the Night", "Barbie The Album", "Single", "Non-Explicit", 1250000000, 91, 110, 67, 85, 78),
        ("Houdini", "Radical Optimism", "Single", "Non-Explicit", 710000000, 88, 117, 72, 88, 89),
        ("Training Season", "Radical Optimism", "Single", "Non-Explicit", 530000000, 86, 123, 73, 89, 68),
        ("Physical", "Future Nostalgia", "Album Track", "Non-Explicit", 980000000, 83, 147, 65, 84, 75),
        ("Break My Heart", "Future Nostalgia", "Album Track", "Non-Explicit", 1120000000, 83, 113, 73, 73, 47),
        ("Love Again", "Future Nostalgia", "Album Track", "Non-Explicit", 780000000, 81, 116, 66, 67, 44),
        ("Illusion", "Radical Optimism", "Album Track", "Non-Explicit", 410000000, 82, 125, 70, 87, 81),
    ]),
    ("Billie Eilish", "Alternative / Pop", [
        ("bad guy", "WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?", "Album Track", "Non-Explicit", 2600000000, 88, 135, 70, 43, 56),
        ("lovely", "Single", "Single", "Non-Explicit", 2800000000, 89, 115, 35, 30, 12),
        ("Birds of a Feather", "HIT ME HARD AND SOFT", "Album Track", "Non-Explicit", 1450000000, 97, 105, 75, 51, 44),
        ("Lunch", "HIT ME HARD AND SOFT", "Single", "Explicit", 890000000, 93, 125, 82, 67, 81),
        ("What Was I Made For?", "Barbie The Album", "Single", "Non-Explicit", 1180000000, 91, 120, 44, 23, 14),
        ("Happier Than Ever", "Happier Than Ever", "Album Track", "Explicit", 1350000000, 87, 81, 33, 23, 12),
        ("everything i wanted", "Single", "Single", "Non-Explicit", 1600000000, 85, 120, 70, 23, 24),
        ("when the party's over", "WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?", "Album Track", "Non-Explicit", 1750000000, 85, 83, 31, 11, 20),
        ("ocean eyes", "Don't Smile at Me", "Single", "Non-Explicit", 1520000000, 84, 145, 51, 37, 16),
        ("Chihiro", "HIT ME HARD AND SOFT", "Album Track", "Non-Explicit", 620000000, 89, 110, 62, 59, 31),
    ]),
    ("Post Malone", "Hip-Hop / Pop", [
        ("Sunflower", "Spider-Man: Into the Spider-Verse", "Single", "Non-Explicit", 3300000000, 91, 90, 76, 48, 91),
        ("Circles", "Hollywood's Bleeding", "Album Track", "Non-Explicit", 2450000000, 89, 120, 69, 76, 55),
        ("rockstar", "beerbongs & bentleys", "Album Track", "Explicit", 2950000000, 88, 160, 59, 52, 13),
        ("Congratulations", "Stoney", "Album Track", "Explicit", 2550000000, 87, 123, 63, 80, 49),
        ("I Had Some Help", "F-1 Trillion", "Single", "Explicit", 1100000000, 94, 128, 64, 85, 89),
        ("Chemical", "Austin", "Single", "Non-Explicit", 720000000, 85, 170, 67, 90, 62),
        ("Better Now", "beerbongs & bentleys", "Album Track", "Explicit", 2050000000, 86, 145, 68, 56, 34),
        ("Pour Me a Drink", "F-1 Trillion", "Single", "Non-Explicit", 410000000, 83, 116, 68, 77, 72),
        ("Wow.", "Hollywood's Bleeding", "Single", "Explicit", 1780000000, 84, 100, 83, 54, 39),
        ("Goodbyes", "Hollywood's Bleeding", "Album Track", "Explicit", 1350000000, 82, 150, 58, 65, 18),
    ]),
    ("Ariana Grande", "Pop / R&B", [
        ("7 rings", "thank u, next", "Album Track", "Explicit", 2250000000, 88, 140, 78, 32, 33),
        ("thank u, next", "thank u, next", "Album Track", "Explicit", 1880000000, 86, 107, 72, 65, 41),
        ("positions", "Positions", "Album Track", "Explicit", 1450000000, 85, 144, 74, 80, 68),
        ("we can't be friends (wait for your love)", "eternal sunshine", "Single", "Non-Explicit", 980000000, 93, 116, 65, 74, 29),
        ("yes, and?", "eternal sunshine", "Single", "Explicit", 620000000, 87, 119, 80, 75, 70),
        ("Into You", "Dangerous Woman", "Album Track", "Non-Explicit", 1550000000, 85, 110, 62, 73, 37),
        ("Side to Side", "Dangerous Woman", "Album Track", "Explicit", 1420000000, 84, 159, 65, 74, 61),
        ("no tears left to cry", "Sweetener", "Single", "Non-Explicit", 1400000000, 83, 122, 70, 71, 35),
        ("the boy is mine", "eternal sunshine", "Album Track", "Explicit", 480000000, 86, 125, 77, 69, 56),
        ("God is a woman", "Sweetener", "Album Track", "Non-Explicit", 1150000000, 82, 145, 60, 66, 27),
    ]),
    ("Harry Styles", "Pop / Rock", [
        ("As It Was", "Harry's House", "Single", "Non-Explicit", 3450000000, 93, 174, 52, 73, 66),
        ("Watermelon Sugar", "Fine Line", "Album Track", "Non-Explicit", 2650000000, 89, 95, 55, 82, 56),
        ("Adore You", "Fine Line", "Album Track", "Non-Explicit", 1650000000, 86, 99, 68, 77, 57),
        ("Sign of the Times", "Harry Styles", "Single", "Non-Explicit", 1580000000, 85, 120, 52, 57, 21),
        ("Late Night Talking", "Harry's House", "Album Track", "Non-Explicit", 1100000000, 85, 115, 71, 73, 90),
        ("Matilda", "Harry's House", "Album Track", "Non-Explicit", 520000000, 80, 114, 51, 35, 39),
        ("Golden", "Fine Line", "Album Track", "Non-Explicit", 920000000, 82, 140, 45, 78, 54),
        ("Music For a Sushi Restaurant", "Harry's House", "Single", "Non-Explicit", 480000000, 80, 107, 72, 78, 93),
        ("Falling", "Fine Line", "Album Track", "Non-Explicit", 1150000000, 84, 110, 57, 27, 6),
        ("Cinema", "Harry's House", "Album Track", "Non-Explicit", 360000000, 76, 100, 74, 56, 54),
    ]),
    ("Olivia Rodrigo", "Pop / Indie Pop", [
        ("drivers license", "SOUR", "Single", "Explicit", 2200000000, 88, 144, 59, 43, 13),
        ("good 4 u", "SOUR", "Single", "Explicit", 2100000000, 88, 167, 56, 66, 69),
        ("vampire", "GUTS", "Single", "Explicit", 1320000000, 90, 138, 51, 53, 33),
        ("bad idea right?", "GUTS", "Single", "Explicit", 670000000, 84, 130, 63, 86, 75),
        ("deja vu", "SOUR", "Album Track", "Explicit", 1450000000, 86, 181, 44, 61, 18),
        ("traitor", "SOUR", "Album Track", "Non-Explicit", 1520000000, 86, 100, 38, 34, 9),
        ("get him back!", "GUTS", "Single", "Explicit", 520000000, 82, 105, 54, 88, 77),
        ("ballad of a homeschooled girl", "GUTS", "Album Track", "Explicit", 390000000, 79, 134, 49, 93, 62),
        ("obsessed", "GUTS (spilled)", "Single", "Explicit", 460000000, 83, 140, 66, 85, 73),
        ("favorite crime", "SOUR", "Album Track", "Non-Explicit", 980000000, 83, 128, 41, 28, 20),
    ]),
    ("Kendrick Lamar", "Hip-Hop / Rap", [
        ("HUMBLE.", "DAMN.", "Album Track", "Explicit", 2150000000, 88, 150, 90, 62, 42),
        ("Not Like Us", "Single", "Single", "Explicit", 1150000000, 96, 101, 90, 47, 78),
        ("All The Stars", "Black Panther The Album", "Single", "Explicit", 1650000000, 87, 97, 69, 63, 55),
        ("DNA.", "DAMN.", "Album Track", "Explicit", 1250000000, 84, 140, 64, 52, 42),
        ("Money Trees", "good kid, m.A.A.d city", "Album Track", "Explicit", 1720000000, 89, 72, 72, 53, 34),
        ("LOVE.", "DAMN.", "Album Track", "Explicit", 1380000000, 85, 126, 80, 58, 77),
        ("euphoria", "Single", "Single", "Explicit", 620000000, 90, 140, 69, 73, 54),
        ("Swimming Pools (Drank)", "good kid, m.A.A.d city", "Album Track", "Explicit", 1120000000, 83, 74, 69, 49, 29),
        ("Die Hard", "Mr. Morale & The Big Steppers", "Album Track", "Explicit", 540000000, 80, 101, 71, 70, 76),
        ("N95", "Mr. Morale & The Big Steppers", "Single", "Explicit", 490000000, 79, 140, 82, 73, 44),
    ]),
    ("SZA", "R&B / Soul", [
        ("Kill Bill", "SOS", "Album Track", "Explicit", 1950000000, 92, 118, 64, 73, 42),
        ("Snooze", "SOS", "Album Track", "Explicit", 1450000000, 91, 143, 56, 56, 39),
        ("Good Days", "SOS", "Single", "Explicit", 1080000000, 85, 121, 44, 65, 41),
        ("Nobody Gets Me", "SOS", "Album Track", "Explicit", 780000000, 84, 100, 36, 28, 29),
        ("Saturn", "Single", "Single", "Explicit", 690000000, 89, 178, 43, 62, 34),
        ("I Hate U", "SOS", "Single", "Explicit", 710000000, 83, 106, 54, 39, 41),
        ("The Weekend", "Ctrl", "Album Track", "Explicit", 1150000000, 84, 102, 74, 48, 60),
        ("Love Galore", "Ctrl", "Album Track", "Explicit", 1020000000, 83, 130, 79, 58, 48),
        ("Low", "SOS", "Album Track", "Explicit", 590000000, 81, 122, 83, 67, 30),
        ("Broken Clocks", "Ctrl", "Album Track", "Explicit", 720000000, 81, 120, 63, 66, 57),
    ]),
    ("Coldplay", "Rock / Alternative", [
        ("Yellow", "Parachutes", "Album Track", "Non-Explicit", 2450000000, 89, 173, 43, 52, 28),
        ("Viva La Vida", "Viva la Vida or Death and All His Friends", "Album Track", "Non-Explicit", 2300000000, 88, 138, 49, 62, 42),
        ("Something Just Like This", "Memories...Do Not Open", "Single", "Non-Explicit", 2650000000, 87, 103, 62, 64, 45),
        ("The Scientist", "A Rush of Blood to the Head", "Album Track", "Non-Explicit", 2100000000, 87, 146, 56, 44, 21),
        ("Fix You", "X&Y", "Album Track", "Non-Explicit", 1680000000, 85, 138, 21, 42, 12),
        ("My Universe", "Music of the Spheres", "Single", "Non-Explicit", 1250000000, 84, 105, 59, 71, 47),
        ("A Sky Full of Stars", "Ghost Stories", "Album Track", "Non-Explicit", 1520000000, 84, 125, 55, 68, 16),
        ("Paradise", "Mylo Xyloto", "Album Track", "Non-Explicit", 1380000000, 83, 140, 45, 60, 20),
        ("feelslikeimfallinginlove", "Moon Music", "Single", "Non-Explicit", 340000000, 81, 130, 52, 78, 62),
        ("Adventure of a Lifetime", "A Head Full of Dreams", "Album Track", "Non-Explicit", 1100000000, 82, 112, 66, 81, 86),
    ]),
    ("Imagine Dragons", "Rock / Pop Rock", [
        ("Believer", "Evolve", "Album Track", "Non-Explicit", 3150000000, 90, 125, 78, 78, 67),
        ("Demons", "Night Visions", "Album Track", "Non-Explicit", 2350000000, 88, 90, 51, 71, 43),
        ("Thunder", "Evolve", "Album Track", "Non-Explicit", 2400000000, 87, 168, 61, 82, 29),
        ("Radioactive", "Night Visions", "Album Track", "Non-Explicit", 1950000000, 85, 136, 45, 78, 21),
        ("Bones", "Mercury - Acts 1 & 2", "Single", "Non-Explicit", 1680000000, 88, 114, 77, 74, 57),
        ("Enemy", "Mercury - Acts 1 & 2", "Single", "Non-Explicit", 1550000000, 87, 77, 73, 78, 55),
        ("Whatever It Takes", "Evolve", "Album Track", "Non-Explicit", 1200000000, 82, 135, 67, 65, 54),
        ("Natural", "Origins", "Single", "Non-Explicit", 1400000000, 83, 100, 70, 61, 22),
        ("Bad Liar", "Origins", "Album Track", "Non-Explicit", 1150000000, 81, 175, 38, 79, 30),
        ("Eyes Closed", "LOOM", "Single", "Non-Explicit", 380000000, 82, 118, 68, 83, 62),
    ]),
    ("Justin Bieber", "Pop", [
        ("Stay", "F*ck Love 3: Overkill", "Single", "Explicit", 3100000000, 89, 170, 59, 76, 48),
        ("Ghost", "Justice", "Album Track", "Non-Explicit", 1750000000, 87, 154, 60, 74, 44),
        ("Peaches", "Justice", "Single", "Explicit", 1620000000, 86, 90, 68, 70, 46),
        ("Love Yourself", "Purpose", "Album Track", "Non-Explicit", 2400000000, 87, 100, 61, 38, 52),
        ("Sorry", "Purpose", "Album Track", "Non-Explicit", 2250000000, 86, 100, 65, 76, 41),
        ("What Do You Mean?", "Purpose", "Single", "Non-Explicit", 1650000000, 84, 125, 85, 75, 79),
        ("Intentions", "Changes", "Single", "Non-Explicit", 1200000000, 82, 148, 81, 55, 87),
        ("Hold On", "Justice", "Album Track", "Non-Explicit", 710000000, 80, 140, 66, 63, 29),
        ("Lonely", "Justice", "Single", "Explicit", 890000000, 81, 80, 43, 24, 10),
        ("Holy", "Justice", "Single", "Non-Explicit", 920000000, 81, 87, 67, 70, 37),
    ]),
    ("Eminem", "Hip-Hop / Rap", [
        ("Without Me", "The Eminem Show", "Album Track", "Explicit", 2250000000, 90, 112, 91, 67, 66),
        ("Lose Yourself", "8 Mile Soundtrack", "Single", "Explicit", 2200000000, 89, 171, 69, 74, 6),
        ("The Real Slim Shady", "The Marshall Mathers LP", "Album Track", "Explicit", 1950000000, 88, 105, 95, 66, 76),
        ("Mockingbird", "Encore", "Album Track", "Explicit", 1780000000, 89, 84, 64, 67, 24),
        ("Houdini", "The Death of Slim Shady (Coup de Grâce)", "Single", "Explicit", 690000000, 92, 128, 92, 88, 88),
        ("Godzilla", "Music To Be Murdered By", "Album Track", "Explicit", 1450000000, 85, 166, 76, 75, 83),
        ("Till I Collapse", "The Eminem Show", "Album Track", "Explicit", 1920000000, 86, 171, 55, 85, 10),
        ("Stan", "The Marshall Mathers LP", "Album Track", "Explicit", 1250000000, 84, 80, 78, 77, 51),
        ("Tobey", "The Death of Slim Shady (Coup de Grâce)", "Single", "Explicit", 340000000, 81, 140, 82, 70, 48),
        ("Not Afraid", "Recovery", "Single", "Explicit", 1100000000, 83, 86, 86, 95, 67),
    ]),
    ("Billie Eilish & Finneas", "Pop / Acoustic", [
        ("I Love You", "WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?", "Album Track", "Non-Explicit", 920000000, 82, 137, 42, 14, 12),
        ("Bellyache", "Don't Smile at Me", "Single", "Non-Explicit", 1120000000, 83, 100, 70, 45, 58),
        ("Your Power", "Happier Than Ever", "Single", "Non-Explicit", 650000000, 80, 130, 63, 28, 48),
        ("My Future", "Happier Than Ever", "Single", "Non-Explicit", 580000000, 79, 115, 44, 43, 31),
        ("Bury a Friend", "WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?", "Single", "Non-Explicit", 1050000000, 82, 120, 90, 39, 20),
    ]),
    ("Bruno Mars", "Pop / Funk / R&B", [
        ("Locked Out of Heaven", "Unorthodox Jukebox", "Single", "Non-Explicit", 2300000000, 89, 144, 73, 70, 87),
        ("That's What I Like", "24K Magic", "Album Track", "Non-Explicit", 2150000000, 88, 134, 85, 56, 86),
        ("Just the Way You Are", "Doo-Wops & Hooligans", "Single", "Non-Explicit", 2200000000, 87, 109, 64, 84, 43),
        ("Die With a Smile", "Single", "Single", "Non-Explicit", 1120000000, 97, 158, 54, 71, 52),
        ("Leave The Door Open", "An Evening with Silk Sonic", "Single", "Non-Explicit", 1350000000, 86, 148, 59, 62, 72),
        ("24K Magic", "24K Magic", "Single", "Explicit", 1550000000, 84, 107, 82, 80, 86),
        ("When I Was Your Man", "Unorthodox Jukebox", "Album Track", "Non-Explicit", 2100000000, 87, 73, 61, 40, 40),
        ("Smokin Out The Window", "An Evening with Silk Sonic", "Album Track", "Explicit", 680000000, 82, 82, 63, 67, 88),
        ("Grenade", "Doo-Wops & Hooligans", "Album Track", "Non-Explicit", 1450000000, 83, 110, 71, 56, 23),
        ("Treasure", "Unorthodox Jukebox", "Album Track", "Non-Explicit", 1100000000, 82, 116, 69, 70, 94),
    ]),
    ("Kanye West", "Hip-Hop / Rap", [
        ("Stronger", "Graduation", "Album Track", "Explicit", 1850000000, 87, 123, 77, 72, 49),
        ("Heartless", "808s & Heartbreak", "Single", "Non-Explicit", 1650000000, 88, 88, 79, 65, 65),
        ("Flashing Lights", "Graduation", "Album Track", "Non-Explicit", 1520000000, 87, 90, 64, 63, 43),
        ("CARNIVAL", "VULTURES 1", "Single", "Explicit", 820000000, 88, 148, 59, 81, 31),
        ("Father Stretch My Hands Pt. 1", "The Life Of Pablo", "Album Track", "Explicit", 1350000000, 85, 113, 73, 56, 47),
        ("Runaway", "My Beautiful Dark Twisted Fantasy", "Album Track", "Explicit", 980000000, 85, 85, 38, 56, 11),
        ("Bound 2", "Yeezus", "Album Track", "Explicit", 1120000000, 84, 149, 37, 67, 31),
        ("Praise God", "Donda", "Album Track", "Explicit", 670000000, 81, 118, 88, 66, 29),
        ("Power", "My Beautiful Dark Twisted Fantasy", "Single", "Explicit", 1180000000, 83, 154, 54, 91, 57),
        ("Gold Digger", "Late Registration", "Single", "Explicit", 1450000000, 84, 93, 63, 70, 62),
    ])
]

# Additional procedural track generation to build a comprehensive 1000-track dataset
additional_genres = [
    "Pop", "Hip-Hop / Rap", "R&B / Soul", "Dance / Electronic", "Rock / Alternative", 
    "Latin / Reggaeton", "Acoustic / Folk", "Indie Pop", "K-Pop", "Afrobeats"
]

extra_artists_by_genre = {
    "Pop": ["Sabrina Carpenter", "Chappell Roan", "Miley Cyrus", "Katy Perry", "Shawn Mendes", "Camila Cabello", "Selena Gomez", "Charlie Puth", "Tate McRae", "Troye Sivan"],
    "Hip-Hop / Rap": ["Travis Scott", "Future", "21 Savage", "J. Cole", "Jack Harlow", "Lil Nas X", "Post Malone", "Doja Cat", "Megan Thee Stallion", "Gunna"],
    "R&B / Soul": ["Frank Ocean", "Brent Faiyaz", "Giveon", "Daniel Caesar", "Steve Lacy", "Summer Walker", "Jhené Aiko", "Khalid", "Bryson Tiller", "Kehlani"],
    "Dance / Electronic": ["Calvin Harris", "David Guetta", "Avicii", "The Chainsmokers", "Kygo", "Marshmello", "Tiësto", "Martin Garrix", "Fred again..", "Peggy Gou"],
    "Rock / Alternative": ["Arctic Monkeys", "The Neighbourhood", "Maneskin", "Twenty One Pilots", "Fall Out Boy", "Linkin Park", "Hozier", "Paramore", "The Killers", "Glass Animals"],
    "Latin / Reggaeton": ["Karol G", "Rauw Alejandro", "Feid", "J Balvin", "Maluma", "Ozuna", "Anuel AA", "Myke Towers", "Peso Pluma", "Rosalía"],
    "Acoustic / Folk": ["Noah Kahan", "Zach Bryan", "Vance Joy", "Passenger", "James Arthur", "Dean Lewis", "Lewis Capaldi", "Sam Smith", "George Ezra", "Lumineers"],
    "Indie Pop": ["Lorde", "Clairo", "Phoebe Bridgers", "Boygenius", "Rex Orange County", "Wallows", "Girl in Red", "Dominic Fike", "Beabadoobee", "Mitski"],
    "K-Pop": ["BTS", "BLACKPINK", "NewJeans", "Stray Kids", "TWICE", "Jung Kook", "Jimin", "LE SSERAFIM", "TOMORROW X TOGETHER", "IVE"],
    "Afrobeats": ["Burna Boy", "Rema", "Wizkid", "Asake", "Tems", "Ayra Starr", "Omah Lay", "Davido", "Fireboy DML", "CKay"]
}

words1 = ["Midnight", "Golden", "Neon", "Electric", "Velvet", "Silent", "Lost", "Wild", "Endless", "Sweet", "Broken", "Falling", "Silver", "Crimson", "Ocean", "Dancing", "Secret", "Starlight", "Shadow", "Summer", "Winter", "Chasing", "Heavy", "Deep", "Pure", "After", "Forever", "Echoes of", "Voices in", "Running with"]
words2 = ["Dreams", "Heart", "Rhythm", "Rain", "Sky", "Fire", "Night", "Tears", "Waves", "Memories", "Soul", "Vibes", "Shadows", "Breeze", "Lover", "Goodbye", "Storm", "Whisper", "Glow", "Echo", "Time", "Streets", "Highway", "Fantasy", "Horizon", "Paradise", "Silence", "Reckoning", "Melody", "Miracle"]

album_names_pool = [
    "Chronicles", "Metamorphosis", "After Dark", "Horizons", "Genesis", "Neon Lights", 
    "Serenade", "Echoes in Time", "Electric Sunset", "Stardust & Shadows", "Heartbeat Odyssey",
    "Midnight Reflections", "Solar Flares", "The Long Road Home", "Velvet Skies", "Infinite Rhythm",
    "Daylight", "Renaissance", "Visions", "Sublime", "The Great Escape", "True Colors"
]

records = []
track_counter = 1

# 1. First add curated top hits
for artist, genre, tracks in artists_genres:
    for t in tracks:
        t_name, album, track_type, explicit, streams, pop, bpm, dance, energy, valence = t
        
        # Release date spread between 2020-01-01 and 2024-09-30
        rand_days = random.randint(0, 1700)
        base_date = datetime.date(2020, 1, 1) + datetime.timedelta(days=rand_days)
        
        rel_year = base_date.year
        rel_month = base_date.month
        rel_month_name = base_date.strftime("%b")
        rel_day = base_date.day
        
        duration_sec = random.randint(145, 270)
        duration_ms = duration_sec * 1000
        
        acousticness = random.randint(5, 75)
        speechiness = random.randint(3, 40)
        in_playlists = int(streams / random.randint(45000, 95000)) + random.randint(500, 3000)
        
        records.append({
            "track_id": f"SPOT_{track_counter:04d}",
            "track_name": t_name,
            "artist_name": artist,
            "album_name": album,
            "release_date": base_date.strftime("%Y-%m-%d"),
            "release_year": rel_year,
            "release_month": rel_month,
            "release_month_name": rel_month_name,
            "release_day": rel_day,
            "genre": genre.split(" / ")[0],
            "track_type": track_type,
            "is_explicit": explicit,
            "popularity": pop,
            "streams": streams,
            "in_spotify_playlists": in_playlists,
            "duration_ms": duration_ms,
            "duration_sec": duration_sec,
            "bpm": bpm,
            "danceability_%": dance,
            "energy_%": energy,
            "valence_%": valence,
            "acousticness_%": acousticness,
            "speechiness_%": speechiness
        })
        track_counter += 1

# 2. Add realistic procedural tracks to reach 1,000 total songs
target_count = 1000
while track_counter <= target_count:
    genre = random.choice(additional_genres)
    artist = random.choice(extra_artists_by_genre[genre])
    
    t_name = f"{random.choice(words1)} {random.choice(words2)}"
    track_type = "Album Track" if random.random() < 0.68 else "Single"
    
    if track_type == "Album Track":
        album = f"{random.choice(album_names_pool)}"
    else:
        album = "Single"
        
    explicit = "Explicit" if random.random() < 0.36 else "Non-Explicit"
    
    # Generate realistic release date between 2020-01-01 and 2024-10-31
    rand_days = random.randint(0, 1765)
    base_date = datetime.date(2020, 1, 1) + datetime.timedelta(days=rand_days)
    rel_year = base_date.year
    rel_month = base_date.month
    rel_month_name = base_date.strftime("%b")
    rel_day = base_date.day
    
    # Popularity & Streams with realistic power-law / log-normal distribution
    pop = random.randint(45, 95)
    # Higher popularity tracks have exponentially more streams
    base_streams = int((pop ** 4.3) * random.uniform(0.7, 1.4) + random.randint(10000000, 80000000))
    # Cap between 15M and 2.8B
    streams = min(max(base_streams, 15000000), 2850000000)
    
    in_playlists = int(streams / random.randint(50000, 110000)) + random.randint(200, 4000)
    
    duration_sec = random.randint(135, 290)
    duration_ms = duration_sec * 1000
    
    # Genre-correlated audio features
    if genre in ["Dance / Electronic", "Latin / Reggaeton"]:
        bpm = random.randint(115, 135)
        dance = random.randint(68, 94)
        energy = random.randint(65, 95)
        valence = random.randint(50, 92)
    elif genre in ["Hip-Hop / Rap"]:
        bpm = random.randint(80, 160)
        dance = random.randint(62, 92)
        energy = random.randint(55, 88)
        valence = random.randint(35, 78)
        explicit = "Explicit" if random.random() < 0.72 else "Non-Explicit"
    elif genre in ["Acoustic / Folk", "Indie Pop"]:
        bpm = random.randint(75, 130)
        dance = random.randint(35, 65)
        energy = random.randint(25, 62)
        valence = random.randint(20, 60)
    else:
        bpm = random.randint(90, 150)
        dance = random.randint(50, 85)
        energy = random.randint(45, 85)
        valence = random.randint(30, 85)
        
    acousticness = random.randint(5, 85)
    speechiness = random.randint(3, 35)

    records.append({
        "track_id": f"SPOT_{track_counter:04d}",
        "track_name": t_name,
        "artist_name": artist,
        "album_name": album,
        "release_date": base_date.strftime("%Y-%m-%d"),
        "release_year": rel_year,
        "release_month": rel_month,
        "release_month_name": rel_month_name,
        "release_day": rel_day,
        "genre": genre,
        "track_type": track_type,
        "is_explicit": explicit,
        "popularity": pop,
        "streams": streams,
        "in_spotify_playlists": in_playlists,
        "duration_ms": duration_ms,
        "duration_sec": duration_sec,
        "bpm": bpm,
        "danceability_%": dance,
        "energy_%": energy,
        "valence_%": valence,
        "acousticness_%": acousticness,
        "speechiness_%": speechiness
    })
    track_counter += 1

csv_path = r"C:\Users\Pravin Ghule\Downloads\BT_Mini_Project\Spotify_PowerBI_Project\spotify_tracks_data.csv"
fieldnames = [
    "track_id", "track_name", "artist_name", "album_name", 
    "release_date", "release_year", "release_month", "release_month_name", "release_day",
    "genre", "track_type", "is_explicit", "popularity", "streams", 
    "in_spotify_playlists", "duration_ms", "duration_sec", "bpm", 
    "danceability_%", "energy_%", "valence_%", "acousticness_%", "speechiness_%"
]

with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

print(f"Successfully generated {len(records)} Spotify tracks to {csv_path}")
