from django.contrib.auth.tokens import PasswordResetTokenGenerator


class AccountVerifyTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (str(user.is_active) + str(user.pk) + str(timestamp))
class SetUpTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (str(user.pk) + str(timestamp))


generate_account_activation_token = AccountVerifyTokenGenerator()
generate_account_setup_token = SetUpTokenGenerator()
