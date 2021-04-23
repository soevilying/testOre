


label Ludiko_meet:
    scene tavern 1
    show ludiko happy at center with dissolve
    if Ludiko.meet==False:
        "???" "Я Людико"
        $ Ludiko.meet = True

        jump map1
    elif True:
        l "....Чего ты хочешь"
        jump map1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
