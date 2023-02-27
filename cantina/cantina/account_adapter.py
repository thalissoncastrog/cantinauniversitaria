from allauth.account.adapter import DefaultAccountAdapter

#Somente administração cadastra novos funcionários
class NoNewUsersAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self,request):
        return False