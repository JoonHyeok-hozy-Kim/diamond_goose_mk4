from django.http import HttpResponseForbidden

from equityownedapp.models import EquityOwned


def equity_owned_ownership_required(func):
    def decorated(request, *args, **kwargs):
        equity_owned = EquityOwned.objects.get(pk=kwargs['pk'])
        if request.user != equity_owned.owner:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated