


label Ludiko_meet:
    scene tavern 1
    show ludiko happy at center with dissolve
    if Ludiko.meet==False:
        "???" "I'm Ludiko"
        $ Ludiko.meet = True

        jump map1
    elif True:
        l "....what do you want"
        jump map1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
