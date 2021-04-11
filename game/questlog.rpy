


init python:

    import renpy.store as store
    import renpy.exports as renpy

    class Link(store.object):      
        pass




    class Goal(Link):
        def __init__(self,
            id='no name',
            description='no description',
            start=0,
            max=0,
            required=True,
            hidden=False
            ):
            
            self.id(id)
            self.description(description)
            self.required(required)
            self.hidden(hidden)
            self.fetch(max, start)
            self.completed(False)
            self.active(False)
        
        
        
        
        def active(self, flag=None):
            if flag != None:
                self._active = flag
            return self._active
        
        
        
        def inactive(self):
            return not self._active
        
        
        
        def interactive(self):
            return self.active() and not self.completed()
        
        
        
        def id(self, str=None):
            if str:
                self._id = str
            return self._id
        
        
        
        def description(self, str=None):
            if str:
                self._description = str
            return self._description
        
        
        
        def required(self, req=None):
            if req != None:
                self._required = req
            return self._required
        
        
        
        def hidden(self, flag=None):
            if flag != None:
                self._hidden = flag
            return self._hidden
        
        def fetch(self, max=None, start=0):
            if max != None:
                self._need = max
                self._have = start
                return True
            else:
                return self.need() != 0
        
        def remaining(self):
            if self.fetch():
                return self.need() - self.have()
            return False
        
        def need(self):
            return self._need
        
        def have(self):
            return self._have
        
        def find(self, value=1):
            ret = self._have
            self._have += value
            
            self._completecheck()
            return ret
        
        def lose(self, value=1):
            return self.find(value*-1)
        
        def completed(self, flag=None):
            if flag != None:
                self._completed = flag
            return self._completed
        
        def _completecheck(self):
            if self.fetch():
                if self.remaining() <= 0:
                    self.completed(True)




    class Stage(Link):
        def __init__(self,
            triggers=None,
            post=None,
            description=None,
            id=None,
            next=None,
            notification=None):
            
            self._id = id
            self._triggers = triggers
            self._post = post
            self._next = next
            self._notification = notification
            self._description = description
        
        def description(self, str=None):
            if str:
                self._description = str
            return self._description
        
        def id(self, id=None):
            if id:
                self._id = id
            return self._id
        
        def triggers(self, triggers=None):
            if triggers:
                self._triggers = triggers
            return self._triggers
        
        def post(self, post=None):
            if post:
                self._post = post
            return self._post
        
        def next(self, next=None):
            if next != None:
                self._next = next
            return self._next
        
        def notification(self, notify=None):
            if notify:
                self._notification = notify
            return self._notification





    class Task(Link):
        def __init__(self,
            title='no title',
            description='no description',
            tab=None,
            goals=None,
            stages=[ ],
            id=None,
            image=None,
            hidden=True,
            end=None):
            
            self._completed = False
            self._label = end
            self._image = image
            self._tab = tab
            self._tracked = False
            self._goalnames = [ ]
            self._stages = { }
            self._stage = None
            self._firststage = None
            self._cleargoals()
            self.id(id or title)
            self.img(image)
            self.title(title)
            self.hidden(hidden)
            self.description(description)
            self.addgoals(goals)
            self.addstages(stages)
        
        def activate(self, str=None):
            self._changeactivity(str, True)
            self.hidden(False)
        
        def deactivate(self, str=None):
            self._changeactivity(str, False)
        
        def _changeactivity(self, str, bool):
            if str:
                list = str.split(',')
                
                for i in list:
                    self.goal(i).active(bool)
        
        def id(self, str=None):
            if str:
                self._id = str
            return self._id
        
        def interactive(self, str=None):
            list = str.split(',')
            ret = True
            
            for i in list:
                ret = ret and self.goal(i).interactive()
            
            return ret
        
        def tab(self, str=None):
            if str:
                self._tab = str
            return self._tab
        
        def title(self, str=None):
            if str:
                self._title = str
            return self._title
        
        def orderedgoals(self):             
            list = [ ]                      
            for i in self._goalnames:       
                j = self.goal(i)
                
                if j.active():
                    if not j.hidden():
                        list.append(j)
                    else:
                        if j.required():
                            list.append(j)
            
            return list
        
        def description(self, str=None):
            if str:
                self._description = str
            return self._description
        
        def goal(self, str=None):
            if str in self._goals.keys():
                return self._goals[str]
            return None
        
        def goals(self, goals=None):
            if goals:
                for i in goals:
                    self.addgoal(i)
            return self._goals.values()
        
        def img(self, image=None):
            if image:
                self._image = image
            return self._image
        
        def label(self, label=None):
            if label:
                self._label = label
            return self._label
        
        def addgoal(self, goal=None):
            if goal:
                self._goals[goal.id()] = goal
                self._goalnames.append(goal.id())
        
        def addgoals(self, list=None):
            if list:
                for i in list:
                    self.addgoal(i)
        
        def _cleargoals(self):
            self._goals = { }
        
        def find(self, str=None, value=1):
            if str in self._goals.keys():
                self._goals[str].find(value)
                return self._completecheck()
            return False
        
        def lose(self, str=None, value=1):
            if str in self._goals.keys():
                self._goals[str].find(value*-1)
        
        def goaldone(self, str=None, flag=True):
            if str in self._goals.keys():
                self._goals[str].completed(flag)
                return self._completecheck()
            return False
        
        def hidden(self, flag=None):
            if flag != None:
                self._hidden = flag
            return self._hidden
        
        def tracked(self, flag=None):
            if flag!=None:
                self._tracked = flag
            return self._tracked
        
        def addstage(self, stage):
            if not self._firststage:
                self._firststage = stage.id()
            self._stages[stage.id()] = stage
        
        def addstages(self, list):
            i = 0
            while i < len(list):
                j = list[i]
                if not j.id():
                    j.id('stage'+str(i))
                if j.next() == None:
                    if i+1<len(list):
                        j.next('stage'+str(i+1))
                self.addstage(j)
                i += 1
        
        def stage(self, stage=None):
            if stage in self._stages.keys():
                self._stage = self._stages[stage]
            return self._stage
        
        def completed(self):
            return self._completed
        
        def _completecheck(self):
            ret = True
            
            list = self._goals.values()
            
            for i in list:
                if i.active() and i.required():
                    ret = ret and i.completed()
            
            return ret
        
        def hasgoal(self, goal):
            return goal in self._goalnames
        
        def hasstage(self, stage):
            return stage in self._stages.keys()






    class Tasklog(Link):
        def __init__(self,
            tasks=None,
            screen=None,
            key=None,
            enabled=False,
            notify="notification",
            tracker="tracker",
            completion="Completed"):
            
            self._tasks = { }
            self._tabs = [ ]
            self._notify = None
            self._screen = screen
            self._key = key
            self._tracked = None
            self.qvar = None
            self.tvar = None
            self._completiontab = completion
            self.tracker(tracker)
            self.notifyimage(notify)
            self.enabled(enabled)
            self.addtasks(tasks)
        
        def activate(self, str):
            words = str.split()
            word = words[0]
            
            q = self._findtask(word)
            if q:
                q.activate(str)
        
        def deactivate(self, str):
            words = str.split()
            word = words[0]
            
            q = self._findtask(word)
            
            if q:
                q.deactivate(str)
        
        def addtask(self, task=None, tab=None):
            if task:
                i = tab or task.tab()
                if i not in self._tasks.keys():
                    self._tabs.append(i)
                    self._tasks[i] = [ ]
                
                self._tasks[i].append(task)
                
                if not self.qvar:
                    self.qvar = task
                    self.tvar = i
        
        def addtasks(self, tasks=None):
            if tasks:
                for i in tasks:
                    self.addtask(i)
        
        def emptytab(self, tab):
            return len(self.tab(tab)) == 0
        
        def tab(self, tab=None):
            if tab:
                return self._tasks[tab]
            return self.tvar
        
        def cleartab(self, tab=None):
            if tab:
                if tab in self._tasks.keys():
                    del self._tasks[tab]
        
        def newtab(self):                           
            list = self._tasks[self.tvar]          
            
            ret = None
            
            for i in list:
                if not i.hidden() and ret == None:
                    ret = i
            
            self.qvar = ret
        
        def _nextstage(self, task):
            stage = task.stage()
            str = stage.post()
            next = stage.next()
            
            
            if next:
                stage = task.stage(next)
                
                
                task.activate(stage.triggers())
                
                
                task.description(stage.description())
                
                
                if stage.notification():
                    self.notify(stage.notification())
                elif stage.notification()==None:
                    self.notify('"'+task.title()+'" goals updated')
            
            
            else:
                
                task._completed = True
                
                if self._completiontab:
                    self.movetask(task, self._completiontab)
                else:
                    task.hidden(True)
                    q = self._firsttask()
                    if q:
                        self.qvar = q
                        self.tvar = q.tab()
                    else:
                        self.keyoff()
                
                if stage.notification():
                    self.notify(stage.notification())
                elif stage.notification()==None:
                    self.notify('"'+task.title()+'" completed')
            
            
            if str:
                if renpy.has_label(str):
                    renpy.call(str)
        
        def _firsttask(self):
            for i in self._tasks:
                for task in self._tasks[i]:
                    if not task.completed() and not task.hidden():
                        return task
        
        def find(self, item, value=1, task=None):
            q = task
            
            if not q:
                q = self._findtask(item)
            
            if q.find(item, value):
                self._nextstage(q)
        
        def markdone(self, goal, task=None):
            q = task
            
            if not q:
                q = self._findtask(goal)
            
            if q.goaldone(goal):
                self._nextstage(q)
        
        def interactive(self, goals, task=None):
            words = goals.split()
            word = words[0]
            
            q = task
            
            if not q:
                q = self._findtask(word)
            
            return q.interactive(goals)
        
        def completed(self, str):  
            q = self.task(str)
            
            
            if q:
                return q.completed()
            
            q = self._findtask(str)
            
            if q:
                return q.goal(str).completed()
            
            return False
        
        def have(self, item):
            q = self._findtask(item)
            
            return q.goal(item).have()
        
        def _findtask(self, goal=None, qid=None, stage=None):  
            for list in self._tasks.values():
                for item in list:
                    if goal and item.hasgoal(goal):
                        return item
                    if qid and item.id() == qid:
                        return item
                    if stage and item.hasstage(stage):
                        return item
            
            return None
        
        def setnext(self, str):
            q = self._findtask(stage=str)
            
            if q:
                q.stage().next(str)
        
        def task(self, qid):
            return self._findtask(qid=qid)
        
        def assign(self, qid=None):               
            task = self.task(qid)
            
            stage = task.stage(task._firststage)
            
            task.activate(stage.triggers())
            
            if stage.notification():
                self.notify(stage.notification())
            elif stage.notification()==None:
                self.notify('You have received "'+task.title()+'"')
        
        def allhidden(self, tab):
            ret = True
            list = self._tasks[tab]
            
            for i in list:
                ret = ret and i.hidden()
            
            return ret
        
        def stoptracking(self):
            q = self.qvar
            
            q.tracked(False)
            self._tracked = None
        
        def track(self, task=None):
            
            q = task or self.qvar
            
            q.tracked(True)
            if self._tracked:
                self._tracked.tracked(False)
            self._tracked = q
        
        def tracked(self):
            return self._tracked
        
        def tracker(self, str=None):
            if str:
                self._tracker = str
            return self._tracker
        
        def displayedtabs(self):
            list = self._tabs
            ret = [ ]
            
            for i in list:
                if not log.emptytab(i) and not log.allhidden(i):
                    ret.append(i)
            return ret
        
        def removetask(self, task, tab):
            list = self._tasks[tab]
            k = None
            i = 0
            
            while i < len(list):
                if list[i] == task and k == None:
                    k = i
                i += 1
            
            del self._tasks[tab][k]
        
        def movetask(self, task, finish):
            self.addtask(task, finish)
            self.removetask(task, task.tab())
            if self.qvar == task:
                self.tvar = finish
        
        def screen(self, screen=None):
            if screen:
                self._screen = screen
            return self._screen
        
        def key(self, key=None):
            if key:
                self._screen = key
            return self._key
        
        def keyon(self):
            self.enable()
            if self.key():
                renpy.show_screen(self.key())
        
        def keyoff(self):
            self.disable()
            if self.key():
                renpy.hide_screen(self.key())
        
        def show(self):
            renpy.show_screen(self.screen())
        
        def enabled(self, flag=None):
            if flag != None:
                self._enabled = flag
            return self._enabled
        
        def enable(self):
            self.enabled(True)
        
        def disable(self):
            self.enabled(False)
        
        def notifyimage(self, img=None):
            if img:
                self._notifyimage = img
            return self._notifyimage
        
        def notify(self, str=None, img=None):
            self.message(str)
            renpy.show(img or self.notifyimage())
        
        def message(self, str=None):
            if str:
                self._notify = str
            return self._notify
        
        def activetab(self, show_hidden=False):
            list = self.tab(self.tvar)
            ret = [ ]
            
            for i in list:
                if show_hidden or not i.hidden():
                    ret.append(i)
            
            return ret
        
        def activedescription(self):
            return self.qvar.description()
        
        def activeimage(self):
            return self.qvar.img()
        
        def trackable(self):
            return not self.qvar.tracked() and not self.qvar.completed()
        
        def trackerprogress(self):
            return self.tracked().orderedgoals()
        
        def activeprogress(self):
            return self.qvar.orderedgoals()
        
        def trackedtitle(self):
            return self.tracked().title()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
