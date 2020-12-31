from allauth.account.adapter import DefaultAccountAdapter


class NoNewUserAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request): #بهذه الدالة تم غلق صفحة التسجيل الجديد حتى لا يتمكن أي شخص من القيام بتسجيل جديد
        return False