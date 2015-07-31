from oliver.models import Account

__author__ = 'oliver'



class RestAuthBackend:

    def authenticate(self, accountid=None, password=None):
        try:
            user = Account.objects.get(accountid=accountid)
        except Account.DoesNotExist:
            pass
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None