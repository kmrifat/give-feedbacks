from django.contrib import admin
from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return self.model.objects.all().order_by('-id')

    fields = ['is_anonymous', 'good', 'bad', 'need_improvement', 'created_for']
    list_display = ['is_anonymous', 'created_by', 'good', 'bad', 'need_improvement', 'created_for']


admin.site.register(Feedback, FeedbackAdmin)
