"""
Template tags for auto-translation of PL leftovers in templates.

Usage in templates:
    {% load auto_translate_tags %}
    {% auto_translate "Witaj świecie" %}
    {% auto_translate_block %}
        This is hardcoded PL text
    {% end_auto_translate_block %}
"""
from django import template
from django.utils.safestring import mark_safe

# Import the translate function lazily so module-level failures (e.g. on
# read-only filesystems like Vercel where the SQLite cache cannot be opened)
# don't crash template engine initialization.
# See MBTApp.auto_translate — it has an in-memory fallback for that case.
try:
    from MBTApp.auto_translate import translate as auto_translate_fn
except Exception:  # pragma: no cover - defensive
    auto_translate_fn = None

register = template.Library()


class AutoTranslateNode(template.Node):
    """Wraps content and translates PL→target on render."""

    def __init__(self, nodelist, target_var='LANGUAGE_CODE'):
        self.nodelist = nodelist
        self.target_var = target_var

    def render(self, context):
        if auto_translate_fn is None:  # defensive — module failed to import
            return self.nodelist.render(context)
        target = context.get(self.target_var, 'pl')
        if target == 'pl':
            # Already source language
            return self.nodelist.render(context)
        text = self.nodelist.render(context)
        if not text.strip():
            return text
        try:
            translated = auto_translate_fn(text, source='pl', target=target)
            return translated
        except Exception:
            return text


@register.tag(name='auto_translate_block')
def auto_translate_block(parser, token):
    """Block tag that translates enclosed PL text into the current language."""
    nodelist = parser.parse(('end_auto_translate_block',))
    parser.delete_first_token()
    return AutoTranslateNode(nodelist)


@register.simple_tag
def auto_translate(text, source='pl'):
    """Simple tag: translates `text` to current LANGUAGE_CODE."""
    from django.utils.translation import get_language
    target = get_language() or 'pl'
    if target == source or auto_translate_fn is None:
        return text
    return auto_translate_fn(text, source=source, target=target)


@register.filter
def pl_translate(text):
    """Filter: {{ "PL text"|pl_translate }} — uses current language as target."""
    from django.utils.translation import get_language
    target = get_language() or 'pl'
    if target == 'pl' or auto_translate_fn is None:
        return text
    return auto_translate_fn(text, source='pl', target=target)