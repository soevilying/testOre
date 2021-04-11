













define config.name = _("Tavern of Spear")




define gui.show_name = True




define config.version = "v0.14d"





define gui.about = _p("""
""")





define build.name = "Tavern_of_Spear"



define build.itch_project = "fd-caro/6464"


define config.has_sound = True
define config.has_music = True
define config.has_voice = True





















define config.language = 'English'
define config.enter_transition = dissolve
define config.exit_transition = dissolve

define config.default_music_volume = 0.0
define config.default_sfx_volume = 0.8
define config.default_voice_volume = 0.8
define config.fade_music = 0.5


define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None















define config.window = "auto"
define config.developer = True



define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)






default preferences.text_cps = 0




default preferences.afm_time = 15














define config.save_directory = "Tvern_of_Spear-1"





define config.window_icon = "gui/window_icon.png"





init python:
















    renpy.music.register_channel("Axel", "music", True)
    renpy.music.register_channel("Chet", "music", True)
    renpy.music.register_channel("Hakan", "music", True)
    renpy.music.register_channel("Ludiko", "music", True)
    renpy.music.register_channel("Meko", "music", True)
    renpy.music.register_channel("Nauxus", "music", True)
    renpy.music.register_channel("Snow", "music", True)
    renpy.music.register_channel("Thane", "music", True)
    renpy.music.register_channel("Witer", "music", True)
    renpy.music.register_channel("Selye", "music", True)
    renpy.music.register_channel("Eyvind", "music", True)
    renpy.music.register_channel("Ebb", "music", True)
    renpy.music.register_channel("Flo", "music", True)
    renpy.music.register_channel("Chan1", "music", True)
    renpy.music.register_channel("Chan2", "music", True)
    renpy.music.register_channel("Chan3", "music", True)

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.png', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpyc', 'archive')








    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
