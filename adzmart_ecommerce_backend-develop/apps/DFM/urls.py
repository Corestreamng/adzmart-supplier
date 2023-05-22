from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.DFM import views

urlpatterns = [
    path('dfm-brief/', views.MediaBriefRequests.as_view(), name='media-brief-listings'),
    path('dfm-advisory/', views.MediaAdvisoryRequests.as_view(), name='media-advisory-listings'),
    path('dfm-support/', views.MediaSupportRequests.as_view(), name='support-listings'),
    path('dfm-brief/<int:pk>', views.MediaBriefRequests.as_view(), name='media-brief-details'),
    path('dfm-advisory/<int:pk>', views.MediaAdvisoryRequests.as_view(), name='media-advisory-details'),
    path('dfm-support/<int:pk>', views.MediaSupportRequests.as_view(), name='support-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
