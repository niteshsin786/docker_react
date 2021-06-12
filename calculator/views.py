from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "input.html")

bank_balance = [0]

def addition(request):

    num1 = request.POST['num1']
    num2 = (bank_balance[len(bank_balance) -1 ])
    
    if num1.isdigit():
        b = int(num1) + int(num2)
        bank_balance.append(b)

        return render(request, "input.html", {"result": bank_balance[len(bank_balance) -1]})
    else:
        res = "Only digits are allowed"
        return render(request, "result.html", {"result": res})


def subtraction(request):

    num1 = request.POST['num1']
    num2 = (bank_balance[len(bank_balance) -1 ])

    if num1.isdigit():
        b = int(num2) - int(num1)
        bank_balance.append(b)

        return render(request, "input.html", {"result": bank_balance[len(bank_balance) -1]})
    else:
        res = "Only digits are allowed"
        return render(request, "result.html", {"result": res})
