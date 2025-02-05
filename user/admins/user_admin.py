from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ["full_name", "username", "email","user_gender"]
    list_filter =['user_gender']
    search_fields=['full_name','username','email']
    sortable_by=['full_name','email']
    
    
    
