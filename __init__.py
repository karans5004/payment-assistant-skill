from mycroft import MycroftSkill, intent_file_handler
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger

ccnum = ''
ccname = ''
ccvv = ''
ccexpmon = ''
pg = ''
bankcode = ''
ccexpyr = ''




class PaymentAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        my_setting = self.settings.get('payment_details')
        

          

    @intent_file_handler('assistant.payment.intent')
    def select_payment(self, message):
        ccnum = self.settings.get('ccnum')
        ccname = self.settings.get('ccname')
        ccvv = self.settings.get('ccvv')
        ccexpmon = self.settings.get('ccexpmon')
        pg = self.settings.get('pg')
        bankcode = self.settings.get('bankcode')
        ccexpyr = self.settings.get('ccexpyr')

        """self.speak_dialog(ccname)
        self.speak_dialog(pg)
        self.speak_dialog(bankcode)
        for d in ccnum:
            self.speak_dialog(d)
        
        #self.speak_dialog(ccnum)
        #self.speak_dialog(ccvv)
        for d in ccvv:
            self.speak_dialog(d)
        self.speak_dialog(ccexpyr)
        self.speak_dialog(ccexpmon)
        """
        self.speak_dialog('assistant.payment')


    @intent_handler(IntentBuilder("").require("bill"))
    def bill_selected(self, message):
        self.speak_dialog('bill.payment')

    @intent_handler(IntentBuilder("").require("personal"))
    def personal_selected(self, message):
        self.speak_dialog('personal.payment')


    @intent_handler(IntentBuilder("").require('electricity'))
    def what_bill(self, message):
        self.speak_dialog('electricity.payment')


        

def create_skill():
    return PaymentAssistant()

