import pandas as pd
from pathlib import Path

###########################################
# 初期設定
# lobby != "standard"  # squad_2, squad_4

game_mode_1 = "area"  # area, yagura, hoko, asari
# game_mode_2 = "yagura"

# ルール毎
# all    campingshelter_camo
# area   52gal
# yagura dynamo_becchu
# hoko   bucketslosher_deco
# asari  kelvin525_becchu

# 2つまで
# all bottlegeyser
# area campingshelter_camo
# yagura bottlegeyser
# hoko bottlegeyser　結構差ある
# asari　bottlegeyser

# area yagura campingshelter_camo
# hoko asari bucketslosher_deco

if 0:
    stage1 = "shottsuru"
    stage2 = "ama"
    # ajifry, ama, anchovy, arowana, battera, bbass, chozame, devon, engawa, fujitsubo, gangaze, hakofugu, hokke, kombu,
    # manta, mongara, mozuku, mutsugoro, otoro, shottsuru, sumeshi, tachiuo, zatou
elif 0:
    period = '2020-06'

game_ver = "5.2.0"
file_name = "df/Ver." + game_ver + ".pkl"  # All.pkl, Ver.5.2.0.pkl, 2020-03.pkl
# file_name = "df/Feb.all.pkl"
###########################################
exclude_a1 = True
path = Path("./data")

if 0:
    df = pd.DataFrame()
    for file in path.glob("*"):
        print("read ", file)
        # データの読み込み
        df_l = pd.read_csv(file, dtype="string")
        # line = -1
        # for period, game_ver_l, lobby_mode, lobby, \
        #     A1_inked, A2_inked, A3_inked, A4_inked, B1_inked, B2_inked, B3_inked, B4_inked \
        #         in zip(df_l['# period'], df_l['game-ver'], df_l['lobby-mode'], df_l['lobby'],
        #                df_l['A1-inked'], df_l['A2-inked'], df_l['A3-inked'], df_l['A4-inked'],
        #                df_l['B1-inked'], df_l['B2-inked'], df_l['B3-inked'], df_l['B4-inked']):
        #     line += 1
        #     # (lobby != "standard") or
        #     if (lobby_mode == "regular") or (game_ver_l != game_ver or \
        #             (A1_inked is pd.NA) or (A1_inked == 0) or \
        #             (A2_inked is pd.NA) or (A2_inked == 0) or \
        #             (A3_inked is pd.NA) or (A3_inked == 0) or \
        #             (A4_inked is pd.NA) or (A4_inked == 0) or \
        #             (B1_inked is pd.NA) or (B1_inked == 0) or \
        #             (B2_inked is pd.NA) or (B2_inked == 0) or \
        #             (B3_inked is pd.NA) or (B3_inked == 0) or \
        #             (B4_inked is pd.NA) or (B4_inked == 0):
        #         # or (not('2020-03' in period))
        #         df_l.drop(line, inplace=True)
        #         continue
        df = df.append(df_l)
    df.to_pickle(file_name)
else:
    df = pd.read_pickle(file_name)

# https://stat.ink/api-info/weapon2?_lang_=ja-JP
win_count = {"splatscope": 0, "sshooter_collabo": 0, "sshooter": 0, "hokusai": 0, "liter4k": 0, "bold": 0, "nan": 0,
             "wakaba": 0, "<NA>": 0, "hissen": 0, "nzap85": 0, "sharp": 0, "dualsweeper": 0, "nova": 0,
             "splatroller": 0, "rapid": 0, "splatroller_collabo": 0, "52gal": 0, "heroslosher_replica": 0,
             "sputtery": 0, "heroshooter_replica": 0, "maneuver": 0, "pablo": 0, "variableroller": 0, "jetsweeper": 0,
             "liter4k_scope": 0, "hotblaster_custom": 0, "barrelspinner": 0, "prime": 0, "heroroller_replica": 0,
             "splatscope_collabo": 0, "splatcharger": 0, "heromaneuver_replica": 0, "herospinner_replica": 0,
             "dynamo": 0, "herobrush_replica": 0, "maneuver_collabo": 0, "96gal": 0, "h3reelgun": 0,
             "heroshelter_replica": 0, "l3reelgun": 0, "parashelter": 0, "splatcharger_collabo": 0, "promodeler_mg": 0,
             "bucketslosher": 0, "soytuber": 0, "carbon": 0, "heroblaster_replica": 0, "hotblaster": 0,
             "herocharger_replica": 0, "splatspinner": 0, "promodeler_rg": 0, "clashblaster": 0, "squiclean_a": 0,
             "screwslosher": 0, "prime_collabo": 0, "momiji": 0, "barrelspinner_deco": 0, "rapid_elite": 0,
             "bamboo14mk1": 0, "campingshelter": 0, "liter4k_custom": 0, "liter4k_scope_custom": 0, "longblaster": 0,
             "dynamo_tesla": 0, "jetsweeper_custom": 0, "pablo_hue": 0, "variableroller_foil": 0, "hydra": 0,
             "kelvin525": 0, "nzap89": 0, "bucketslosher_deco": 0, "bottlegeyser": 0, "spygadget": 0, "hokusai_hue": 0,
             "l3reelgun_d": 0, "sputtery_hue": 0, "52gal_deco": 0, "rapid_deco": 0, "96gal_deco": 0,
             "soytuber_custom": 0, "screwslosher_neo": 0, "nova_neo": 0, "quadhopper_black": 0, "bold_neo": 0,
             "h3reelgun_d": 0, "splatspinner_collabo": 0, "parashelter_sorella": 0, "clashblaster_neo": 0,
             "hissen_hue": 0, "longblaster_custom": 0, "sharp_neo": 0, "kelvin525_deco": 0, "bottlegeyser_foil": 0,
             "squiclean_b": 0, "dualsweeper_custom": 0, "carbon_deco": 0, "rapid_elite_deco": 0, "spygadget_sorella": 0,
             "octoshooter_replica": 0, "kugelschreiber": 0, "explosher": 0, "bamboo14mk2": 0,
             "campingshelter_sorella": 0, "furo": 0, "nautilus47": 0, "quadhopper_white": 0, "hydra_custom": 0,
             "splatscope_becchu": 0, "splatcharger_becchu": 0, "maneuver_becchu": 0, "sshooter_becchu": 0,
             "splatroller_becchu": 0, "nova_becchu": 0, "prime_becchu": 0, "screwslosher_becchu": 0, "dynamo_becchu": 0,
             "hokusai_becchu": 0, "ochiba": 0, "spygadget_becchu": 0, "l3reelgun_becchu": 0, "52gal_becchu": 0,
             "kugelschreiber_hue": 0, "splatspinner_becchu": 0, "kelvin525_becchu": 0, "furo_deco": 0,
             "rapid_becchu": 0, "explosher_custom": 0, "nautilus79": 0, "sputtery_clear": 0, "h3reelgun_cherry": 0,
             "promodeler_pg": 0, "squiclean_g": 0, "bucketslosher_soda": 0, "longblaster_necro": 0,
             "pablo_permanent": 0, "campingshelter_camo": 0, "nzap83": 0, "barrelspinner_remix": 0, "bamboo14mk3": 0,
             "bold_7": 0}
lose_count = win_count.copy()
total = win_count.copy()
win_rate = win_count.copy()

for period_l, game_ver_l, lobby_mode, lobby, mode_l, stage_l, win, \
    A1_rank, A2_rank, A3_rank, A4_rank, B1_rank, B2_rank, B3_rank, B4_rank, \
    A1_weapon, A2_weapon, A3_weapon, A4_weapon, B1_weapon, B2_weapon, B3_weapon, B4_weapon, \
    A1_inked, A2_inked, A3_inked, A4_inked, B1_inked, B2_inked, B3_inked, B4_inked \
        in zip(df['# period'], df['game-ver'], df['lobby-mode'], df['lobby'], df['mode'], df['stage'], df['win'],
               df['A1-rank'], df['A2-rank'], df['A3-rank'], df['A4-rank'],
               df['B1-rank'], df['B2-rank'], df['B3-rank'], df['B4-rank'],
               df['A1-weapon'], df['A2-weapon'], df['A3-weapon'], df['A4-weapon'],
               df['B1-weapon'], df['B2-weapon'], df['B3-weapon'], df['B4-weapon'],
               df['A1-inked'], df['A2-inked'], df['A3-inked'], df['A4-inked'],
               df['B1-inked'], df['B2-inked'], df['B3-inked'], df['B4-inked']):
    if (lobby_mode == "regular") or (lobby_mode == "fest") or (game_ver_l != game_ver) or \
            (A1_inked is pd.NA) or (A1_inked == 0) or \
            (A2_inked is pd.NA) or (A2_inked == 0) or \
            (A3_inked is pd.NA) or (A3_inked == 0) or \
            (A4_inked is pd.NA) or (A4_inked == 0) or \
            (B1_inked is pd.NA) or (B1_inked == 0) or \
            (B2_inked is pd.NA) or (B2_inked == 0) or \
            (B3_inked is pd.NA) or (B3_inked == 0) or \
            (B4_inked is pd.NA) or (B4_inked == 0):
        continue

    if ('period' in globals()) and not (period in period_l):
        continue

    if (('game_mode_1' in globals()) and (mode_l != game_mode_1)) and \
            ((not ('game_mode_2' in globals())) or (mode_l != game_mode_2)):
        continue

    # if (mode_l != "area") and (mode_l != "yagura") and (mode_l != "hoko") and (mode_l != "asari"):
    #     continue

    if (('stage1' in globals()) and (stage_l != stage1)) and (('stage2' in globals()) and (stage_l != stage2)):
        continue

    # # A帯の場合　10日分ぐらいだとサンプル数少なすぎ
    # if lobby != "standard":
    #     continue
    # if A1_rank is not pd.NA:
    #     if (A1_rank != 'a-') and (A1_rank != 'a') and (A1_rank != 'a+'):
    #         continue
    # elif A2_rank is not pd.NA:
    #     if (A2_rank != 'a-') and (A2_rank != 'a') and (A2_rank != 'a+'):
    #         continue
    # else:
    #     print("A1 and A2 rank is NA. add code")
    #     exit(-1)
    # # if (A3_rank is not pd.NA) and (A3_rank != 'x'):
    # #    continue

    # X帯のみ
    # if lobby != "standard":
    #     continue
    # if A1_rank is not pd.NA:
    #     if A1_rank != 'x':
    #         continue
    # elif A2_rank is not pd.NA:
    #     if A2_rank != 'x':
    #         continue
    # else:
    #     print("A1 and A2 rank is NA. add code")
    #     exit(-1)
    # # if (A3_rank is not pd.NA) and (A3_rank != 'x'):
    # #    continue

    if win == "alpha":
        if (not exclude_a1) and (A1_weapon is not pd.NA):
            win_count[A1_weapon] += 1
        if ((lobby == "standard") or (not exclude_a1)) and (A2_weapon is not pd.NA):
            win_count[A2_weapon] += 1
        if ((lobby != "squad_4") or (not exclude_a1)) and (A3_weapon is not pd.NA):
            win_count[A3_weapon] += 1
        if ((lobby != "squad_4") or (not exclude_a1)) and (A4_weapon is not pd.NA):
            win_count[A4_weapon] += 1
        if B1_weapon is not pd.NA:
            lose_count[B1_weapon] += 1
        if B2_weapon is not pd.NA:
            lose_count[B2_weapon] += 1
        if B3_weapon is not pd.NA:
            lose_count[B3_weapon] += 1
        if B4_weapon is not pd.NA:
            lose_count[B4_weapon] += 1
    else:
        if (not exclude_a1) and (A1_weapon is not pd.NA):
            lose_count[A1_weapon] += 1
        if ((lobby == "standard") or (not exclude_a1)) and (A2_weapon is not pd.NA):
            lose_count[A2_weapon] += 1
        if ((lobby != "squad_4") or (not exclude_a1)) and (A3_weapon is not pd.NA):
            lose_count[A3_weapon] += 1
        if ((lobby != "squad_4") or (not exclude_a1)) and (A4_weapon is not pd.NA):
            lose_count[A4_weapon] += 1
        if B1_weapon is not pd.NA:
            win_count[B1_weapon] += 1
        if B2_weapon is not pd.NA:
            win_count[B2_weapon] += 1
        if B3_weapon is not pd.NA:
            win_count[B3_weapon] += 1
        if B4_weapon is not pd.NA:
            win_count[B4_weapon] += 1

win_count["sshooter"] += win_count["heroshooter_replica"]
win_count["hotblaster"] += win_count["heroblaster_replica"]
win_count["splatroller"] += win_count["heroroller_replica"]
win_count["hokusai"] += win_count["herobrush_replica"]
win_count["splatcharger"] += win_count["herocharger_replica"]
win_count["maneuver"] += win_count["heromaneuver_replica"]
win_count["bucketslosher"] += win_count["heroslosher_replica"]
win_count["barrelspinner"] += win_count["herospinner_replica"]
win_count["parashelter"] += win_count["heroshelter_replica"]
win_count["sshooter_collabo"] += win_count["octoshooter_replica"]

lose_count["sshooter"] += lose_count["heroshooter_replica"]
lose_count["hotblaster"] += lose_count["heroblaster_replica"]
lose_count["splatroller"] += lose_count["heroroller_replica"]
lose_count["hokusai"] += lose_count["herobrush_replica"]
lose_count["splatcharger"] += lose_count["herocharger_replica"]
lose_count["maneuver"] += lose_count["heromaneuver_replica"]
lose_count["bucketslosher"] += lose_count["heroslosher_replica"]
lose_count["barrelspinner"] += lose_count["herospinner_replica"]
lose_count["parashelter"] += lose_count["heroshelter_replica"]
lose_count["sshooter_collabo"] += lose_count["octoshooter_replica"]

del win_count["heroshooter_replica"], win_count["heroblaster_replica"], win_count["heroroller_replica"], \
    win_count["herobrush_replica"], win_count["herocharger_replica"], win_count["heromaneuver_replica"], \
    win_count["heroslosher_replica"], win_count["herospinner_replica"], win_count["heroshelter_replica"], \
    win_count["octoshooter_replica"], \
    lose_count["heroshooter_replica"], lose_count["heroblaster_replica"], lose_count["heroroller_replica"], \
    lose_count["herobrush_replica"], lose_count["herocharger_replica"], lose_count["heromaneuver_replica"], \
    lose_count["heroslosher_replica"], lose_count["herospinner_replica"], lose_count["heroshelter_replica"], \
    lose_count["octoshooter_replica"], \
    win_rate["heroshooter_replica"], win_rate["heroblaster_replica"], win_rate["heroroller_replica"], \
    win_rate["herobrush_replica"], win_rate["herocharger_replica"], win_rate["heromaneuver_replica"], \
    win_rate["heroslosher_replica"], win_rate["herospinner_replica"], win_rate["heroshelter_replica"], \
    win_rate["octoshooter_replica"], \
    win_rate["nan"], win_rate["<NA>"]

for key, value in win_count.items():
    total[key] = value + lose_count[key]
    if total[key] != 0:
        win_rate[key] = value / total[key]

for key, value in sorted(win_rate.items(), key=lambda x: x[1]):
    print(key + ": " + str(value) + " :" + str(total[key]))
