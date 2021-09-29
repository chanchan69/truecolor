def fg(color: any) -> str:
    """
    Returns an ANSI escape code

    :param color: a hex color as a str (ie #123456), a rgb color as a tuple (ie (1,2,3)), or a supported color name as a str (ie magenta)
    """
    if isinstance(color, tuple):
        rgb = color

    elif isinstance(color, str) and color.__contains__("#"):
        rgb = hex_to_rgb(color)

    elif isinstance(color, str) and not color.__contains__("#"):
        rgb = name_to_rgb(color)
    else:
        return ""

    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    return f"\033[38;2;{r};{g};{b}m"


def hex_to_rgb(hex_code: str) -> list:
    return [int(hex_code[i:i + 2], 16) for i in range(1, 6, 2)]


def name_to_rgb(name: str) -> tuple:
    color_names = dict(black=(0, 0, 0), red=(128, 0, 0), green=(0, 128, 0), yellow=(128, 128, 0), blue=(0, 0, 128),
                       magenta=(128, 0, 128), cyan=(0, 128, 128), light_gray=(192, 192, 192), dark_gray=(128, 128, 128),
                       light_red=(255, 0, 0), light_green=(0, 255, 0), light_yellow=(255, 255, 0),
                       light_blue=(0, 0, 255), light_magenta=(255, 0, 255), light_cyan=(0, 255, 255),
                       white=(255, 255, 255), grey_0=(0, 0, 0), navy_blue=(0, 0, 95), dark_blue=(0, 0, 135),
                       blue_3a=(0, 0, 175), blue_3b=(0, 0, 215), blue_1=(0, 0, 255), dark_green=(0, 95, 0),
                       deep_sky_blue_4a=(0, 95, 95), deep_sky_blue_4b=(0, 95, 135), deep_sky_blue_4c=(0, 95, 175),
                       dodger_blue_3=(0, 95, 215), dodger_blue_2=(0, 95, 255), green_4=(0, 135, 0),
                       spring_green_4=(0, 135, 95), turquoise_4=(0, 135, 135), deep_sky_blue_3a=(0, 135, 175),
                       deep_sky_blue_3b=(0, 135, 215), dodger_blue_1=(0, 135, 255), green_3a=(0, 175, 0),
                       spring_green_3a=(0, 175, 95), dark_cyan=(0, 175, 135), light_sea_green=(0, 175, 175),
                       deep_sky_blue_2=(0, 175, 215), deep_sky_blue_1=(0, 175, 255), green_3b=(0, 215, 0),
                       spring_green_3b=(0, 215, 95), spring_green_2a=(0, 215, 135), cyan_3=(0, 215, 175),
                       dark_turquoise=(0, 215, 215), turquoise_2=(0, 215, 255), green_1=(0, 255, 0),
                       spring_green_2b=(0, 255, 95), spring_green_1=(0, 255, 135), medium_spring_green=(0, 255, 175),
                       cyan_2=(0, 255, 215), cyan_1=(0, 255, 255), dark_red_1=(95, 0, 0), deep_pink_4a=(95, 0, 95),
                       purple_4a=(95, 0, 135), purple_4b=(95, 0, 175), purple_3=(95, 0, 215), blue_violet=(95, 0, 255),
                       orange_4a=(95, 95, 0), grey_37=(95, 95, 95), medium_purple_4=(95, 95, 135),
                       slate_blue_3a=(95, 95, 175), slate_blue_3b=(95, 95, 215), royal_blue_1=(95, 95, 255),
                       chartreuse_4=(95, 135, 0), dark_sea_green_4a=(95, 135, 95), pale_turquoise_4=(95, 135, 135),
                       steel_blue=(95, 135, 175), steel_blue_3=(95, 135, 215), cornflower_blue=(95, 135, 255),
                       chartreuse_3a=(95, 175, 0), dark_sea_green_4b=(95, 175, 95), cadet_blue_2=(95, 175, 135),
                       cadet_blue_1=(95, 175, 175), sky_blue_3=(95, 175, 215), steel_blue_1a=(95, 175, 255),
                       chartreuse_3b=(95, 215, 0), pale_green_3a=(95, 215, 95), sea_green_3=(95, 215, 135),
                       aquamarine_3=(95, 215, 175), medium_turquoise=(95, 215, 215), steel_blue_1b=(95, 215, 255),
                       chartreuse_2a=(95, 255, 0), sea_green_2=(95, 255, 95), sea_green_1a=(95, 255, 135),
                       sea_green_1b=(95, 255, 175), aquamarine_1a=(95, 255, 215), dark_slate_gray_2=(95, 255, 255),
                       dark_red_2=(135, 0, 0), deep_pink_4b=(135, 0, 95), dark_magenta_1=(135, 0, 135),
                       dark_magenta_2=(135, 0, 175), dark_violet_1a=(135, 0, 215), purple_1a=(135, 0, 255),
                       orange_4b=(135, 95, 0), light_pink_4=(135, 95, 95), plum_4=(135, 95, 135),
                       medium_purple_3a=(135, 95, 175), medium_purple_3b=(135, 95, 215), slate_blue_1=(135, 95, 255),
                       yellow_4a=(135, 135, 0), wheat_4=(135, 135, 95), grey_53=(135, 135, 135),
                       light_slate_grey=(135, 135, 175), medium_purple=(135, 135, 215),
                       light_slate_blue=(135, 135, 255), yellow_4b=(135, 175, 0), dark_olive_green_3a=(135, 175, 95),
                       dark_green_sea=(135, 175, 135), light_sky_blue_3a=(135, 175, 175),
                       light_sky_blue_3b=(135, 175, 215), sky_blue_2=(135, 175, 255), chartreuse_2b=(135, 215, 0),
                       dark_olive_green_3b=(135, 215, 95), pale_green_3b=(135, 215, 135),
                       dark_sea_green_3a=(135, 215, 175), dark_slate_gray_3=(135, 215, 215), sky_blue_1=(135, 215, 255),
                       chartreuse_1=(135, 255, 0), light_green_2=(135, 255, 95), light_green_3=(135, 255, 135),
                       pale_green_1a=(135, 255, 175), aquamarine_1b=(135, 255, 215), dark_slate_gray_1=(135, 255, 255),
                       red_3a=(175, 0, 0), deep_pink_4c=(175, 0, 95), medium_violet_red=(175, 0, 135),
                       magenta_3a=(175, 0, 175), dark_violet_1b=(175, 0, 215), purple_1b=(175, 0, 255),
                       dark_orange_3a=(175, 95, 0), indian_red_1a=(175, 95, 95), hot_pink_3a=(175, 95, 135),
                       medium_orchid_3=(175, 95, 175), medium_orchid=(175, 95, 215), medium_purple_2a=(175, 95, 255),
                       dark_goldenrod=(175, 135, 0), light_salmon_3a=(175, 135, 95), rosy_brown=(175, 135, 135),
                       grey_63=(175, 135, 175), medium_purple_2b=(175, 135, 215), medium_purple_1=(175, 135, 255),
                       gold_3a=(175, 175, 0), dark_khaki=(175, 175, 95), navajo_white_3=(175, 175, 135),
                       grey_69=(175, 175, 175), light_steel_blue_3=(175, 175, 215), light_steel_blue=(175, 175, 255),
                       yellow_3a=(175, 215, 0), dark_olive_green_3=(175, 215, 95), dark_sea_green_3b=(175, 215, 135),
                       dark_sea_green_2=(175, 215, 175), light_cyan_3=(175, 215, 215), light_sky_blue_1=(175, 215, 255),
                       green_yellow=(175, 255, 0), dark_olive_green_2=(175, 255, 95), pale_green_1b=(175, 255, 135),
                       dark_sea_green_5b=(175, 255, 175), dark_sea_green_5a=(175, 255, 215),
                       pale_turquoise_1=(175, 255, 255), red_3b=(215, 0, 0), deep_pink_3a=(215, 0, 95),
                       deep_pink_3b=(215, 0, 135), magenta_3b=(215, 0, 175), magenta_3c=(215, 0, 215),
                       magenta_2a=(215, 0, 255), dark_orange_3b=(215, 95, 0), indian_red_1b=(215, 95, 95),
                       hot_pink_3b=(215, 95, 135), hot_pink_2=(215, 95, 175), orchid=(215, 95, 215),
                       medium_orchid_1a=(215, 95, 255), orange_3=(215, 135, 0), light_salmon_3b=(215, 135, 95),
                       light_pink_3=(215, 135, 135), pink_3=(215, 135, 175), plum_3=(215, 135, 215),
                       violet=(215, 135, 255), gold_3b=(215, 175, 0), light_goldenrod_3=(215, 175, 95),
                       tan=(215, 175, 135), misty_rose_3=(215, 175, 175), thistle_3=(215, 175, 215),
                       plum_2=(215, 175, 255), yellow_3b=(215, 215, 0), khaki_3=(215, 215, 95),
                       light_goldenrod_2a=(215, 215, 135), light_yellow_3=(215, 215, 175), grey_84=(215, 215, 215),
                       light_steel_blue_1=(215, 215, 255), yellow_2=(215, 255, 0), dark_olive_green_1a=(215, 255, 95),
                       dark_olive_green_1b=(215, 255, 135), dark_sea_green_1=(215, 255, 175),
                       honeydew_2=(215, 255, 215), light_cyan_1=(215, 255, 255), red_1=(255, 0, 0),
                       deep_pink_2=(255, 0, 95), deep_pink_1a=(255, 0, 135), deep_pink_1b=(255, 0, 175),
                       magenta_2b=(255, 0, 215), magenta_1=(255, 0, 255), orange_red_1=(255, 95, 0),
                       indian_red_1c=(255, 95, 95), indian_red_1d=(255, 95, 135), hot_pink_1a=(255, 95, 175),
                       hot_pink_1b=(255, 95, 215), medium_orchid_1b=(255, 95, 255), dark_orange=(255, 135, 0),
                       salmon_1=(255, 135, 95), light_coral=(255, 135, 135), pale_violet_red_1=(255, 135, 175),
                       orchid_2=(255, 135, 215), orchid_1=(255, 135, 255), orange_1=(255, 175, 0),
                       sandy_brown=(255, 175, 95), light_salmon_1=(255, 175, 135), light_pink_1=(255, 175, 175),
                       pink_1=(255, 175, 215), plum_1=(255, 175, 255), gold_1=(255, 215, 0),
                       light_goldenrod_2b=(255, 215, 95), light_goldenrod_2c=(255, 215, 135),
                       navajo_white_1=(255, 215, 175), misty_rose1=(255, 215, 215), thistle_1=(255, 215, 255),
                       yellow_1=(255, 255, 0), light_goldenrod_1=(255, 255, 95), khaki_1=(255, 255, 135),
                       wheat_1=(255, 255, 175), cornsilk_1=(255, 255, 215), grey_100=(255, 255, 255), grey_3=(8, 8, 8),
                       grey_7=(18, 18, 18), grey_11=(28, 28, 28), grey_15=(38, 38, 38), grey_19=(48, 48, 48),
                       grey_23=(58, 58, 58), grey_27=(68, 68, 68), grey_30=(78, 78, 78), grey_35=(88, 88, 88),
                       grey_39=(98, 98, 98), grey_42=(108, 108, 108), grey_46=(118, 118, 118), grey_50=(128, 128, 128),
                       grey_54=(138, 138, 138), grey_58=(148, 148, 148), grey_62=(158, 158, 158),
                       grey_66=(168, 168, 168), grey_70=(178, 178, 178), grey_74=(188, 188, 188),
                       grey_78=(198, 198, 198), grey_82=(208, 208, 208), grey_85=(218, 218, 218),
                       grey_89=(228, 228, 228))

    return color_names[name]