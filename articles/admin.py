from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Chapter, ArticleChapter


class ArticleChapterInlineFormset(BaseInlineFormSet):
    """Дополнительная проверка при сохранении объекта"""
    def clean(self):
        is_main = False
        for form in self.forms:

            if form.cleaned_data.get('is_main'):
                if not is_main:
                    is_main = True
                else:
                    raise ValidationError('Основная тема возможна только одна.')

            if not is_main:
                raise ValidationError('Укажите основной раздел')
        # Если тема не указана:
        if len(self.forms) == 0:
            raise ValidationError("Не указана тема")

        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleChapterInline(admin.TabularInline):
    model = ArticleChapter
    formset = ArticleChapterInlineFormset
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'id')
    # list_filter = ['published_at']
    inlines = [ArticleChapterInline, ]


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


