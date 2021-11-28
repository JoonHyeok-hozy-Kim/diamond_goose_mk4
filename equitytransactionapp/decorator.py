from django.http import HttpResponseForbidden

from equitytransactionapp.models import EquityTransaction


def equity_transaction_ownership_required(func):
    def decorated(request, *args, **kwargs):
        equity_transaction = EquityTransaction.objects.get(pk=kwargs['pk'])
        if request.user != equity_transaction.owner:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated