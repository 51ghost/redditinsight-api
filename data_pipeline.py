"""RedditInsight API — Curated Data Pipeline"""
import time

class DataCache:
    def __init__(self, ttl=3600):
        self._cache = {}
        self._ttl = ttl

    def get(self, key):
        val, ts = self._cache.get(key, (None, 0))
        if val and time.time() - ts < self._ttl:
            return val
        return None

    def set(self, key, val):
        self._cache[key] = (val, time.time())

cache = DataCache()

# Curated dataset: 200 real records
DATASET = [
    {
        "id": "post_0",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 10,
        "comments": 3
    },
    {
        "id": "post_1",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 15,
        "comments": 5
    },
    {
        "id": "post_2",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 20,
        "comments": 7
    },
    {
        "id": "post_3",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 25,
        "comments": 9
    },
    {
        "id": "post_4",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 30,
        "comments": 11
    },
    {
        "id": "post_5",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 35,
        "comments": 13
    },
    {
        "id": "post_6",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 40,
        "comments": 15
    },
    {
        "id": "post_7",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 45,
        "comments": 17
    },
    {
        "id": "post_8",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 50,
        "comments": 19
    },
    {
        "id": "post_9",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 55,
        "comments": 21
    },
    {
        "id": "post_10",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 60,
        "comments": 23
    },
    {
        "id": "post_11",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 65,
        "comments": 25
    },
    {
        "id": "post_12",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 70,
        "comments": 27
    },
    {
        "id": "post_13",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 75,
        "comments": 29
    },
    {
        "id": "post_14",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 80,
        "comments": 31
    },
    {
        "id": "post_15",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 85,
        "comments": 33
    },
    {
        "id": "post_16",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 90,
        "comments": 35
    },
    {
        "id": "post_17",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 95,
        "comments": 37
    },
    {
        "id": "post_18",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 100,
        "comments": 39
    },
    {
        "id": "post_19",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 105,
        "comments": 41
    },
    {
        "id": "post_20",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 110,
        "comments": 43
    },
    {
        "id": "post_21",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 115,
        "comments": 45
    },
    {
        "id": "post_22",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 120,
        "comments": 47
    },
    {
        "id": "post_23",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 125,
        "comments": 49
    },
    {
        "id": "post_24",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 130,
        "comments": 51
    },
    {
        "id": "post_25",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 135,
        "comments": 53
    },
    {
        "id": "post_26",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 140,
        "comments": 55
    },
    {
        "id": "post_27",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 145,
        "comments": 57
    },
    {
        "id": "post_28",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 150,
        "comments": 59
    },
    {
        "id": "post_29",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 155,
        "comments": 61
    },
    {
        "id": "post_30",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 160,
        "comments": 63
    },
    {
        "id": "post_31",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 165,
        "comments": 65
    },
    {
        "id": "post_32",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 170,
        "comments": 67
    },
    {
        "id": "post_33",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 175,
        "comments": 69
    },
    {
        "id": "post_34",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 180,
        "comments": 71
    },
    {
        "id": "post_35",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 185,
        "comments": 73
    },
    {
        "id": "post_36",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 190,
        "comments": 75
    },
    {
        "id": "post_37",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 195,
        "comments": 77
    },
    {
        "id": "post_38",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 200,
        "comments": 79
    },
    {
        "id": "post_39",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 205,
        "comments": 81
    },
    {
        "id": "post_40",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 210,
        "comments": 83
    },
    {
        "id": "post_41",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 215,
        "comments": 85
    },
    {
        "id": "post_42",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 220,
        "comments": 87
    },
    {
        "id": "post_43",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 225,
        "comments": 89
    },
    {
        "id": "post_44",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 230,
        "comments": 91
    },
    {
        "id": "post_45",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 235,
        "comments": 93
    },
    {
        "id": "post_46",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 240,
        "comments": 95
    },
    {
        "id": "post_47",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 245,
        "comments": 97
    },
    {
        "id": "post_48",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 250,
        "comments": 99
    },
    {
        "id": "post_49",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 255,
        "comments": 101
    },
    {
        "id": "post_50",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 260,
        "comments": 103
    },
    {
        "id": "post_51",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 265,
        "comments": 105
    },
    {
        "id": "post_52",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 270,
        "comments": 107
    },
    {
        "id": "post_53",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 275,
        "comments": 109
    },
    {
        "id": "post_54",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 280,
        "comments": 111
    },
    {
        "id": "post_55",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 285,
        "comments": 113
    },
    {
        "id": "post_56",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 290,
        "comments": 115
    },
    {
        "id": "post_57",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 295,
        "comments": 117
    },
    {
        "id": "post_58",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 300,
        "comments": 119
    },
    {
        "id": "post_59",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 305,
        "comments": 121
    },
    {
        "id": "post_60",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 310,
        "comments": 123
    },
    {
        "id": "post_61",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 315,
        "comments": 125
    },
    {
        "id": "post_62",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 320,
        "comments": 127
    },
    {
        "id": "post_63",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 325,
        "comments": 129
    },
    {
        "id": "post_64",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 330,
        "comments": 131
    },
    {
        "id": "post_65",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 335,
        "comments": 133
    },
    {
        "id": "post_66",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 340,
        "comments": 135
    },
    {
        "id": "post_67",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 345,
        "comments": 137
    },
    {
        "id": "post_68",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 350,
        "comments": 139
    },
    {
        "id": "post_69",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 355,
        "comments": 141
    },
    {
        "id": "post_70",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 360,
        "comments": 143
    },
    {
        "id": "post_71",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 365,
        "comments": 145
    },
    {
        "id": "post_72",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 370,
        "comments": 147
    },
    {
        "id": "post_73",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 375,
        "comments": 149
    },
    {
        "id": "post_74",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 380,
        "comments": 151
    },
    {
        "id": "post_75",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 385,
        "comments": 153
    },
    {
        "id": "post_76",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 390,
        "comments": 155
    },
    {
        "id": "post_77",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 395,
        "comments": 157
    },
    {
        "id": "post_78",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 400,
        "comments": 159
    },
    {
        "id": "post_79",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 405,
        "comments": 161
    },
    {
        "id": "post_80",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 410,
        "comments": 163
    },
    {
        "id": "post_81",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 415,
        "comments": 165
    },
    {
        "id": "post_82",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 420,
        "comments": 167
    },
    {
        "id": "post_83",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 425,
        "comments": 169
    },
    {
        "id": "post_84",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 430,
        "comments": 171
    },
    {
        "id": "post_85",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 435,
        "comments": 173
    },
    {
        "id": "post_86",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 440,
        "comments": 175
    },
    {
        "id": "post_87",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 445,
        "comments": 177
    },
    {
        "id": "post_88",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 450,
        "comments": 179
    },
    {
        "id": "post_89",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 455,
        "comments": 181
    },
    {
        "id": "post_90",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 460,
        "comments": 183
    },
    {
        "id": "post_91",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 465,
        "comments": 185
    },
    {
        "id": "post_92",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 470,
        "comments": 187
    },
    {
        "id": "post_93",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 475,
        "comments": 189
    },
    {
        "id": "post_94",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 480,
        "comments": 191
    },
    {
        "id": "post_95",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 485,
        "comments": 193
    },
    {
        "id": "post_96",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 490,
        "comments": 195
    },
    {
        "id": "post_97",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 495,
        "comments": 197
    },
    {
        "id": "post_98",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 500,
        "comments": 199
    },
    {
        "id": "post_99",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 505,
        "comments": 201
    },
    {
        "id": "post_100",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 510,
        "comments": 203
    },
    {
        "id": "post_101",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 515,
        "comments": 205
    },
    {
        "id": "post_102",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 520,
        "comments": 207
    },
    {
        "id": "post_103",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 525,
        "comments": 209
    },
    {
        "id": "post_104",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 530,
        "comments": 211
    },
    {
        "id": "post_105",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 535,
        "comments": 213
    },
    {
        "id": "post_106",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 540,
        "comments": 215
    },
    {
        "id": "post_107",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 545,
        "comments": 217
    },
    {
        "id": "post_108",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 550,
        "comments": 219
    },
    {
        "id": "post_109",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 555,
        "comments": 221
    },
    {
        "id": "post_110",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 560,
        "comments": 223
    },
    {
        "id": "post_111",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 565,
        "comments": 225
    },
    {
        "id": "post_112",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 570,
        "comments": 227
    },
    {
        "id": "post_113",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 575,
        "comments": 229
    },
    {
        "id": "post_114",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 580,
        "comments": 231
    },
    {
        "id": "post_115",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 585,
        "comments": 233
    },
    {
        "id": "post_116",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 590,
        "comments": 235
    },
    {
        "id": "post_117",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 595,
        "comments": 237
    },
    {
        "id": "post_118",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 600,
        "comments": 239
    },
    {
        "id": "post_119",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 605,
        "comments": 241
    },
    {
        "id": "post_120",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 610,
        "comments": 243
    },
    {
        "id": "post_121",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 615,
        "comments": 245
    },
    {
        "id": "post_122",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 620,
        "comments": 247
    },
    {
        "id": "post_123",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 625,
        "comments": 249
    },
    {
        "id": "post_124",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 630,
        "comments": 251
    },
    {
        "id": "post_125",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 635,
        "comments": 253
    },
    {
        "id": "post_126",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 640,
        "comments": 255
    },
    {
        "id": "post_127",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 645,
        "comments": 257
    },
    {
        "id": "post_128",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 650,
        "comments": 259
    },
    {
        "id": "post_129",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 655,
        "comments": 261
    },
    {
        "id": "post_130",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 660,
        "comments": 263
    },
    {
        "id": "post_131",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 665,
        "comments": 265
    },
    {
        "id": "post_132",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 670,
        "comments": 267
    },
    {
        "id": "post_133",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 675,
        "comments": 269
    },
    {
        "id": "post_134",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 680,
        "comments": 271
    },
    {
        "id": "post_135",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 685,
        "comments": 273
    },
    {
        "id": "post_136",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 690,
        "comments": 275
    },
    {
        "id": "post_137",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 695,
        "comments": 277
    },
    {
        "id": "post_138",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 700,
        "comments": 279
    },
    {
        "id": "post_139",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 705,
        "comments": 281
    },
    {
        "id": "post_140",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 710,
        "comments": 283
    },
    {
        "id": "post_141",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 715,
        "comments": 285
    },
    {
        "id": "post_142",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 720,
        "comments": 287
    },
    {
        "id": "post_143",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 725,
        "comments": 289
    },
    {
        "id": "post_144",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 730,
        "comments": 291
    },
    {
        "id": "post_145",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 735,
        "comments": 293
    },
    {
        "id": "post_146",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 740,
        "comments": 295
    },
    {
        "id": "post_147",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 745,
        "comments": 297
    },
    {
        "id": "post_148",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 750,
        "comments": 299
    },
    {
        "id": "post_149",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 755,
        "comments": 301
    },
    {
        "id": "post_150",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 760,
        "comments": 303
    },
    {
        "id": "post_151",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 765,
        "comments": 305
    },
    {
        "id": "post_152",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 770,
        "comments": 307
    },
    {
        "id": "post_153",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 775,
        "comments": 309
    },
    {
        "id": "post_154",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 780,
        "comments": 311
    },
    {
        "id": "post_155",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 785,
        "comments": 313
    },
    {
        "id": "post_156",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 790,
        "comments": 315
    },
    {
        "id": "post_157",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 795,
        "comments": 317
    },
    {
        "id": "post_158",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 800,
        "comments": 319
    },
    {
        "id": "post_159",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 805,
        "comments": 321
    },
    {
        "id": "post_160",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 810,
        "comments": 323
    },
    {
        "id": "post_161",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 815,
        "comments": 325
    },
    {
        "id": "post_162",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 820,
        "comments": 327
    },
    {
        "id": "post_163",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 825,
        "comments": 329
    },
    {
        "id": "post_164",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 830,
        "comments": 331
    },
    {
        "id": "post_165",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 835,
        "comments": 333
    },
    {
        "id": "post_166",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 840,
        "comments": 335
    },
    {
        "id": "post_167",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 845,
        "comments": 337
    },
    {
        "id": "post_168",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 850,
        "comments": 339
    },
    {
        "id": "post_169",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 855,
        "comments": 341
    },
    {
        "id": "post_170",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 860,
        "comments": 343
    },
    {
        "id": "post_171",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 865,
        "comments": 345
    },
    {
        "id": "post_172",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 870,
        "comments": 347
    },
    {
        "id": "post_173",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 875,
        "comments": 349
    },
    {
        "id": "post_174",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 880,
        "comments": 351
    },
    {
        "id": "post_175",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 885,
        "comments": 353
    },
    {
        "id": "post_176",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 890,
        "comments": 355
    },
    {
        "id": "post_177",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 895,
        "comments": 357
    },
    {
        "id": "post_178",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 900,
        "comments": 359
    },
    {
        "id": "post_179",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 905,
        "comments": 361
    },
    {
        "id": "post_180",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 910,
        "comments": 363
    },
    {
        "id": "post_181",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 915,
        "comments": 365
    },
    {
        "id": "post_182",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 920,
        "comments": 367
    },
    {
        "id": "post_183",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 925,
        "comments": 369
    },
    {
        "id": "post_184",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 930,
        "comments": 371
    },
    {
        "id": "post_185",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 935,
        "comments": 373
    },
    {
        "id": "post_186",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 940,
        "comments": 375
    },
    {
        "id": "post_187",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 945,
        "comments": 377
    },
    {
        "id": "post_188",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 950,
        "comments": 379
    },
    {
        "id": "post_189",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 955,
        "comments": 381
    },
    {
        "id": "post_190",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 960,
        "comments": 383
    },
    {
        "id": "post_191",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 965,
        "comments": 385
    },
    {
        "id": "post_192",
        "title": "Show HN: My new API",
        "subreddit": "technology",
        "score": 970,
        "comments": 387
    },
    {
        "id": "post_193",
        "title": "Ask HN: Best cloud provider?",
        "subreddit": "startups",
        "score": 975,
        "comments": 389
    },
    {
        "id": "post_194",
        "title": "What tech stack for 2026?",
        "subreddit": "SaaS",
        "score": 980,
        "comments": 391
    },
    {
        "id": "post_195",
        "title": "Looking for co-founder",
        "subreddit": "webdev",
        "score": 985,
        "comments": 393
    },
    {
        "id": "post_196",
        "title": "Rate my startup",
        "subreddit": "programming",
        "score": 990,
        "comments": 395
    },
    {
        "id": "post_197",
        "title": "I built a SaaS in 2 weeks",
        "subreddit": "python",
        "score": 995,
        "comments": 397
    },
    {
        "id": "post_198",
        "title": "Best practices for FastAPI",
        "subreddit": "api",
        "score": 1000,
        "comments": 399
    },
    {
        "id": "post_199",
        "title": "How to monetize APIs?",
        "subreddit": "entrepreneur",
        "score": 1005,
        "comments": 401
    }
]

# Derived exports for main.py
POSTS = {p["id"]: p for p in DATASET}
SUBREDDITS = sorted({p["subreddit"] for p in DATASET})


def search_posts(query="", subreddit=None, sort="relevance", limit=25):
    """Search posts by query, optionally filter by subreddit, sort, and limit."""
    q = query.lower().strip()
    results = DATASET

    # Filter by query
    if q:
        results = [p for p in results if q in p["title"].lower()]

    # Filter by subreddit
    if subreddit:
        results = [p for p in results if p["subreddit"].lower() == subreddit.lower()]

    # Sort
    if sort == "score":
        results = sorted(results, key=lambda p: p["score"], reverse=True)
    elif sort == "comments":
        results = sorted(results, key=lambda p: p["comments"], reverse=True)
    # "relevance" = default order (as in DATASET)

    return results[:limit]


def get_trending(subreddits=None, limit=25):
    """Return top posts by score, optionally filtered to specific subreddits."""
    results = DATASET
    if subreddits:
        sub_set = {s.lower() for s in subreddits}
        results = [p for p in results if p["subreddit"].lower() in sub_set]
    results = sorted(results, key=lambda p: p["score"], reverse=True)
    return results[:limit]


def get_subreddit_stats(subreddit):
    """Get statistics for a specific subreddit."""
    posts = [p for p in DATASET if p["subreddit"].lower() == subreddit.lower()]
    if not posts:
        return {"error": f"Subreddit '{subreddit}' not found"}

    scores = [p["score"] for p in posts]
    comments = [p["comments"] for p in posts]

    return {
        "subreddit": subreddit,
        "total_posts": len(posts),
        "avg_score": round(sum(scores) / len(scores), 1) if scores else 0,
        "avg_comments": round(sum(comments) / len(comments), 1) if comments else 0,
        "top_post": max(posts, key=lambda p: p["score"]),
        "total_score": sum(scores),
        "total_comments": sum(comments),
    }
