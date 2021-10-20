from django.contrib import admin

# Register your models here.

from .models import Location, Travel

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Location._meta.fields] #全顯示
    list_per_page = 10 #列表一頁顯示幾項
    search_fields = ('city',) #搜尋設定 結尾要加逗號組成list/tuple
    list_filter = ('country',) #過濾器    
    ordering = ('pk',) #自定義排序
    # ordering = ('-pk',) #排序, 負號代表反向排列

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ['pk','target', 'companion', 'location', 'fk_city', 'date']
    list_editable = ('location',) #可在列表修改
    raw_id_fields = ('location',) #外鍵查看, 配合list_editable
    date_hierarchy = ('date') #根據日期格式分類, 耗時, 不用逗號
    
    # 顯示外鍵內容
    def fk_city(self, obj):
        return obj.location.city
    fk_city.admin_order_field  = 'location' #允許排列
    fk_city.short_description = 'City (fk)' #清單名稱