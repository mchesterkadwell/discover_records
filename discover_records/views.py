from io import StringIO

from django.contrib import messages
from django.core.management import call_command
from django.core.management.base import CommandError
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .forms import RecordForm
from .models import Record


def record(request):
    """View function for retrieving a specified record from TNA Discovery API and inserting it into the database."""

    # If POST submit the data
    if request.method == "POST":
        form = RecordForm(request.POST)

        if form.is_valid():
            record_id = form.cleaned_data["record_id"]

            try:
                out = StringIO()
                call_command("importrecord", record_id, stdout=out)
                messages.success(request, out.getvalue())

            except CommandError as err:
                messages.error(request, str(err))
                return render(request, "pages/record.html", {"form": form})

            return HttpResponseRedirect("view/%s" % record_id)

    # If GET or any other method display empty form
    else:
        form = RecordForm()

    return render(request, "pages/record.html", {"form": form})


def record_view(request, record_id):
    """View function for retrieving a record by id from the database."""
    try:
        record_obj = Record.objects.get(pk=record_id)
    except Record.DoesNotExist:
        raise Http404("Record does not exist")
    return render(request, "pages/record_view.html", {"record": record_obj})
