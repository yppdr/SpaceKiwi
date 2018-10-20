from pygame import *

from random import *

class EnemiesGroup(sprite.Group):
    def __init__(self, columns, rows):
        sprite.Group.__init__(self)
        self.enemies = [[0] * columns for _ in range(rows)]
        self.columns = columns
        self.rows = rows
        self.leftAddMove = 0
        self.rightAddMove = 0
        self._aliveColumns = list(range(columns))
        self._leftAliveColumn = 0
        self._rightAliveColumn = columns - 1
        self._leftKilledColumns = 0
        self._rightKilledColumns = 0

    def add(self, *sprites):
        super(sprite.Group, self).add(*sprites)

        for s in sprites:
            self.enemies[s.row][s.column] = s

    def is_column_dead(self, column):
        for row in range(self.rows):
            if self.enemies[row][column]:
                return False
        return True

    def random_bottom(self):
        random_index = randint(0, len(self._aliveColumns) - 1)
        col = self._aliveColumns[random_index]
        for row in range(self.rows, 0, -1):
            enemy = self.enemies[row - 1][col]
            if enemy:
                return enemy
        return None

    def kill(self, enemy):
        # on double hit calls twice for same enemy, so check before
        if not self.enemies[enemy.row][enemy.column]:
            return  # nothing to kill

        self.enemies[enemy.row][enemy.column] = None
        isColumnDead = self.is_column_dead(enemy.column)
        if isColumnDead:
            self._aliveColumns.remove(enemy.column)

        if enemy.column == self._rightAliveColumn:
            while self._rightAliveColumn > 0 and isColumnDead:
                self._rightAliveColumn -= 1
                self._rightKilledColumns += 1
                self.rightAddMove = self._rightKilledColumns * 5
                isColumnDead = self.is_column_dead(self._rightAliveColumn)

        elif enemy.column == self._leftAliveColumn:
            while self._leftAliveColumn < self.columns and isColumnDead:
                self._leftAliveColumn += 1
                self._leftKilledColumns += 1
                self.leftAddMove = self._leftKilledColumns * 5
                isColumnDead = self.is_column_dead(self._leftAliveColumn)
