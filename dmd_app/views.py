# Create your views here.
import markdown
from django.shortcuts import render

from .models import MarkdownContent

# noinspection PyUnresolvedReferences
def markdown_content_view(request):
    markdown_content = MarkdownContent.objects.first()
    context = {"markdown_content": markdown_content}
    return render(
        request,
        "dmd_app/markdown_content.html",
        context=context
    )