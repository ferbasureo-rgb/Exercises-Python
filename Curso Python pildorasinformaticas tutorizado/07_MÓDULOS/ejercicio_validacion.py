def validarUsuario(username):
    validacion = False
    if len(username) < 5:
        return "El usuario no puede tener menos de 5 caracteres."
    elif len(username) > 15:
        return "El usuario no puede tener más de 15 caracteres."
    elif not username.isalnum():
        return "El usuario sólo puede contener letras o números."
    else:
        validacion = True
    return validacion

def validarPassword(password):
    validacion = False
    if len(password) < 10:
        return "La contraseña debe tener más de 10 caracteres."
    elif password.isalnum():
        return "La contraseña debe contener un carácter que no sea ni letra ni número."
    elif password.islower() or password.isupper():
        return "La contraseña no es segura."
    elif " " in password:
        return "La contraseña no puede tener espacios en blanco."
    else:
        validacion = True
    return validacion

print(validarUsuario("frb1987"))
print(validarPassword("ASDFASDFASDFa."))