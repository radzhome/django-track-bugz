from django.shortcuts import render
from django.http import HttpResponse

from models import Ticket


def test_view(request):
    return HttpResponse("TODO, use admin interface.", content_type="text/plain")


def get_tickets(request):
    #TODO: need to be able to query
    return HttpResponse("TODO,", content_type="text/plain")

# TODO: create a view that lets you get request header
#request.META['HTTP_AUTHORIZATION']
#request.META.get('Authorization')

# TODO: CREATe api root
# @api_view(('GET',))
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format)
#     })

#
# class TicketViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list`, `create`, `retrieve`,
#     `update` and `destroy` actions.
#     Additionally we also provide an extra `highlight` action.
#     """
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
#
#     # TODO: Custom action routes
#     # @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
#     # def highlight(self, request, *args, **kwargs):
#     #     snippet = self.get_object()
#     #     return Response(snippet.highlighted)
#     #
#     # def perform_create(self, serializer):
#     #         serializer.save(owner=self.request.user)