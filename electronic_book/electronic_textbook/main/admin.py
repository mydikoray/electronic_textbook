from django.contrib import admin

from .models import (
    Lecture,
    Laboratory,
    Presentation,
    Material,
    TestQuestion,
    GoogleTestForm,
    Test,
    Question
)


admin.site.register(Lecture)
admin.site.register(Laboratory)
admin.site.register(Presentation)
admin.site.register(Material)


admin.site.register(Test)
admin.site.register(Question)