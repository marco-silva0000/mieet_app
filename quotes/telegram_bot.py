import os
import telegram
from telegram.ext import Updater, CommandHandler
import random
import logging


def echo(bot, update, args):
    args = "".join(args)
    update.message.reply_text(f"user said:{args}")


def start(bot, update, *args, **kwargs):
    update.message.reply_text("I'm a bot, please talk to me!")


def bear(bot, update):
    from image_search import bear_search
    update.message.reply_text(bear_search())

# start_handler = CommandHandler('start', start)
# bear_handler = CommandHandler(['bear', 'urso', '🐻', '🧸', '🐨'], bear)
# updater.dispatcher.add_handler(CommandHandler("test", echo, pass_args=True))
# updater.dispatcher.add_handler(start_handler)
# updater.dispatcher.add_handler(bear_handler)


def random_quote(update, context):
    from quotes.models import Quote
    quote = Quote.random_quote()
    update.message.reply_text(str(quote))


def quote_from_author(update, context, author):
    print(f'will quote from author={author}')
    from quotes.models import Quote
    quote = Quote.from_author(author)
    print(f'quote:{quote}')
    update.message.reply_text(str(quote))


def author_command(update, context):
    from quotes.models import Author
    print('author command')
    if len(context.args):
        print('len is something')
        if context.args[0] == 'add':
            if len(context.args) > 2:
                author = Author.objects.create(key=context.args[1], name=" ".join(context.args[2:]), is_validated=False)
                update.message.reply_text(f"added author with key:{author.key} name:{author.name}")
            else:
                update.message.reply_text(f"too few arguments, please use ['add', 'value_for_key', 'valus for ful name']")
        else:
            update.message.reply_text(f"unrecognised command, use ['add', 'value_for_key', 'valus for ful name']")
    else:
        message = Author.list()
        update.message.reply_text(message)


def quote_command(update, context):
    from quotes.models import Author, Quote
    print("will get quote")
    print(update.__dict__)
    print(context.__dict__)
    if len(context.args):
        print('len is something')
        if context.args[0] == 'add':
            print('is add')
            if len(context.args) == 2:
                print('no author')
                Quote.objects.add(message=context.args[1])
                update.message.reply_text("Added quote without author")
            else:
                print('author')
                try:
                    author = Author.objects.get(key=context.args[1])
                    print(f'author={author}')
                    q = Quote.objects.create(author=author, text=" ".join(context.args[2:]), is_validated=False)
                    print(f'quote={q}')
                    update.message.reply_text(f"added quote for author {author}")
                except Author.DoesNotExist:
                    print('author does not exist')
                    update.message.reply_text(f"could not find author {context.args[1]}, quote not added")
        elif len(context.args) == 1:
            print('len args == 1')
            try:
                author = Author.objects.get(key=context.args[0])
                print(f'author={author}')
                quote_from_author(update, context, author)
            except Author.DoesNotExist:
                update.message.reply_text(f"could not find author {context.args[0]}")
        else:
            print('else')
            update.message.reply_text("could not parse args")
    else:
        random_quote(update, context)


def quote_maker(author, can_add=True):
    pass
    

BASE_HANDLERS = (
        (['quote'], quote_command),
        (['author'], author_command),
        )


class Bot:
    def __init__(self, token=None):
        self._token=token
        self._updater=Updater(self._token, use_context=True)
        self._configured = False
        self.config()

    def config(self, handlers=BASE_HANDLERS):
        for keys, method in handlers:
            self.add_handler(keys, method)
        self._configured = True
    
    def run(self):
        self._updater.start_polling()

    def add_handler(self, keys, method):
        handler = CommandHandler(keys, method)
        self._updater.dispatcher.add_handler(handler)

