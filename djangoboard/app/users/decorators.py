from django.shortcuts import redirect
from django.urls import reverse_lazy


def login_required(view_func, login_url=reverse_lazy('testusers:login')):
    def wrap(request, *args, **kwargs):
        if 'user' in request.session:
            return view_func(request, *args, **kwargs)
        return redirect(login_url)

    return wrap
