from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .form import *

# Create your views here.
def ContactList(request):
    contact = Contact.objects.all()
    context = {'contact': contact}
    return render(request, "TAM/home.html", context)

def ContactDetials(request,pk):
    contact = Contact.objects.get(id=pk)
    context = {'contact': contact}

    return render(request, 'TAM/contactDetails.html', context)

def createContact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'TAM/contact_form.html', context)

def updateContact(request, pk):
    contact = Contact.objects.get(id=pk)
    form = ContactForm(instance=contact)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'TAM/contact_form.html', context)

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)
    form = ContactForm(instance=contact)
    if request.method == "POST":
        contact.delete()
        return redirect('/')

    context = {'contact': contact}
    return render(request, 'TAM/deleteContact.html', context)


def createContactPhoneNumber(request):
    form = PhoneNumberForm()
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'TAM/contact_form.html', context)


def createContactName(request):
    form = NameForm()
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'TAM/contact_form.html', context)

