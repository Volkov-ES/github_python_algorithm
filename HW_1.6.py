"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""

""" РЕШЕНИЕ ПРЕПОДАВАТЕЛЯ """

class QueueClass:
    def __init__(self):
        self.elems = []
        
    def is_empty(self):
        return self.elems == []
    
    def to_queue(self, item):
        self.elems.insert(0, item)
        
    def from_queue(self):
        return self.elems.pop()
    
    def size(self):
        return len(self.elems)
    
class TaskBoard:
    def __init__(self):
        self.cur_queue = QueieClass()     # Базовая очередь
        self.revision_queue = QueueClass()     # Очередь на доработку
        self.log = []    # Список решенных задач
        
    def resolve_task(self):
        """Закрываем текущую задачу и добавляем в лог"""
        task = self.cur_queue.from_queue()
        self.log.append(task)
        
    def to_revision_task(self):
        """Отправляем текущую задачу на доработку"""
        task = self.cur_queue.from_queue()
        self.revision_queue.to_queue(task)
        
    def to_current_queue(self, item):
        """Добавляем задачу в текущие"""
        self.cur_queue.to_queue(item)
        
    def from_revision(self):
        """Возвращаем задачу из доработки в текущую очередь"""
        task = self.revision_queue.from_queue()
        self.cur_queue.to_queue(task)
        
    def current_task(self):
        """Текущая задача"""
        return self.cur_queue.elems[len(self.cur_queue.elems) - 1]
    
    def current_revision(self):
        """Задача в доработке"""
        return self.revision_queue.elems[len(self.revision_queue.elems) - 1]
    
if __name__ == '__main__':
    """ЗДЕСЬ ДОЛЖНО БЫТЬ КАКОЕ-ТО ПРОДОЛЖЕНИЕ, НО В ВИДЕО УРОКЕ ЕГО НЕТ,
       МНЕ ОЧЕНЬ ИНТЕРЕСНО ЭТО ПРОДОЛЖЕНИЕ"""
        