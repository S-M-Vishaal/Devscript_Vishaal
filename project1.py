next = True
while next == True:
    print(''' 
    1) Aries
    2) Tauras 
    3) Gemini
    4) Cancer
    5) Leo
    6) Virgo 
    7) Libra
    8) Scorpio
    9) Sagittarius
    10) Capricon 
    11) Aquarius
    12) Pisces
     ''')

    s = int(input("Enter your sign number & Press Enter\n"))
    print(s)

    if s==1:
        print("Arrears or money from an unexpected source promises to fill your coffers. Convincing those who matter about your ideas will be a big achievement for you. Those feeling under the weather are likely to show marked improvement. You may involve yourself in social work and derive much satisfaction from it. A property issue is likely to be resolved amicably. An argument with spouse cannot be ruled out; avoid it if you can. You may take time out from your busy schedule to plan a short vacation to let your hair down.")
    elif s==2:
        print("Your choice of eating right and remaining active promises to keep you fit and energetic. Some of you will be able to maintain a high standard of performance all throughout. Someone may be rather too insistent in offering you an investment option, but don’t get carried away by his or her shoptalk With everything going great guns, there’s no way you can feel anything but great! You may not feel up to doing a time consuming job at home. A dream house is likely to become a reality for some. Travelling on a business trip is possible for those into export and import.")
    elif s==3:
        print(" Realising a handsome amount from someone is possible on the financial front. This is not the right time to disclose your business intentions; keep your competitors guessing. Registering a property in your name is possible. Those travelling may face delays due to unforeseen circumstances. Avoid being too sensitive on the home front. Thanks to your active life, you will feel more energetic now, than before. A hectic phase may finally be over, so set the old routine and get back to it.")
    elif s==4:
        print("An urgent requirement of money is likely to be met through your own savings. Doctors and engineers can expect a satisfying day both professionally and monetarily. You may take the initiative to enhance your physical fitness. Good performance in a sporting event will get you onto the centre stage. You may start repair work of your house or office. A new development on the home front may keep you preoccupied. An outing with family and friends is likely and will prove refreshing and restful.")    
    elif s==5:
        print("A profitable venture goes underway and promises to get the cash registers ringing. Keep a watchful eye on the business front as there are elements working against your interest. Circumstances may force you to compromise on eating right, but revert as soon as possible, before it starts affecting health. It is easy to shift the blame on someone, but be in their boots to realise the difficulties faced by them. A blissful existence is foreseen for the newlyweds. This is a favourable time to go in for a house or property. Visit to some friends or relatives are long overdue, so make plans to look them up.")
    elif s==6:
        print("This is a good time to go in for an investment that promises to turn lucrative and bring in good money. Explaining things in detail to a superior will help in clearing a misunderstanding at work. Those suffering from medical problems are likely to enter a healthier phase of life. Some of you may have to undertake an out of town journey. Homemakers are likely to have their hands full catering to guests. Your forthrightness in expressing yourself honestly will be appreciated. Your fears regarding a property matter will be ill-founded.")
    elif s==7:
        print("Your initiative on the health front promises to keep you fit and energetic. It is best not to indulge in office romance as it can affect your work adversely. Money will not be a problem now with increased earning. Something close to your heart gets a boost and delights you no end! A family relation may flatter you with his or her praise for you. Property or a new vehicle may be acquired by some. A break from the routine is indicated; it can very well be a vacation.")
    elif s==8:
        print("Managing your savings by wise investments is the need of the hour on the financial front. Be careful of competitors at work as they can beat you at the game of one-upmanship. Some of you are likely to take the possession of a house or an apartment. Visit to a place of religious significance may be in the planning stages. So, be prepared to enjoy the company of friends and relations. Your love for junk food may have serious repercussions on the health front. You shine like a beacon in a sea for someone who is depressed.")
    elif s==9:
        print("Someone may try to shoptalk you into an investment, but it is best not to get impulsive. You have the magic wand that will swing things in your favour on the professional front! You will manage to remain regular in your workouts and benefit. A vacation will give ample opportunity to enjoy the new locale and let your hair down. You will manage to take care of an elderly in the family. Someone will be at hand to give all kinds of suggestions, but don’t get unduly swayed especially by negative suggestions. Solid gains are seen for those investing in properties.")
    elif s==10:
        print("Unnecessarily worrying about your health may actually make you unwell! A family gathering will provide an excellent opportunity for bonding with those you don’t meet often. Professional excellence will help you in getting firmly established in the organisation. Some of you can end up paying more than intended for a product or service, but it will be worth it! Problems confronting you on the home front will disappear. Day seems favourable for builders and property dealers. Time constraints may deter you from travelling out of town.")
    elif s==11:
        print(" Sticking to daily fitness routine will not pose much problem for you. Some of you are likely to get slotted for a prized appointment or posting. You may find your coffer brimming, as a much-awaited balance payment is received. A social event may get you involved and help you win brownie points on the social front. Playing host to relatives is indicated and will be fun. This is a good day for negotiating a property deal. Those contemplating a long journey must travel only with confirmed arrangements.")
    elif s==12:
        print("Be careful about what you spend on, as you can end up wasting money. A soft approach in handling a subordinate will go a long way in encouraging a positive relationship. A health initiative promises to keep you fit and on the go. Take steps to resolve a property matter amicably. A fun-filled journey is foreseen and may keep you totally engrossed. Give ear to a family member’s advice as it will be for your own good. Someone is likely to get envious on the social front, so get ready to become the butt of gossips!")
    else:
        print("The number entered is not valid")

    temp = input("Can we do it again? Y/N\n")
    if temp == 'Y':
        next = True
    else:
        next = False        



