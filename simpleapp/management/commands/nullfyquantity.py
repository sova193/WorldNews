from django.core.management.base import BaseCommand, CommandError
from simpleapp.models import NewsPortal, NewsCategory

class Command(BaseCommand):
    help = 'Обнуляет все новости или статьи'
    requires_migrations_checks = True  # Напоминать ли о миграциях. Если true — то будет напоминание о том, что не
    # сделаны все миграции (если такие есть)

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('argument', nargs='+', type=int)

    def handle(self, *args, **options):
        # здесь можете писать любой код, который выполнится при вызове вашей команды
        self.stdout.readable()
        self.stdout.write('Вы действительно хотите удалить новости или статьи? если Новости то 1,'
                          'если Статьи то 2')  # спрашиваем пользователя,
        # действительно ли он хочет удалить все товары
        answer = input()  # считываем подтверждение

        if answer not in ('1', '2'):
            self.stdout.write(self.style.ERROR('Отменено'))

        elif answer == '1':  # в случае подтверждения действительно удаляем все товары
            category = NewsCategory.objects.get(name='Новости')
            NewsPortal.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted all news from category {category.name}'))
            return

        elif answer == '2':  # в случае подтверждения действительно удаляем все товары
            category = NewsCategory.objects.get(name='Статьи')
            NewsPortal.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted all news from category {category.name}'))
            return

        self.stdout.write(
            self.style.ERROR('Access denied'))  # в случае неправильного подтверждения, говорим, что в доступе отказано
