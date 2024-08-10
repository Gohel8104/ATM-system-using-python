class ATM1:
    def __init__(self):
        print("English language is selected.")
        self.balance = 1000  # Initial balance 

    def display_menu(self):
        print("Welcome to the ATM!")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Change PIN")
        print("6. Exit")

    def select_menu_option(self):
        option = input("Enter your choice: ")
        if option == "1":
            self.balance_inquiry()
        elif option == "2":
            self.cash_withdrawal()
        elif option == "3":
            self.deposit()
        elif option == "4":
            self.transfer()
        elif option == "5":
            self.change_pin()
        elif option == "6":
            print("Thank you for using the ATM. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please select a valid option.")
            self.select_menu_option()

    def balance_inquiry(self):
        print("Balance Inquiry selected.")
        print("Your current balance is:", self.balance)

    def cash_withdrawal(self):
        print("Cash Withdrawal selected.")
        amount = float(input("Enter the amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful. Remaining balance:", self.balance)

    def deposit(self):
        print("Deposit selected.")
        amount = float(input("Enter the amount to deposit: "))
        self.balance += amount
        print("Deposit successful. Updated balance:", self.balance)

    def transfer(self):
        print("Transfer selected.")
        amount = float(input("Enter the amount to transfer: "))
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            recipient_account = input("Enter the recipient's account number: ")
            confirmation = input(f"Confirm transfer of {amount} to account {recipient_account}? (yes/no): ")
            if confirmation.lower() == "yes":
                self.balance -= amount
                print("Transfer successful. Remaining balance:", self.balance)
            else:
                print("Transfer cancelled.")

    def change_pin(self):
        print("Change PIN selected.")
        old_pin = input("Enter your old PIN: ")
        new_pin = input("Enter your new PIN: ")
        confirm_new_pin = input("Confirm your new PIN: ")
        if new_pin == confirm_new_pin:
            print("PIN changed successfully.")
        else:
            print("New PINs do not match. Please try again.")

    def start(self):
        while True:
            self.display_menu()
            self.select_menu_option()

# ---------------------------------------------------------------------------------------------------------------------
#hindi
class ATM2:
    def __init__(self):
        print("हिंदी भाषा चुनी गई है।")
        self.balance = 1000  # Initial balance 
        
    def display_menu(self):
        print("ATM में आपका स्वागत है!")
        print("1. शेष पूछताछ")
        print("2. नकद निकालना")
        print("3. जमा")
        print("4. हस्तांतरण")
        print("5. पिन बदलें")
        print("6. बाहर निकलें")

    def select_menu_option(self):
        option = input("अपना विकल्प दर्ज करें: ")
        if option == "1":
            self.balance_inquiry()
        elif option == "2":
            self.cash_withdrawal()
        elif option == "3":
            self.deposit()
        elif option == "4":
            self.transfer()
        elif option == "5":
            self.change_pin()
        elif option == "6":
            print("ATM का उपयोग करने के लिए धन्यवाद। अलविदा!")
            exit()
        else:
            print("अमान्य विकल्प. कृपया एक मान्य विकल्प चुनें।")
            self.select_menu_option()

    def balance_inquiry(self):
        print("शेष पूछताछ चयन किया गया है।")
        print("आपका वर्तमान शेष है:", self.balance)

    def cash_withdrawal(self):
        print("नकद निकालने का चयन किया गया है।")
        amount = float(input("निकालने के लिए राशि दर्ज करें: "))
        if amount > self.balance:
            print("पर्याप्त शेष नहीं है।")
        else:
            self.balance -= amount
            print("निकास सफल। शेष राशि:", self.balance)

    def deposit(self):
        print("जमा का चयन किया गया है।")
        amount = float(input("जमा करने के लिए राशि दर्ज करें: "))
        self.balance += amount
        print("जमा सफल। अद्यतित शेष:", self.balance)

    def transfer(self):
        print("हस्तांतरण चयन किया गया है।")
        amount = float(input("हस्तांतरण के लिए राशि दर्ज करें: "))
        if amount > self.balance:
            print("पर्याप्त शेष नहीं है।")
        else:
            recipient_account = input("प्राप्तकर्ता का खाता नंबर दर्ज करें: ")
            confirmation = input(f"{amount} के हस्तांतरण की पुष्टि करें? (1.(हाँ)/2.(नहीं)): ")
            if confirmation.lower() == "1":
                self.balance -= amount
                print("हस्तांतरण सफल। शेष राशि:", self.balance)
            else:
                print("हस्तांतरण रद्द।")

    def change_pin(self):
        print("पिन बदलने का चयन किया गया है।")
        old_pin = input("अपना पुराना पिन दर्ज करें: ")
        new_pin = input("अपना नया पिन दर्ज करें: ")
        confirm_new_pin = input("अपना नया पिन पुष्टि करें: ")
        if new_pin == confirm_new_pin:
            print("पिन सफलतापूर्वक बदल गया।")
        else:
            print("नए पिन मेल नहीं खाते। कृपया पुनः प्रयास करें।")

    def start(self):
        while True:
            self.display_menu()
            self.select_menu_option()

#------------------------------------------------------------------------------------------------------------------
#gujarati
class ATM3:
    def __init__(self):
        print("ગુજરાતી ભાષા પસંદ કરી છે।")
        self.balance = 1000  # Initial balance 

    def display_menu(self):
        print("એટીએમમાં આપનું સ્વાગત છે!")
        print("1. શેષ પૂછતાછ")
        print("2. નગદ નીકાસ")
        print("3. જમા")
        print("4. ટ્રાન્સફર")
        print("5. પીન બદલો")
        print("6. બહાર નીકળો")

    def select_menu_option(self):
        option = input("તમારો વિકલ્પ દાખલ કરો: ")
        if option == "1":
            self.balance_inquiry()
        elif option == "2":
            self.cash_withdrawal()
        elif option == "3":
            self.deposit()
        elif option == "4":
            self.transfer()
        elif option == "5":
            self.change_pin()
        elif option == "6":
            print("એટીએમનો ઉપયોગ કરવા બદલ આભાર. અલવિદા!")
            exit()
        else:
            print("અમાન્ય પસંદ. કૃપા કરીને માન્ય વિકલ્પ પસંદ કરો.")
            self.select_menu_option()

    def balance_inquiry(self):
        print("શેષ પૂછતાછ પસંદ કરેલું છે.")
        print("તમારું વર્તમાન શેષ છે:", self.balance)

    def cash_withdrawal(self):
        print("નગદ નીકાસ પસંદ કરેલું છે.")
        amount = float(input("નીકાસ કરવા માટે રકમ દાખલ કરો: "))
        if amount > self.balance:
            print("પર્યાપ્ત શેષ નથી.")
        else:
            self.balance -= amount
            print("નગદ નિકાસ સફળ. શેષ રકમ:", self.balance)

    def deposit(self):
        print("જમા પસંદ કરેલું છે.")
        amount = float(input("જમા કરવા માટે રકમ દાખલ કરો: "))
        self.balance += amount
        print("જમા સફળ. નવી શેષ:", self.balance)


    def transfer(self):
        print("ટ્રાન્સફર પસંદ કરેલું છે.")
        amount = float(input("ટ્રાન્સફર કરવા માટે રકમ દાખલ કરો: "))
        if amount > self.balance:
            print("પર્યાપ્ત શેષ નથી.")
        else:
            recipient_account = input("પ્રાપ્તકર્તાનું ખાતા નંબર દાખલ કરો: ")
            confirmation = input(f"{amount} નું ટ્રાન્સફર કરવાની પુષ્ટિ કરો? (1.(હા)/2.(ના)): ")
            if confirmation.lower() == "1":
                self.balance -= amount
                print("ટ્રાન્સફર સફળ. શેષ રકમ:", self.balance)
            else:
                print("ટ્રાન્સફર રદ થઈ છે.")

    def change_pin(self):
        print("પીન બદલવું પસંદ કરેલું છે.")
        old_pin = input("તમારો જૂનો પીન દાખલ કરો: ")
        new_pin = input("તમારો નવો પીન દાખલ કરો: ")
        confirm_new_pin = input("તમારો નવો પીન પુષ્ટિ કરો: ")
        if new_pin == confirm_new_pin:
            print("પીન સફળતાપૂર્વક બદલાઈ ગઈ છે.")
        else:
            print("નવા પીન મેળ નહીં ખાતું. કૃપા કરીને પુનઃ પ્રયાસ કરો.")

    def start(self):
        while True:
            self.display_menu()
            self.select_menu_option()
# -------------------------------------------------------------------------------------------------------------------


# Entry point of the program
print("Welcome to the ATM!")
print("""Please select your language:|
        कृपया अपनी भाषा का चयन करें:|
        તમારી પસંદગી ભાષા માટે સંખ્યા દાખલ કરો: """)
print("1. English")
print("2. हिंदी")
print("3. ગુજરાતી")

language_choice = input("""Enter the number corresponding to your preferred language: |
                            अपनी पसंदीदा भाषा के लिए संख्या दर्ज करें:|
                            તમારી પસંદગી ભાષા માટે સંખ્યા દાખલ કરો:  """)

if language_choice == "1":
    # "English"
    atm=ATM1()
    atm.start()
elif language_choice == "2":
    # "hindi"
    atm=ATM2()
    atm.start()
elif language_choice == "3":
    # "gujarati"
    atm=ATM3()
    atm.start()
else:
    print("""Invalid choice. Please select a valid option.
            अमान्य विकल्प. कृपया एक मान्य विकल्प चुनें।
            અમાન્ય પસંદ. કૃપા કરીને માન્ય વિકલ્પ પસંદ કરો.""")
