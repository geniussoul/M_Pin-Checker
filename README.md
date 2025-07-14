🔐 M_PIN-Checker — Mobile PIN Strength Analyzer
==============================================

A Python-based CLI tool that checks whether your 4- or 6-digit M-PIN is commonly used or dangerously predictable
(such as your date of birth, your spouse's DOB, or your anniversary date).

--------------------------
💡 Purpose
--------------------------
Ever wondered if your mobile unlock PIN is too obvious?

This tool checks:
✔️ Whether it's on a list of commonly used weak PINs  
✔️ Whether it matches parts of known personal dates (like birthdays)  
✔️ Whether it follows patterns derived from those dates (DDMM, MMYY, etc.)

Your M-PIN should be more than just "1234" or "0711" (hello birthdays 😅) — this tool will tell you just how strong it really is.

--------------------------
🚀 Features
--------------------------
✅ Detects commonly used 4-digit and 6-digit PINs  
✅ Compares PIN against DOBs and anniversaries  
✅ Identifies specific demographic weakness causes  
✅ Provides readable and structured strength analysis  
✅ Built using Python's `datetime` module and sets for efficiency

--------------------------
📦 Requirements
--------------------------
- Python 3.x

No third-party packages required — pure Python power 💪

--------------------------
🛠️ How to Use
--------------------------
1. Run the script:
    python mpin.py

2. Input:
   - A 4-digit or 6-digit M-PIN when prompted
   - Your date of birth (DD-MM-YYYY)
   - Spouse's date of birth (DD-MM-YYYY)
   - Anniversary (DD-MM-YYYY)

3. Output:
   - Tells you if your M-PIN is "COMMONLY USED"
   - Or whether it is "WEAK" or "STRONG" based on matches with your personal dates

--------------------------
📊 Example Output
--------------------------
Enter your 4 or 6 digit mpin : 0711

Enter your DOB (DD-MM-YYYY) : 07-11-2000

Enter your spouse DOB (DD-MM-YYYY) : 09-03-2001

Enter your anniversary date (DD-MM-YYYY) : 12-12-2022

MPIN analysis result

mpin : 0711

reason : ['DEMOGRAPHIC_DOB_SELF']

strength : WEAK

Reason for weakness : ['DEMOGRAPHIC_DOB_SELF']

markdown
Copy
Edit

--------------------------
🧠 How It Works
--------------------------
- Parses input dates using `datetime.strptime`  
- Extracts possible vulnerable combinations like:
  - `DDMM`, `MMDD`, `YYMM`, `MMYY`, `DDYY`, etc.
- Compares the input M-PIN against:
  - Hardcoded sets of commonly used PINs
  - Dynamically generated date-based patterns

--------------------------
🚨 Notes
--------------------------
- Only supports 4 or 6 digit PINs
- Prints matched patterns for debugging (can be commented out)
- Ideal for security researchers or app developers creating PIN validation rules

--------------------------
📜 License
--------------------------
MIT License — do what you want, just don’t make your PIN "123456" again 😤

--------------------------
👨‍💻 Author
--------------------------
Made with a secure mindset by Martand Mishra (aka Genius)  
📧 Email: martandmishra473@gmail.com  
🔗 LinkedIn: https://linkedin.com/in/martand-mishra-geniusscholar  
🐙 GitHub: https://github.com/martand-mishra

--------------------------
✨ Quote
--------------------------
"Your mobile PIN is your first line of defense. Don’t make it your weakest link."
