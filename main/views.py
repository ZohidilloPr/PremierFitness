from django.utils import timezone
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .models import Treiner, Weeks, Contact as CT, Member
from django.shortcuts import render, redirect

# Create your views here.

def handler404(request, *args, **argv):
    return render(request, "pages/404.html", status=404)

def handler500(request, *args, **argv):
    return render(request, 'pages/500.html', status=500)


def Home(request):
    """ ASOSIY PAGE UCHUN FUNCTION """
    if request.method == "POST":
        f_name = request.POST.get("m_f_name")
        phone = request.POST.get("m_phone")
        message = request.POST.get("m_message")
        try:
            member = Member.objects.create(
                f_name=f_name,
                phone=phone,
                text=message,
            )
            member.save() 
            messages.success(request, _("Biz bilan bog'lanish istagida bolganingiz uchun minnadormiz. Siz bilan mutaxasislarimiz aloqaga chiqadi."))
        except Exception:
            messages.error(request, _("Afsuski sizning murojatingiz yuborilmadi, iltimos qaytadan urinib ko'ring."))
        return redirect("/")
    
    weeks = Weeks.objects.all()
    trainer = Treiner.objects.all().order_by("order_num")
    context = {
        "weeks": weeks,
        "trainers" : trainer,
        "f_name": _("F.I.SH"),
        "message": _("Xabar"),
        "phone": _("Telefon raqam"),
        "year": timezone.now().year,
        "send_m": _("Savolni yuborish"),
        "we_address":_("Bizning manzil"),
        "questionYN": _("Savollaringiz bormi"),
        "address":_("Toshkent shahri Bektemir tumani 191-uy 2-3 qavat"),
    }
    return render(request, "index.html", context)


def Contact(request):
    if request.method == "POST":
        f_name = request.POST.get("f_name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        try:
            contact = CT.objects.create(
                f_name=f_name,
                phone=phone,
                text=message,
            )
            contact.save() 
            messages.success(request, _("Biz bilan bog'lanish istagida bolganingiz uchun minnadormiz. Siz bilan mutaxasislarimiz aloqaga chiqadi."))
        except Exception:
            messages.error(request, _("Afsuski sizning murojatingiz yuborilmadi, iltimos qaytadan urinib ko'ring"))
        return redirect("/")
    
    return render(request, "contact.htm")
