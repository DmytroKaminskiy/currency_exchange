# class Email:
#     def __init__(self, email):
#         self._email = email
#
#     email = property()
#
#     @email.getter  # getter
#     def email(self):
#         return self._email
#
#     @email.setter  # setter
#     def email(self, value):
#         if '@' not in value:
#             raise ValueError('Wrong Email')
#         if '.' not in value:
#             raise ValueError('Wrong Email')
#         self._email = value
#
#     @email.deleter  # deleter
#     def email(self):
#         self._email = ''
#
# class Student(Email):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#
# s = Student('email.com')
# print(s.email)
#
# s.email = 'awdawdawdaw@mail.com'
# print(s.email)
#
# del s.email
# print(s.email, 'No email')

class Email:
    def __init__(self, email=None):
        self.email = email

    def __get__(self, obj, objtype):  # getter
        print('__get__', self.email)
        return self.email

    def __set__(self, instance, value):  # setter
        # raise AttributeError('Protected Method')
        print('__set__')
        if '@' not in value:
            raise ValueError('Wrong Email')
        if '.' not in value:
            raise ValueError('Wrong Email')
        self.email = value

    def __delete__(self, instance):  # deleter
        print('__delete__')
        self.email = ''


class Student:
    mail = Email()
    # phone = Phone()

    def __init__(self, email):
        self.mail = email

class Human:
    mail = Email()

    def __init__(self, email):
        self.mail = email


s = Student('email@mail.com')
print(s.mail)
s.mail = 'adawdawd@mail.com'
print(s.mail)
del s.mail

class Template:
    def __init__(self, template=None):
        self.template = template

    def __get__(self, obj, objtype):  # getter
        return get_template(self.template, self.request)


class View:
    template_name = Template('templ.html')

class View2:
    template_name = Template('templ2.html')

class View3:
    @property
    def template_name(self):
        return get_template('templ3.html', self.request)
