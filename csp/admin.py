from django.contrib import admin

from csp.models import Group, Report


class GroupAdmin(admin.ModelAdmin):
    fields = ('name', 'identifier',)
    list_display = ('name', 'identifier', 'count',)
    readonly_fields = ('identifier',)

    def has_add_permission(*a, **kw):
        return False


class ReportAdmin(admin.ModelAdmin):
    date_hierarchy = 'reported'
    list_display = ('__unicode__', 'document_uri', 'blocked_uri',
                    'violated_directive', 'referrer', 'reported')
    list_filter = ('document_uri', 'violated_directive', 'group')
    readonly_fields = ('group', 'document_uri', 'blocked_uri', 'referrer',
                       'violated_directive', 'original_policy', 'reported')

    def has_add_permission(*a, **kw):
        return False


admin.site.register(Group, GroupAdmin)
admin.site.register(Report, ReportAdmin)
