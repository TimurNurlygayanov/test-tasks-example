# The example taken from
# https://book.pythontips.com/en/latest/decorators.html
# and fixed, because the original example doesn't work.


class logit(object):
    _logfile = 'out.log'

    def __init__(self, func, *args):
        self.func = func

    def __call__(self, *args, **kwargs):
        log_string = self.func.__name__ + " was called"
        print(log_string)

        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')

        # Now, send a notification
        self.notify()

        # return base func
        return self.func(*args, **kwargs)

    def notify(self):
        # logit only logs, no more
        pass


class email_logit(logit):
    """ A logit implementation for sending emails to admins
        when the function is called.
    """
    def __init__(self, *args, email='admin@myproject.com', **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        print('Sending email to {0}'.format(self.email))


@email_logit
def my_func(a=None):
    print(a)


# Run the code:
my_func(3)
