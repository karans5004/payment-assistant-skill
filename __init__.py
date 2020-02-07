from mycroft import MycroftSkill, intent_file_handler


class PaymentAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.payment.intent')
    def handle_assistant_payment(self, message):
        self.speak_dialog('assistant.payment')


def create_skill():
    return PaymentAssistant()

