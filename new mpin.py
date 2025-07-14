from datetime import datetime
COMMONLY_USED_4_DIGIT = {
    "1234", "0000", "1111", "1212", "7777", "1004", "2000", "4444", "2222", "6969", "9999", "3333", "5555", "6666", "1122"
}
COMMONLY_USED_6_DIGIT = {
    "123456", "000000", "111111", "121212", "777777", "100400", "200000", "444444", "222222", "696969", "999999", "333333", "555555", "666666", "112233"
}

class MPIN:
    def __init__(self):
        global mpin
        mpin = input("Enter your 4 or 6 digit mpin : ")
        is_4_digit = len(mpin) == 4
        is_6_digit = len(mpin) == 6
        if(is_4_digit and mpin in COMMONLY_USED_4_DIGIT) or (is_6_digit and mpin in COMMONLY_USED_6_DIGIT):
            print("COMMONLY USED")
        else:
            dob_self = input("Enter your DOB (DD-MM-YY) : ")
            dob_spouse = input("Enter your spouse DOB (DD-MM-YY) : ")
            anniversary = input("Enter your anniversary date (DD-MM-YY) : ")
            result = self.check_mpin_strength(mpin, dob_self, dob_spouse, anniversary)

    def extract_date_patterns(self,date):
        date = datetime.strptime(date,"%d-%m-%Y")
        patterns = set()
        day = f"{date.day:02}"
        month = f"{date.month:02}"
        year_full = str(date.year)
        year_short = year_full[-2:]

        patterns.update({
            day + month,
            month + day,
            year_short + month,
            month + year_short,
            day + year_short,
            year_short + day
        })

        patterns.update({
            year_short + month + day,
            day + year_short + month,
            day + month + year_short,
            month + day + year_short,
            year_short + day + month,
            month + year_short + day
        })
        print(patterns)
        # return patterns


    def check_mpin_strength(self,mpin, dob_self="", dob_spouse="", anniversary=""):
        reason = []
        is_4_digit = len(mpin) == 4
        is_6_digit = len(mpin) == 6

        checks = [
            ("DEMOGRAPHIC_DOB_SELF",dob_self),
            ("DEMOGRAPHIC_DOB_SPOUSE",dob_spouse),
            ("DEMOGRAPHIC_ANNIVERSARY",anniversary)
        ]

        for label,date in checks:
            if mpin in self.extract_date_patterns(date):
                reason.append(label)

        strengths = "WEAK" if reason else "STRONG"

        print("\nMPIN analysis result")
        print(f"mpin : {mpin}")
        print(f"reason : {reason}")
        print(f"strength : {strengths}")
        if strengths == "WEAK":
            print("Reason for weakness : ",reason)
        else:
            print("Your MPIN is strong. No weakness found")

sundar = MPIN()