image bg pink = "#ffb3b3"
image bg green = "#c3ffb1"
image bg yellow = "#fbffb7"
image bg blue = "#b1e3ff"
define numbers = "0123456789"

label createlog:

    init python:

        tasks = [ ]


        goals = [ ]
        stages = [ ]

        goals.append(Goal("peter", "Find and help Peter"))
        goals.append(Goal("paul", "Find and help Paul"))
        goals.append(Goal("mary", "Find and help Mary"))
        goals.append(Goal("finish", "Return to Eileen for your reward"))

        stages.append(Stage("peter,paul,mary", "atlast"))
        stages.append(Stage("finish"))

        tasks.append(Task("Eileen's Task",
            "Help Eileen out by helping out her friends Peter, Paul, and Mary who are each in different rooms.  Eileen is in the pink room.",
            "TutorialOWO",
            goals,
            stages))


        goals = [ ]
        stages = [ ]

        goals.append(Goal("survey", "Talk to Mary"))
        goals.append(Goal("tattle", "Tell Mary that Paul sent you. {size=10}(optional){/size}", required=False))
        goals.append(Goal("truth", "Return to Paul with Mary's note"))
        goals.append(Goal("lie", "Return to Paul with the finished survey"))


        stages.append(Stage("survey,tattle", next="truth"))
        stages.append(Stage("truth", id="truth", next=False))
        stages.append(Stage("lie", id="lie", next=False))

        tasks.append(Task("Paul's Task",
            "Help Paul out by taking the survey to Mary for him.  Paul is in the yellow room.",
            "Tutorial",
            goals,
            stages))


        goals = [ ]
        stages = [ ]

        goals.append(Goal("pinkbush", "Search the bushes in the pink room"))
        goals.append(Goal("greenbush", "Search the bushes in the green room"))
        goals.append(Goal("yellowbush", "Search the bushes in the yellow room"))
        goals.append(Goal("pinktalk", "Ask Eileen about Mary's glasses"))
        goals.append(Goal("greentalk", "Ask Peter about Mary's glasses"))
        goals.append(Goal("yellowtalk", "Ask Paul about Mary's glasses"))
        goals.append(Goal("marytalk", "Return to Mary and tell her the results of your search"))

        stages.append(Stage("pinkbush,greenbush,yellowbush","searchfailed"))
        stages.append(Stage("pinktalk,greentalk,yellowtalk",
            "failedagain",
            "Searching the bushes didn't turn anything up.  Talk to everyone to see if they have seen Mary's glasses."))
        stages.append(Stage("marytalk",
            "success",
            "Talking to people and searching the bushes have both been a fantastic waste of time.  It's time to return to Mary in the blue room."))

        tasks.append(Task("Mary's Task",
            "Help Mary by finding her glasses.  Start by searching the bushes in each room.  Mary is in the blue room.",
            "Tutorial",
            goals,
            stages))



        goals = [ ]
        stages = [ ]

        goals.append(Goal("book", "Talk to Eileen to get Peter's math book", 0, 1))
        goals.append(Goal("return", "Return the book to Peter"))
        goals.append(Goal("math", "Solve 3 math problems for Peter", 0, 3))

        stages.append(Stage("book"))
        stages.append(Stage("return"))
        stages.append(Stage("math"))

        tasks.append(Task("Peter's Task",
            "Peter wants you to help him find his math book.  Eileen may know where it is.  Peter hangs out in the green room.",
            "Tutorial",
            goals,
            stages))

        log = Tasklog(tasks, "qlog", "qkey")

        del goals
        del tasks
        del stages

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
