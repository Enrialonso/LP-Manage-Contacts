#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render

from apps.app_gestor_usuarios.models import db_usuarios, \
    db_manage_contacts
from apps.app_gestor_usuarios.forms import signupForm, loginForm, \
    addForm


def index(request):
    return render(request, 'index.html', {'session': request.session})


def signup(request):

    db = db_manage_contacts.objects

    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():

            form.save()  # store the user in the db_usuarios

            data = form.cleaned_data  # extract the data for the form and make a dictionary
            request.session['usuario'] = data['email']

            query = db.filter(associated_user=request.session['usuario'
                              ]).order_by('name').values()
            query = list(query)
            message = 'Upsss! Contacts list empty!'
            return render(request, 'menu.html',
                          {'session': request.session,
                          'contacts': query, 'message': message})
    else:
        if 'usuario' in request.session:
            return render(request, 'menu.html',
                          {'session': request.session})
        else:
            form = signupForm()
            return render(request, 'signup.html', {'form': form},
                          {'session': request.session})


def login(request):
    if request.method == 'POST':

        db = db_usuarios.objects

        query = db.filter(email=request.POST['email']).values()
        query = list(query)

        if query[0]['email'] == request.POST['email'] \
            and query[0]['password'] == request.POST['password']:

            form = addForm()
            request.session['usuario'] = request.POST['email']
            db = db_manage_contacts.objects
            query = db.filter(associated_user=request.session['usuario'
                              ]).order_by('name').values()
            query = list(query)
            return render(request, 'menu.html',
                          {'session': request.session,
                          'contacts': query})
        else:

            form = loginForm()
            return render(request, 'login.html', {'form': form,
                          'session': request.session})
    else:

          # if the method request GET or others

        if 'usuario' in request.session:
            return render(request, 'menu.html',
                          {'session': request.session})
        else:
            form = loginForm()
            return render(request, 'login.html', {'form': form,
                          'session': request.session})


def logout(request):
    if 'usuario' in request.session:
        form = loginForm()
        del request.session['usuario']
        return render(request, 'login.html',
                      {'session': request.session, 'form': form})
    else:
        return render(request, 'index.html',
                      {'session': request.session})


def menu(request):

    db = db_manage_contacts.objects

    if 'usuario' in request.session:

        if request.method == 'POST':

            if 'name' in request.POST:
                query = \
                    db.filter(associated_user=request.session['usuario'
                              ]).filter(name=request.POST['name'
                        ]).values()
            elif 'email' in request.POST:
                query = \
                    db.filter(associated_user=request.session['usuario'
                              ]).filter(email=request.POST['email'
                        ]).values()
            elif 'postalcode' in request.POST:
                query = \
                    db.filter(associated_user=request.session['usuario'
                              ]).filter(postalcode=request.POST['postalcode'
                        ]).values()
            elif 'state' in request.POST:
                query = \
                    db.filter(associated_user=request.session['usuario'
                              ]).filter(state=request.POST['state'
                        ]).values()
            elif 'country' in request.POST:
                query = \
                    db.filter(associated_user=request.session['usuario'
                              ]).filter(country=request.POST['country'
                        ]).values()

            query = list(query)

            if len(query) == 0:
                message = '0 results in this search!!!'
                return render(request, 'menu.html',
                              {'session': request.session,
                              'contacts': '', 'message': message})
            else:
                return render(request, 'menu.html',
                              {'session': request.session,
                              'contacts': query, 'message': ''})
        else:

            query = db.filter(associated_user=request.session['usuario'
                              ]).order_by('name').values()
            query = list(query)
            message = 'Upsss! Contacts list empty!'
            return render(request, 'menu.html',
                          {'session': request.session,
                          'contacts': query, 'message': message})
    else:

        return render(request, 'index.html')


def addcontact(request):

    db = db_manage_contacts.objects

    if 'usuario' in request.session:

        if request.method == 'POST':

            form = addForm(request.POST)

            query = db.filter(email=request.POST['email']).values()
            query = list(query)

            if len(query) > 0:
                formulario = addForm(initial={
                    'associated_user': request.session['usuario'],
                    'name': request.POST['name'],
                    'last': request.POST['last'],
                    'email': request.POST['email'],
                    'phone_local': request.POST['phone_local'],
                    'phone_mov': request.POST['phone_mov'],
                    'street': request.POST['street'],
                    'street_number': request.POST['street_number'],
                    'population': request.POST['population'],
                    'state': request.POST['state'],
                    'country': request.POST['country'],
                    'postalcode': request.POST['postalcode'],
                    'url_web': request.POST['url_web'],
                    })

                message = \
                    'Contact not added, The email of this contact is already exist!'
                return render(request, 'addcontact.html',
                              {'session': request.session,
                              'form': formulario, 'message': message})

            if form.is_valid():
                form.save()  # store the user in the db_usuarios

                query = \
                    db.filter(associated_user=request.session['usuario'
                              ]).order_by('name').values()
                query = list(query)
                message = 'Upsss! Contacts list empty!'
                return render(request, 'menu.html',
                              {'session': request.session,
                              'contacts': query, 'message': message})
        else:

            form = \
                addForm(initial={'associated_user': request.session['usuario'
                        ]})
            return render(request, 'addcontact.html',
                          {'session': request.session, 'form': form})
    else:

        return render(request, 'index.html',
                      {'session': request.session})


def editcontact(request):

    db = db_manage_contacts.objects

    if 'usuario' in request.session:

        if request.method == 'POST':

            formulario = addForm(initial={
                'associated_user': request.session['usuario'],
                'name': request.POST['name'],
                'last': request.POST['last'],
                'email': request.POST['email'],
                'phone_local': request.POST['phone_local'],
                'phone_mov': request.POST['phone_mov'],
                'street': request.POST['street'],
                'street_number': request.POST['street_number'],
                'population': request.POST['population'],
                'state': request.POST['state'],
                'country': request.POST['country'],
                'postalcode': request.POST['postalcode'],
                'url_web': request.POST['url_web'],
                })

            return render(request, 'editcontact.html', {
                'session': request.session,
                'form': formulario,
                'message': '',
                'id': request.POST['id'],
                })
        else:

            return render(request, 'menu.html',
                          {'session': request.session})
    else:

        return render(request, 'index.html',
                      {'session': request.session})


def deletecontact(request):

    if 'usuario' in request.session:
        if request.method == 'POST':

            db = db_manage_contacts.objects

            db.filter(id=request.POST['id']).delete()

            query = db.filter(associated_user=request.session['usuario'
                              ]).order_by('name').values()
            query = list(query)
            message = 'Your Contact ' + request.POST['name'] + ' ' \
                + request.POST['last'] + ' is already deleted!!!'
            return render(request, 'menu.html',
                          {'session': request.session,
                          'contacts': query, 'messagedit': message})
        else:

            return render(request, 'menu.html',
                          {'session': request.session})
    else:

        return render(request, 'index.html',
                      {'session': request.session})


def editdone(request):

    if 'usuario' in request.session:
        if request.method == 'POST':

            db = db_manage_contacts.objects

            db.filter(id=request.POST['id']).update(
                name=request.POST['name'],
                last=request.POST['last'],
                email=request.POST['email'],
                phone_local=request.POST['phone_local'],
                phone_mov=request.POST['phone_mov'],
                street=request.POST['street'],
                street_number=request.POST['street_number'],
                population=request.POST['population'],
                state=request.POST['state'],
                country=request.POST['country'],
                postalcode=request.POST['postalcode'],
                url_web=request.POST['url_web'],
                )

            query = db.filter(associated_user=request.session['usuario'
                              ]).order_by('name').values()
            query = list(query)
            message = 'Your Contact ' + request.POST['name'] + ' ' \
                + request.POST['last'] + ' is already updated!!!'
            return render(request, 'menu.html',
                          {'session': request.session,
                          'contacts': query, 'messagedit': message})
        else:

            return render(request, 'menu.html',
                          {'session': request.session})
    else:

        return render(request, 'index.html',
                      {'session': request.session})
