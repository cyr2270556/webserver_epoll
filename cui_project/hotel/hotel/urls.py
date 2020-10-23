from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),

    #分页模板
    # path('pagetest',views.paging,name='test'),

    #文件下载模板
    # path('downloadtest',views.download),

    path('uploadtest/',include('upload_test.urls')),

    #子应用模板
    path('sonapp/',include('sonapp.urls')),

]
#用户可以根据地址栏输入访问上传的文件
urlpatterns += static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)
print(settings.MEDIA_URL)
print(settings.MEDIA_ROOT)