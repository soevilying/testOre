screen statspick:

    default str = 3
    default agi = 3
    default int = 3
    default end = 3
    default cha = 3
    default n = 9
    frame:
        xalign 0.5 ypos 0.2
        has vbox:
            spacing 20
        text "-STR:[str]"
        text "-AGI:[agi]"
        text "-INT:[int]"
        text "-END:[end]"
        text "-CHA:[cha]"
        text "POINTS:[n]"



    frame:
        xalign 0.55 ypos 0.2
        has vbox
        if str>=10:
            textbutton "+"
        elif n<=0:
            textbutton "+"
        else:
            textbutton "+" action (SetScreenVariable("str",str+1),SetScreenVariable("n",n-1))
        if agi>=10:
            textbutton "+"
        elif n<=0:
            textbutton "+"
        else:
            textbutton "+" action (SetScreenVariable("agi",agi+1),SetScreenVariable("n",n-1))
        if int>=10:
            textbutton "+"
        elif n<=0:
            textbutton "+"
        else:
            textbutton "+" action (SetScreenVariable("int",int+1),SetScreenVariable("n",n-1))
        if end>=10:
            textbutton "+"
        elif n<=0:
            textbutton "+"
        else:
            textbutton "+" action (SetScreenVariable("end",end+1),SetScreenVariable("n",n-1))
        if cha>=10:
            textbutton "+"
        elif n<=0:
            textbutton "+"
        else:
            textbutton "+" action (SetScreenVariable("cha",cha+1),SetScreenVariable("n",n-1))
    frame:
        xalign 0.45 ypos 0.2
        has vbox
        if str<=3:
            textbutton "-"
        elif n>=10:
            textbutton "-"
        else:
            textbutton "-" action (SetScreenVariable("str",str-1),SetScreenVariable("n",n+1))
        if agi<=3:
            textbutton "-"
        elif n>=10:
            textbutton "-"
        else:
            textbutton "-" action (SetScreenVariable("agi",agi-1),SetScreenVariable("n",n+1))
        if int<=3:
            textbutton "-"
        elif n>=10:
            textbutton "-"
        else:
            textbutton "-" action (SetScreenVariable("int",int-1),SetScreenVariable("n",n+1))
        if end<=3:
            textbutton "-"
        elif n>=10:
            textbutton "-"
        else:
            textbutton "-" action (SetScreenVariable("end",end-1),SetScreenVariable("n",n+1))
        if cha<=3:
            textbutton "-"
        elif n>=10:
            textbutton "-"
        else:
            textbutton "-" action (SetScreenVariable("cha",cha-1),SetScreenVariable("n",n+1))
    frame:
        xalign 0.5 ypos 0.6
        has vbox:
            spacing 20
        textbutton _("Go"):
            action (Return ("start_1"),SetVariable("Zalt.str",str),SetVariable("Zalt.agi",agi),SetVariable("Zalt.int",int),SetVariable("Zalt.end",end),SetVariable("Zalt.cha",cha))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
