from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 

monthly_challenges = {
    "january" : "Eat only meat for the entire month !",
    "february" : "Run for at leat 20mn every day",
    "march" : "Learn Django for at least 20 minutes every day",
    "april" : "Learn russian for at leat 1 hour a day",
    "may": "Learn italian at leat 15mn every day",
    "june": "Do some sport every day",
    "july": "Swim at leat 5 hours every week",
    "august": "Practise CSS 30mn every day",
    "september": "Practise conversationnal russian 30mn every day",
    "october": "Do not eat sugar for an entire month",
    "november": "Finish your mega portfolio",
    "december": None
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months":months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month=months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge
    return HttpResponseRedirect(redirect_path)



def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })


    except:
        raise Http404()