"""Se te propone crear un módulo capaz de evaluar usuarios y contraseñas.
Para ello el módulo tendrá dos funciones, una para validar usuarios y otra para validar contraseñas.
(Pista: necesitarás utilizar la función «isalnum()» entre otras para realizar este ejercicio.
Esta función evalúa si una cadena de texto es alfanumérica devolviendo True en caso de serlo o False en caso contrario).

La función de validación de usuarios debe cumplir las siguientes restricciones:

No debe tener menos de 5 caracteres ni más de 15. Si se incumple esta restricción, la función devolverá el mensaje “El usuario no puede tener menos de 5 caracteres” o “El usuario no puede tener más de 15 caracteres”.
Solo puede contener letras y números. Si se incumple esta restricción la función devolverá el mensaje “El usuario solo puede contener letras y números”
Si el usuario es correcto, la función devolverá True.
La función de validación de contraseñas debe cumplir las siguientes restricciones:

Debe tener más de 10 caracteres. Si se incumple esta restricción, la función devolverá el mensaje “La contraseña debe tener más de 10 caracteres”
Debe contener al menos un carácter que no sea ni letra ni número. Si se incumple esta restricción, la función devolverá el mensaje “La contraseña debe contener un carácter que no sea ni letra ni número”
Debe contener al menos una letra mayúscula y una letra minúscula. Si se incumple esta restricción, la función devolverá el mensaje “La contraseña no es segura”
No puede tener espacios en blanco. Si se incumple esta restricción, la función devolverá el mensaje “La contraseña no puede contener espacios en blanco”
Si el usuario es correcto, la función devolverá True."""

from ejercicio_validacion import validarUsuario
from ejercicio_validacion import validarPassword

#validarUsuario()
#validarPassword()

#Solución:

def evalua_usuario(usuario):
    if usuario.isalnum():
        if len(usuario)<5:
            return "El usuario no puede contener menos de 5 caracteres."
        elif len(usuario)>15:
            return "El usuario no puede tener más de 15 caracteres."
        else:
            return True
    return "El usuario sólo puede contener letras y números."

def evalua_password(password):
    mayuscula=False
    minuscula=False

    if len(password)<10:
        return "La contraseña no puede tener menos de 10 caracteres."
    elif password.isalnum():
        return "La contraseña debe tener un caracter que no sea ni letra ni numero."
    else:
        for i in password:
            if i.isupper():
                mayuscula = True
            elif i.islower():
                minuscula = True
            elif i==" ":
                return "La contraseña no puede tener espacios en blanco."
        if mayuscula and minuscula:
            return True
        else:
            return "La contraseña no es segura."

print(evalua_usuario("frb1987"))
print(evalua_password("probandoContraseña1."))