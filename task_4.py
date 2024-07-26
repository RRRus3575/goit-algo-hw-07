class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self, reply):
        if reply in self.replies:
            reply.text = ""
            reply.author = ''
            reply.is_deleted = True

    def display(self, level=0):
        indent = " " * (level * 4)
        if self.is_deleted:
            print(f"{indent} Цей коментар було видалено.")
        else:
            print(f"{indent}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)

# Приклад використання
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# Відображення ієрархії коментарів
print("До видалення:")
root_comment.display()

# Видалення відповіді
root_comment.remove_reply(reply1)

# Відображення ієрархії коментарів після видалення
print("\nПісля видалення:")
root_comment.display()
