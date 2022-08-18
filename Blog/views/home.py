from django.http import HttpResponse


def homePageView(req):
  return HttpResponse(content='Hello World!')