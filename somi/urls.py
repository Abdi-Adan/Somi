from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# local imports
from courses.views import CourseListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('courses/', include('courses.urls')),
    path('students/', include('students.urls')),

    # authentication urls
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]


if settings.DEBUG:
    import debug_toolbar
    # static media url
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # debug toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    