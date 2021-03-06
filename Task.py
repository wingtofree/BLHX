# coding: utf-8

import Scene


class Task:
    def __init__(self, game):
        self.game = game

    def run(self):
        pass


class ExerciseTask(Task):
    def __init__(self, game):
        super().__init__(game)

    def run(self):
        mainScene = Scene.MainScene(self.game)
        precombatScene = Scene.PrecombatScene(self.game)
        exerciseScene = Scene.ExerciseScene(self.game)
        battleScene = Scene.BattleScene(self.game)
        mainScene.enterPrecombat()
        precombatScene.enterExercise()
        while True:
            if not exerciseScene.enterExercise():
                break
            battleScene.leaveBattle(False)
        exerciseScene.back()
        precombatScene.back()


class MaidTask(Task):
    def __init__(self, game):
        super().__init__(game)

    def run(self):
        mainScene = Scene.MainScene(self.game)
        maidScene = Scene.MaidScene(self.game)
        battleScene = Scene.BattleScene(self.game)
        if not mainScene.enterMaid():
            return
        while True:
            maidScene.enterExercise()
            battleScene.leaveBattle(False)


class C01S01LoopTask(Task):
    def __init__(self, game):
        super().__init__(game)

    def run(self):
        mainScene = Scene.MainScene(self.game)
        precombatScene = Scene.PrecombatScene(self.game)
        c01s01Scene = Scene.C01S01Scene(self.game)
        battleScene = Scene.BattleScene(self.game)
        mainScene.enterPrecombat()
        if not precombatScene.enterSubcapter(1, 1):
            precombatScene.back()
            return
        while True:
            c01s01Scene.enterAmbush()
            battleScene.enterBattle()
            battleScene.leaveBattle(False)
            c01s01Scene.leaveAmbush()


class C03S04Task(Task):
    def __init__(self, game):
        super().__init__(game)

    def run(self):
        mainScene = Scene.MainScene(self.game)
        precombatScene = Scene.PrecombatScene(self.game)
        c03s04Scene = Scene.C03S04Scene(self.game)
        battleScene = Scene.BattleScene(self.game)
        mainScene.enterPrecombat()
        while True:
            precombatScene.enterSubcapter(3, 4)
            while c03s04Scene.bossExist:
                c03s04Scene.weighAnchor()
                battleScene.enterBattle()
                battleScene.leaveBattle()
